import requests

url = 'https://api.weather.yandex.ru/v2/informers?lat=55.75396&lon=37.620393'
res = requests.get(url, headers={'X-Yandex-API-Key': '8aa0c4b5-3e77-4fdc-8260-f37f76357da6'})
print(res.text)
print(res.status_code, res.url)

