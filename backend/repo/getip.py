import requests


def getIp():
    return requests.get("https://api.ipify.org?format=json").json()["ip"]
