import requests

payload = {"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params= payload, verify=False)
print(response.text)

response_text = requests.get("https://playground.learnqa.ru/api/get_text", verify = False)
print(response_text)
