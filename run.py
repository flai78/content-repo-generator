# importing the requests library
import requests
  
# api-endpoint
URL = "https://spotest.free.beeceptor.com/api/test"
  
# location given here
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API
BODY = {'address':location}

HEADERS = {'x-test-data':'pippo'}
  
# sending get request and saving the response as response object
r = requests.post(url = URL, json=BODY, headers=HEADERS)
  
# extracting data in json format
data = r.json()
  
  
# extracting latitude, longitude and formatted address 
# of the first matching location
mydata = data['mydata']
  
# printing the output
print("mydata:%s\n"
      %(mydata))