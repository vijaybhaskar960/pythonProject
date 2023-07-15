import json
import requests
import jsonpath


url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response.status_code)


# Parse response to json format

json_response = json.loads(response.text)
print(json_response)


# Fetch value using json path
pages = jsonpath.jsonpath(json_response,"total")
print(pages)

json_response = json.loads(response.text)

pages = jsonpath.jsonpath(json_response, "id")
print(pages)

