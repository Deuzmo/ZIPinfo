import json
import requests


def findby_country_and_zip(country, zip):
    response = requests.get("https://api.zippopotam.us/{}/{}".format(country,zip))
    return response.json()