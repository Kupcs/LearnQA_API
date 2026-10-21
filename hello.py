import requests

response = requests.get("https://playground.learnqa.ru/api/hello", verify=False)
print(response.text)

response_text = requests.get("https://playground.learnqa.ru/api/get_text", verify = False)
print(response_text)
