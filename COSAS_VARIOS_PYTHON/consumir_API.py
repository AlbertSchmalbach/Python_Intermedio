# from urllib import response
# from urllib.request import urlopen
# import json
# from pprint import pprint

# url = 'https://anime-facts-rest-api.herokuapp.com/api/v1'

# respuesta = urlopen(url)
# data = json.loads(respuesta.read())

# for d in data:
#     print(d['anime_img'])

import requests

url = "https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions"

headers = {
	"X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
