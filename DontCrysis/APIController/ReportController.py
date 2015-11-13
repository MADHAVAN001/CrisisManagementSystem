__author__ = 'Ankur Bansal'

import threading
import time
from DontCrysis.Utility.ReportAPI import generate
from DontCrysis.Utility.ReportSend import GmailAPI
from DontCrysis.models import ReportReceiver

class ReportController(threading.Thread):
     def __init__(self):
         super(ReportController, self).__init__()

     def run(self):
        last_report_send = 0
        while((int(round(time.time() * 1000)) - last_report_send) > (0.5 * 60 * 60 * 1000 )):
            last_report_send = int(round(time.time() * 1000))
            generate()
            message = "Dear PMO, \n\n Attached is the report containing the updated status of Events in Singapore during the period of last 30 minutes." \
                      " We will continue to send you updates on all matters requiring your assisstance. \n" \
                      "\n \nThanks & Regards,\nDontCrysis Team"
            subject = "[DontCrysis] Routine Update"

            report_receivers = ReportReceiver.objects.all()
            for item in report_receivers:
                GmailAPI(subject,message,item.email)


