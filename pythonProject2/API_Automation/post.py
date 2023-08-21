import requests
import json
import jsonpath
url = "https://reqres.in/api/users"

# Read json input
file = open('C:\\Users\\vijay\\OneDrive\\Desktop\\API NoteBook\\Sample.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

# Make post request with json input body
response = requests.post(url, request_json)
print(response)

# Validating response Code

assert response.status_code == 201

# Fetch Header Response Code
print(response.headers.get("Content-Length"))

# Parse response to Json format
response_json = json.loads(response.text)

# Pick up Id using Json Path

Id = jsonpath.jsonpath(response_json, 'id')
print(Id)
