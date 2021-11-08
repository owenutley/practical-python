import requests

api_key = "1141afdd1ead5402c22a9aead0dd7ae1"
city = "Orlando"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

request = requests.get(url)
json = request.json()
print(json)
