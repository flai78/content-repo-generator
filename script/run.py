# importing the requests library
import requests
import datetime
import os
  
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
  

# of the first matching location
mydata = data['mydata']
  
# printing the output
print("mydata:%s\n"
      %(mydata))

f = open('./tmp/pkey.txt', 'w+')

update_date = datetime.datetime.now()

f.write(f"Update on {update_date} \r\n")
f.write(f"Data from web service {mydata} \r\n")
super_secret = os.getenv('SUPER_SECRET')
f.write(f"Value from GitHub secret DATA_KEY: {super_secret} \r\n")

for i in range(10):
     f.write("This is line %d\r\n" % (i+1))

f.close()