import requests

response = requests.get("https://reqres.in/api/users?page=2")
print(response)
code = response.status_code
# print(dir(response))
assert code == 200, 'Code is Mached'
# print(response.text)
# print(response.content)
res = response.json()
print(res['total'])



