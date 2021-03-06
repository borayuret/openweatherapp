# openweathermap.org sitesinden şehir sıcaklık verisi çekeceğiz.

# key: 24bb5a00705b2420901490c95519ab0b

# Api Call: http://api.openweathermap.org/data/2.5/weather?q=ankara&appid=24bb5a00705b2420901490c95519ab0b


import requests
import json


api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q=ankara&appid=24bb5a00705b2420901490c95519ab0b")

# result dönen JSON dökümanıdır.
result = json.loads(api_request.content)


print(result)