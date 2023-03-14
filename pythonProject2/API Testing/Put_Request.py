import jsonpath
import requests
import json

url = "https://reqres.in/api/users/2"

file = open("C:\\Users\\vijay\\OneDrive\\Desktop\\demo.json",'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

# Make Put request with json Input body

response = requests.put(url,request_json)
print(response)

response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response,'name')
print(updated_li)




