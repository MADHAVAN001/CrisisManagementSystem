__author__ = 'Ankur Bansal'

import threading
import time
from DontCrysis.Utility.HazeAPI import checkHaze
from DontCrysis.Utility.HazeUpdate import HazeTable_Update
from DontCrysis.models import Subscriber
from DontCrysis.Utility.GmailAPI import GmailAPI

class HazeController(threading.Thread):
    def __init__(self):
        super(HazeController, self).__init__()

    def HazeAlert(reading,area_code):

        area_lookup={4 : ['69', '70', '71', '72', '73', '75', '76', '77', '78', '79', '80'],
                     3 : ['42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '81'],
                     2 : ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '14', '15', '16', '17', '18', '19',
                          '22', '23', '24', '25', '26', '27', '28', '29', '30', '38', '39', '40', '41' ],
                     5 : ['20', '21', '31', '32', '33', '34', '35', '36', '37', '53', '54', '55', '56', '57', '82'],
                     6 : ['13', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68']}

        postal_codes = area_lookup[area_code]
        subscribers = Subscriber.objects.all()

        subject = "Haze Alert"
        message = "Haze level above 300. Please stay indoors and stop all outdoor activities."

        for item in postal_codes:
            for item2 in subscribers:
                if(item == item2.postalcode[0:1]):
                    GmailAPI(subject,message,item2.email)

    def run(self):
        last_haze_check = 0
        haze_readings = []
        while((int(round(time.time() * 1000)) - last_haze_check) > (3 * 60 * 60 * 1000 )):
            last_haze_check = int(round(time.time() * 1000))
            haze_readings = checkHaze()

        print haze_readings
        haze_table = {4 : haze_readings[0], 5 : haze_readings[1], 3 : haze_readings[2], 6 : haze_readings[3], 2 : haze_readings[4] }
        for key in haze_table:
            HazeTable_Update(haze_table[key],key)
            if(haze_table[key] > 300):
                self.HazeAlert(haze_table[key],key)

haze_thread = HazeController()
haze_thread.start() # This actually causes the thread to run
haze_thread.join()  # This waits until the thread has completed
# At this point, both threads have completed