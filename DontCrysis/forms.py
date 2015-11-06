from django import forms
from models import Subscriber
from models import Crisis
from models import ReportReceiver

TYPE=(
    (1, 'FIRE' ),
    (2, 'FLOOD'),
    (3, 'MEDICAL EMERGENCY'),
    (4, 'INDUSTRIAL ACCIDENT'),
    (5, 'THUNDERSTORM'),
    (6, 'VOLCANIC ERUPTION'),
    (7, 'TSUNAMI'),
    (8, 'TORNADO/HURRICANE'),
    (9, 'EARTHQUAKE'),
    (10, 'OTHERS')
)
SEVERITY =(
    (1, 'EXTREMELY URGENT'),
    (2, 'VERY URGENT'),
    (3, 'URGENT'),
    (4, 'LESS URGENT'),
    (5, 'VERY LESS URGENT')
)

class CrisisCreateForm(forms.ModelForm):
    type = forms.ChoiceField(choices=TYPE, required=True )
    severity = forms.ChoiceField(choices=SEVERITY, required=True )
    class Meta:
        model=Crisis
        exclude=['isActive','date','time']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = "__all__"

class ReportReceiverForm(forms.ModelForm):
    class Meta:
        model = ReportReceiver
        fields = "__all__"

class CrisisForm(forms.ModelForm):
    type = forms.ChoiceField(choices=TYPE, required=True )
    severity = forms.ChoiceField(choices=SEVERITY, required=True )
    class Meta:
        model = Crisis
        fields = ['description','postalcode', 'severity' ]
