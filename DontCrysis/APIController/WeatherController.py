__author__ = 'Ankur Bansal'

import threading
import time
from DontCrysis.Utility.WeatherAPI import check_weather

class WeatherController(threading.Thread):
     def __init__(self):
         super(WeatherController, self).__init__()

     def run(self):
        last_weather_check = 0
        while((int(round(time.time() * 1000)) - last_weather_check) > (1 * 60 * 60 * 1000 )):
            last_weather_check = int(round(time.time() * 1000))
            weather_readings = check_weather()
            print weather_readings

<<<<<<< HEAD
#weather_thread = WeatherController()

=======


>>>>>>> 82af89de859962f9a0621c6de54d286a5cc835a4
#weather_thread.start() # This actually causes the thread to run
#weather_thread.join()  # This waits until the thread has completed
# At this point, both threads have completed