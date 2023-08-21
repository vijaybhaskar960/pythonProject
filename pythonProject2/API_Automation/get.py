import requests

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)

json_response = response.json()
print(json_response)
print(json_response['total'])
print(json_response['data'][0]['email'])
print(json_response['data'][0]['last_name'])
