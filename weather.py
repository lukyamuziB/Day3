import requests

API_KEY= "bc7cb8fb59984a4d9a373932170507"
CORE_URL= "http://api.apixu.com/v1/"
PATH_FOR_CURRENT= CORE_URL+"current.json?key="+API_KEY
PATH_FOR_FORECAST= CORE_URL+"forecast.json?key="+API_KEY
data= {}

#gets integer, prompting retry on invalid input
def get_option(notif):
	number= int(input(notif))
	while(not isinstance(number,int)):
		number= raw_input("Please pick a valid option:  ")
	return int(number)

print("\n")
print("______________HELLO, WELCOME TO MY SIMPLE WEATHER FORECAST PROGRAM_____________\n\n\n\n\n")
city= input("I would like the forcast for: ")
print (city)

data["q"]= city

pref= get_option("1. Current or 2. Forecast\n")
pref= PATH_FOR_FORECAST if pref is 2 else PATH_FOR_CURRENT

reply= requests.get(pref, params=data)

# print ("your reply URL is" + reply.url)
pref= get_int("1. Current or 2. Forecast\n")

if pref is 2:
	data.update(get_forecast_options())

pref= PATH_FOR_FORECAST if pref is 2 else PATH_FOR_CURRENT

print("Getting weather forecast for "+city+"...")

try:
	reply= requests.get(pref, params=data)
except Error.ConnectionError as e:
	print ("The Service is currently down, please retry in a few seconds :)\nOr make sure you have a working internet connection")

if not reply.status_code == requests.codes.ok:
	print ("The Service is currently down, please retry in a few seconds :)")

reply= (reply.json())["current"] if pref is PATH_FOR_CURRENT else (reply.json())["forecast"]["forecastday"] #extract current object

if pref is PATH_FOR_CURRENT:
	print( city+ " is "+ reply["condition"]["text"]+ " today, at "+ str(reply["temp_c"])+" degrees. "+ "It feels more like "+ str(reply["feelslike_c"])+ " degress though!")
else:
	for day in range(0, data["days"]):
		print ("Tomorrow," if day is 0 else "Then the next day,",)
print (city+ " will be "+ reply[day]["day"]["condition"]["text"]+ ", at "+ str(reply[day]["day"]["avgtemp_c"])+" degrees on average.")