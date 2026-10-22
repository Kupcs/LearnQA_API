"""Ex6: Длинный редирект
Необходимо написать скрипт, который создает GET-запрос на метод: https://playground.learnqa.ru/api/long_redirect
С помощью конструкции response.history необходимо узнать, сколько редиректов происходит от изначальной точки
назначения до итоговой. И какой URL итоговый.
Ответ опубликуйте в виде ссылки на коммит со скриптом, а также укажите количество редиректов и конечный URL."""

import requests

url = "https://playground.learnqa.ru/api/long_redirect"
response = requests.get(url, verify=False)
redirect_count = len(response.history)
last_url = response.history[-1].url
url_path = [i.url for i in response.history]

print(f"URL path: {url_path}")
print(f"Redirect count: {redirect_count}")
print(f"Last url: {last_url}")
