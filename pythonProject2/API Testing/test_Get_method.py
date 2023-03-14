import requests
import json
import jsonpath

def test_create_new_user():
    url = "https://reqres.in/api/users"

    # Read input Json file
    file = open("C:\\Users\\vijay\\OneDrive\\Desktop\\demo.json",'r')
    json_input = file.read()
    response_json = json.loads(json_input)
    print(response_json)

    # Make POST request with Json Input body
    response = requests.post(url,response_json)
    print(response.content)

    # Validating Response Code
    assert response.status_code == 201

    # Fetch Header from Response
    print(response.headers.get('Content-Lenght'))

    # Parse response to Json Format

    response_json = json.loads(response.text)

    # Pick Id using Json Format
    id = jsonpath.jsonpath(response_json,'id')
    print(id)