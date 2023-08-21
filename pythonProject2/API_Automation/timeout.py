import requests

response = requests.get('https://httpbin.org/delay/5')
print(response)
print(response.status_code)