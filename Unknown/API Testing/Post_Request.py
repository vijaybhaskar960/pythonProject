import json
import jsonpath
import requests

url = "https://reqres.in/api/users"

file = open("C:\\Users\\Vijay Bhaskar Reddy\\Downloads\\demo.json",'r')
json_input = file.read()

response_json = json.loads(json_input)
print(response_json)

response = requests.post(url,response_json)
print(response.content)
print(response.status_code)

# Fetch date header

ele = jsonpath.jsonpath(response_json,'id')
print(ele[0])

