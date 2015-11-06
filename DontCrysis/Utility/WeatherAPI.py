__author__ = 'Ankur Bansal'

import json
import urllib2



def return_weather_data():
    singapore_weather_url = 'http://api.wunderground.com/api/56e9258a7b8f52b9/geolookup/conditions/forecast/q/Singapore/Singapore.json'
    json_urlopener = urllib2.urlopen(singapore_weather_url)
    data = json.load(json_urlopener)
    data_current_observation=data['current_observation']
    temp_c=int(data_current_observation['temp_c'])
    weather_condition=data_current_observation['weather']
    relative_humidity=data_current_observation['relative_humidity']
    visibility_km=float(data_current_observation['visibility_km'])
    precip_1hr_in=float(data_current_observation['precip_1hr_in'])
    wind_kph=float(data_current_observation['wind_kph'])
    uv_index=int(data_current_observation['UV'])
    if temp_c=='':
        temp_c='NA'
    if weather_condition=='':
        weather_condition='NA'
    if relative_humidity=='':
        relative_humidity='NA'
    if visibility_km=='':
        visibility_km='NA'
    if wind_kph=='':
        wind_kph='NA'
    if precip_1hr_in=='':
        precip_1hr_in='NA'
    if uv_index=='':
        uv_index='NA'

    data={'temp_c':temp_c, 'weather_condition':weather_condition,
          'relative_humidity':relative_humidity, 'visibility_km':visibility_km, 'wind_kph':wind_kph,
          'precip_1hr_in': precip_1hr_in, 'UV':uv_index}
    return data


def check_weather():
    weather_data = return_weather_data()
    #print weather_data
    report_weather=[]
    #Temperature Status
    if((weather_data['temp_c']>=45)):
        report_weather.append("> = 45 C")
    elif((weather_data['temp_c']>=35)):
        report_weather.append("35 - 45 C")
    elif((weather_data['temp_c']>=25)):
        report_weather.append("25 - 35 C")
    elif((weather_data['temp_c']>=10)):
        report_weather.append("10 - 25 C")
    elif(weather_data['temp_c']<10):
        report_weather.append("< 10 C")
    else:
        report_weather.append("Temperature NA")

    #Weather Status
    if(weather_data['weather_condition'] != 'NA'):
        report_weather.append(weather_data['weather_condition'])
    else:
        report_weather.append("Weather Status NA")

    #Visibility Status
    if(weather_data['visibility_km']<1):
        report_weather.append("Very Poor visibility")
    elif(weather_data['visibility_km']<=4):
        report_weather.append("Poor visibility")
    elif(weather_data['visibility_km']<=10):
        report_weather.append("Moderate visibility")
    elif(weather_data['visibility_km']<=20):
        report_weather.append("Good visibility")
    elif(weather_data['visibility_km']<=40):
        report_weather.append("Very good visibility")
    elif(weather_data['visibility_km']>40):
        report_weather.append("Excellent visibility")
    else:
        report_weather.append("Visibility NA")

    #Wind Speed Status
    if(weather_data['wind_kph']>150):
        report_weather.append("Heavy Thunderstorm")
    elif(weather_data['wind_kph']>65):
        report_weather.append("Strong Thunderstorm")
    elif(weather_data['wind_kph']>50):
        report_weather.append("High wind speed")
    elif(weather_data['wind_kph']<=50):
        report_weather.append("Normal wind conditions")
    else:
        report_weather.append("Wind data NA")

    #Rain Status
    if(weather_data['precip_1hr_in']>2.00):
        report_weather.append("Extremely heavy rain")
    elif(weather_data['precip_1hr_in']>0.63):
        report_weather.append("Very heavy rain")
    elif(weather_data['precip_1hr_in']>0.16):
        report_weather.append("Heavy rain")
    elif(weather_data['precip_1hr_in']>0.04):
        report_weather.append("Moderate rain")
    elif(weather_data['precip_1hr_in']>0.0098):
        report_weather.append("Light rain")
    elif(0<weather_data['precip_1hr_in']<=0.0098 ):
        report_weather.append("Drizzle")
    elif(weather_data['precip_1hr_in']<=0.00):
        report_weather.append("No rain")
    else:
        report_weather.append("Rain data NA")

    report_weather.append(weather_data['relative_humidity'])

    #UV Index Status
    if(weather_data['UV']<1):
        report_weather.append("No exposure. No protection required.")
    elif(1<=weather_data['UV']<=2):
        report_weather.append("Low exposure. No protection required.")
    elif(2<weather_data['UV']<=5):
        report_weather.append("Moderate exposure. Seek shade during midday hours, cover up and wear sunscreen. ")
    elif(5<weather_data['UV']<=7):
        report_weather.append("High exposure. Seek shade during midday hours, cover up and wear sunscreen. ")
    elif(7<weather_data['UV']<=10):
        report_weather.append("Very high exposure. Avoid being outside during midday hours; shirt, suncreen and hat are essential.")
    elif(weather_data['UV']>10):
        report_weather.append("Very high exposure. Avoid being outside during midday hours; shirt, suncreen and hat are essential.")
    else:
        report_weather.append("UV index NA")

    return report_weather

#check_weather()
