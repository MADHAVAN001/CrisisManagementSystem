__author__ = 'Ankur Bansal'

import threading
from DontCrysis.Utility.FacebookAPI import FacebookAPI
from DontCrysis.models import Crisis
from DontCrysis.models import Agency

class FacebookController(threading.Thread):
     def __init__(self,id,type):
        super(FacebookController, self).__init__()
        self.id = id
        self.type = type

     def run(self):
        crisis = Crisis.objects.get(id = self.id)
        agency = Agency.objects.filter(type = self.type)
        agency_info = ""
        for item in agency:
            agency_info = agency_info + "Name : " + item.name + ",\tContact : " + item.telephone + "\n"

        message = "An alert for " + crisis.title + " in your area was reported at " + str(crisis.time) + \
                   ". The description provided by the reporter is as follows : \'" + crisis.description + "\'. \nThis email is to notify " \
                "you of the situation. Please contact the following agencies in case you require any assitance : \n\n" + agency_info \
                   + "\n\n The relevant emergency personnel has been dispatched to take control of the situation. \n\nTake Care."
        FacebookAPI(message)
