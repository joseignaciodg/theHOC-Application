import pyowm # Python Open Weather
from geopy.geocoders import Nominatim
import sys

key = '61be56cc6f5a837ea95f719805978b70'
city = 'Milan'

#obtener latitud y longitud

geolocator = Nominatim(user_agent='myapplication')
location = geolocator.geocode(city)

LON = location.longitude
LAT = location.latitude

#obtener informacion tiempo

openMap = pyowm.OWM(key)   
openMaps = openMap.weather_manager()                
tiempo = openMaps.weather_at_place(city)  
data = tiempo.weather                  

#print ('-----------------------------------------------------------')

#print ('STATUS: ', data.detailed_status)
#print('WIND: ', data.wind)   
#print('HUMIDITY: ', data.humidity)     
#print('TEMPERATURE IN CELSIUS: ', data.temperature('celsius')) 
#print('RAIN: ', data.rain)    
#print('HEAT INDEX: ', data.heat_index) 
#print('CLOUDS: ', data.clouds)

#print ('-----------------------------------------------------------')

#prediccion para el dia
one_call = openMaps.one_call(lat=LAT, lon=LON)

original_stdout = sys.stdout # Save a reference to the original standard output

with open('tiempo.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    
    print ('During the day we are going to have', one_call.forecast_daily[0].detailed_status)
    temp = data.temperature('celsius')
    print ('The actual temperature is ', temp['temp'])      
    print ("The maximum is going to be ", temp['temp_max'])
    print ("And the minimum  ", temp['temp_min'])
    print ("The most important, it feels like ", temp['feels_like'])
    print ("It is not raining right now.")
    print ('And the actual humidity is ', data.humidity)     
    sys.stdout = original_stdout # Reset the standard output to its original value

