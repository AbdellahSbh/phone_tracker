#Disclaimer!!!!!
#This program was done and it can only be used for an educational purpose and testing any use of it for hacking or illegal tracking can lead to a lawsuit
#Abdellah Sabhi 


import phonenumbers
from phonenumbers import geocoder
from phone import number
import folium

key = "67b6f0ebf0864d1da886d8e02c00637b"

check_number = phonenumbers.parse(number)
location= geocoder.description_for_number(check_number, "en")
print(location)

from phonenumbers import carrier
service_provider= phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder= OpenCageGeocode(key)
query = str(location)
results= geocoder.geocode(query)

lat= results[0]['geometry']['lat']
lng= results[0]['geometry']['lng']

print("latitude and longitude", lat,lng)

Mymap= folium.Map(location=[lat , lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(Mymap)

Mymap.save("location.html")
