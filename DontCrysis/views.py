from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.template import Context
from forms import SubscriberForm,CrisisCreateForm, ReportReceiverForm, CrisisForm
from django.core.context_processors import csrf
from models import Crisis, Agency, ReportReceiver
from django.core.urlresolvers import reverse_lazy
import datetime
import ctypes
from DontCrysis.Utility.SmsAPI import sendsms
from DontCrysis.APIController.EmailController import EmailController
from DontCrysis.APIController.FacebookController import FacebookController
from DontCrysis.APIController.HazeController import HazeController
from DontCrysis.APIController.WeatherController import WeatherController
import DontCrysis.Utility.FusionTable
from DontCrysis.APIController.ReportController import ReportController
# Create your views here.

TYPE={  1: 'FIRE' ,
        2: 'FLOOD',
        3: 'MEDICAL EMERGENCY',
        4: 'INDUSTRIAL ACCIDENT',
        5: 'BAD WEATHER',
        6: 'OTHERS'
     }

def homepage(request):
    haze_thread = HazeController()
    weather_thread = WeatherController()
    report_thread = ReportController()
    haze_thread.start()
    weather_thread.start()
    report_thread.start()
    return render(request,'homepage.html')

def homepage_map2(request):
    return render(request,'homepagemap2.html')

def subscribe(request):
    return render(request, 'Subscribe.html')

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('Login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')

def loggedin(request):
    crises = Crisis.objects.all().order_by('-date','-time')
    reports= ReportReceiver.objects.all()
    return render(request,'loggedin.html',{'crises' :crises, 'reports':reports})

def invalid_login(request):
    return render_to_response('invalid.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')

    else:
        form = UserCreationForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('register.html', args)



def register_success(request):
    return render_to_response('register_success.html')

def createSubscriber(request):
    if request.POST:
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/subscriber_successful')
    else:
        form = SubscriberForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
    return render_to_response('Subscribe.html', args)

#@login_required(redirect ka url)
def addReportReceiver(request):
     if request.POST:
        form = ReportReceiverForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/loggedin')
     else:
        form = ReportReceiverForm()
     args = {}
     args.update(csrf(request))

     args['form'] = form
     return render_to_response('add_report_receiver.html', args)

def report_reciever_added(request):
    return render_to_response('loggedin.html')

def subscriber_successful(request):
    return render_to_response('homepage.html')


def crisis_create(request):
    # To prevent access to pages that require login
    if not request.user.is_authenticated():
        ctypes.windll.user32.MessageBoxA(0, "You are not logged in","Not logged in!", 1)
        return login(request)

    if request.POST:
        form=CrisisCreateForm(request.POST)
        if form.is_valid():
            crisis = form.save(commit=False);
            crisis.date = datetime.date.today()
            crisis.time = datetime.datetime.now().time()
            crisis.save()
            type = crisis.type
            DontCrysis.Utility.FusionTable.insert(str(TYPE.get(type)),crisis.postalcode)
            sendsms(request,crisis)
            email_thread = EmailController(crisis.id,crisis.type)
            facebook_thread = FacebookController(crisis.id,crisis.type)
            facebook_thread.start()
            email_thread.start() # This actually causes the thread to run
            #email_thread.join()  # This waits until the thread has completed
            # At this point, both threads have completed
            return HttpResponseRedirect('/crisis/status')
    else:
        form=CrisisCreateForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('crisis_create.html', args)

'''def crisis_create(request):
    if request.POST:
        form=CrisisCreateForm(request.POST)
        if form.is_valid():
            crisis_type=form.cleaned_data['type']
            crisis = form.save(commit=False);
            crisis.date = datetime.date.today()
            crisis.time = datetime.datetime.now().time()
            crisis.save()
            request.session['type']=crisis_type
            return HttpResponseRedirect('/crisis/status', crisis.type)
    else:
        form=CrisisCreateForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('crisis_create.html', args)'''

def status_crisis(request):
    crisis_type=request.session.get('type')
    agency = Agency.objects.filter(type=crisis_type)
    return render(request, 'status_crisis.html', {'agency':agency})

def crisis_update(request, pk, template_name='update_crisis.html'):
    crisis = get_object_or_404(Crisis, pk=pk)
    form = CrisisForm(request.POST or None, instance=crisis)
    if form.is_valid():
        form.save()
        return redirect('/loggedin')
    return render(request, template_name, {'form':form})

def crisis_toggle_active(request, pk, template_name='loggedin.html'):
    crisis = get_object_or_404(Crisis, pk=pk)
    if crisis.isActive:
            crisis.isActive = 0
            DontCrysis.Utility.FusionTable.delete(str(TYPE.get(crisis.type)),crisis.postalcode)
    else:
            crisis.isActive = 1
            DontCrysis.Utility.FusionTable.insert(str(TYPE.get(crisis.type)),crisis.postalcode)
    crisis.save()
    return redirect('/loggedin')


def crisis_delete(request, pk, template_name='crisis_confirm_delete.html'):
    crisis = get_object_or_404(Crisis, pk=pk)
    if request.method=='POST':
        crisis.delete()
        return redirect('/loggedin')
    return render(request, template_name, {'object':crisis})


