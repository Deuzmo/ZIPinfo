import json
import requests


def findby_country_and_zip(country, zip):
    response = requests.get("https://api.zippopotam.us/{}/{}".format(country,zip))
    if (response.status_code >= 400):
        return {"error" : "Error! tried to access wrong ZIP code"}
    elif (response.status_code >= 200 and response.status_code < 300):
        return response.json()
    else:
        return {"error": "Error! Something is not working with the server"}