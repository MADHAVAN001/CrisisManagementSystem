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

weather_thread = WeatherController()

weather_thread.start() # This actually causes the thread to run
weather_thread.join()  # This waits until the thread has completed
# At this point, both threads have completed