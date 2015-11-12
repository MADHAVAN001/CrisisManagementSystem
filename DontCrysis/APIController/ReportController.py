__author__ = 'Ankur Bansal'

import threading
import time
from DontCrysis.Utility.ReportAPI import generate

class ReportController(threading.Thread):
     def __init__(self):
         super(ReportController, self).__init__()

     def run(self):
        last_report_send = 0
        while((int(round(time.time() * 1000)) - last_report_send) > (0.5 * 60 * 60 * 1000 )):
            last_report_send = int(round(time.time() * 1000))
            generate()

report_thread = ReportController()

report_thread.start() # This actually causes the thread to run
report_thread.join()  # This waits until the thread has completed
# At this point, both threads have completed