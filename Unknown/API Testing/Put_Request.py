import json
import jsonpath
import requests

url = "https://reqres.in/api/users/2"

file = open("C:\\Users\\Vijay Bhaskar Reddy\\Downloads\\demo.json",'r')
json_input = file.read()

response_json = json.loads(json_input)
print(response_json)

response = requests.put(url,response_json,)
print(response.status_code)

# Parse response content
response_json = json.loads(response.text)

Updated = jsonpath.jsonpath(response_json,"job")
print(Updated[0])

