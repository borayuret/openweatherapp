# openweathermap.org sitesinden şehir sıcaklık verisi çekeceğiz.

# key: 24bb5a00705b2420901490c95519ab0b

# Api Call: http://api.openweathermap.org/data/2.5/weather?q=ankara&appid=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

import requests
import json
import cevir

sehir = input("Şehri giriniz:")
sehirD = (sehir[0:1].replace("i", "İ")+sehir[1:]).capitalize()

api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+sehir+"&appid=24bb5a00705b2420901490c95519ab0b")

# result dönen JSON dökümanıdır.
result = json.loads(api_request.content)


#print(result)

hava_sozlu = {
    "Clouds": "Bulutlu",
    "Clear": "Açık",
    "Rain": "Yağmurlu"
}

print(sehirD + " sıcaklığı: {} K".format(result["main"]["temp"]))
print(sehirD + " sıcaklığı: {0:.2f} C".
      format(cevir.kelvin_to_celcius(result["main"]["temp"])))
print(sehirD + " sıcaklığı: {} C".
      format(round(cevir.kelvin_to_celcius(result["main"]["temp"]), 2)))
print(sehirD + " sıcaklığı: {0:.2f} F".
      format( cevir.kelvin_to_fahrenheit(result["main"]["temp"])))



print(sehirD + " havası(sözlü):", hava_sozlu[result["weather"][0]["main"]])
