import requests

API_KEY= "bc7cb8fb59984a4d9a373932170507"
CORE_URL= "http://api.apixu.com/v1/"
PATH_FOR_CURRENT= CORE_URL+"current.json?key="+API_KEY
PATH_FOR_FORECAST= CORE_URL+"forecast.json?key="+API_KEY
data= {}

#gets integer, prompting retry on invalid input
def get_option(notif):
	number= int(input(notif))
	while(number.isdigit()==False):
		number= raw_input("Please pick a valid option:  ")
	return int(number)

city= input("I would like the forcast for: ")
print (city)

data["q"]= city

pref= get_option("1. Current or 2. Forecast\n")
pref= PATH_FOR_FORECAST if pref is 2 else PATH_FOR_CURRENT

reply= requests.get(pref, params=data)

print (reply.url)

reply= (reply.json())["current"]

print (city+ " is "+ reply["condition"]["text"]+ " today, at "+ str(reply["temp_c"])+" degrees. "+ "It feels more like "+ str(reply["feelslike_c"])+ " degress though!")