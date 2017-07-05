import requests
import requests.exceptions as Error

data= {}
API_KEY= "bc7cb8fb59984a4d9a373932170507"
CORE_URL= "http://api.apixu.com/v1/"
PATH_FOR_CURRENT= CORE_URL+"current.json?key="+API_KEY

print("\n")
print("______________HELLO, WELCOME TO MY SIMPLE WEATHER PROGRAM_____________\n\n")
city= input("Input the City whose weather info you need: ")
print (city)

data["q"]= city
reply= requests.get(PATH_FOR_CURRENT, params = data)
print ("your reply URL is: " + reply.url+"\n")
print("Getting weather forecast for "+city+"...\n")

try:
	reply= requests.get(PATH_FOR_CURRENT, params=data)
except Error.ConnectionError as e:
	print ("The Service is currently down, please retry in a few seconds :)")

if not reply.status_code == requests.codes.ok:
	print ("The Service is currently down, please retry in a few seconds :)")

reply= (reply.json())["current"]

print( city + " is "+ reply["condition"]["text"]+ " today, at "+ str(reply["temp_c"])+" degrees. "+ "It feels more like "+ str(reply["feelslike_c"])+ " degress though!")
print("The wind speed is at: "+ str(reply["wind_kph"])+ " Kilometers per hour\n" + "The pressure is at: "+ str(reply["pressure_mb"])+" millibars")
print("The humdity percentage is at: "+ str(reply["humidity"])+ "%\n"+"Cloud coverage is at: "+ str(reply["cloud"])+"%")
print("Today's Precipitation in millimeters is at: "+ str(reply["precip_mm"])+"\nGeneral wind Direction: "+ str(reply["wind_degree"])+ " " +reply["wind_dir"])
