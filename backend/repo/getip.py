import httpx


def getIp():
    return httpx.get("https://api.ipify.org?format=json").json()["ip"]
