
import threading
from DontCrysis.models import Crisis
from DontCrysis.models import Agency
from DontCrysis.models import Subscriber
from DontCrysis.Utility.GmailAPI import GmailAPI
from django.http import request

class EmailController(threading.Thread):
    def __init__(self,id,type):
        super(EmailController, self).__init__()
        self.id = id
        self.type = type

    def run(task):
        #crisis_id = request.session.get('id')
        #crisis_type = request.session.get('type')
        crisis = Crisis.objects.get(id = self.id)
        agency = Agency.objects.filter(type = self.type)

        crisis_title = crisis.title
        crisis_time = str(crisis.time)
        crisis_postal_code = crisis.postalcode
        crisis_description = crisis.description

        agency_info = ""
        for item in agency:
            agency_info = agency_info + "Name : " + item.name + ",\tContact : " + item.telephone + "\n"

        subject = "" + crisis_title + 'Alert : Started at ' + crisis_time
        message2 = "\n\nAn alert for " + crisis_title + " in your area was reported at " + crisis_time + \
                  ". The description provided by the reporter is as follows : \'" + crisis_description + "\'. \nThis email is to notify " \
                    "you of the situation. Please contact the following agencies in case you require any assitance : \n\n" + agency_info \
                  + "\n\n The relevant emergency personnel has been dispatched to take control of the situation. \n\nTake Care.\nRegards," \
                    "\nDont Crysis Team"

        subscribers = Subscriber.objects.filter(postalcode = crisis_postal_code)

        for item in subscribers:
            message = "Dear "+item.name + message2
            GmailAPI(subject,message,item.email)
