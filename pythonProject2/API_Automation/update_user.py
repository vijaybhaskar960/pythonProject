import requests
import jsonpath
import json


url = "https://reqres.in/api/users/2"

payload = {
    "name": "Nikitha",
    "job": "Java-Developer"
}

response = requests.put(url, data=payload)
print(response)
json_response = json.loads(response.text)
print(json_response)

job = jsonpath.jsonpath(json_response, 'job')
job = jsonpath.jsonpath(json_response, 'name')
job = jsonpath.jsonpath(json_response, 'updatedAt')


print(job)


