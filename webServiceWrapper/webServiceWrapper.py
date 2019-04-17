import requests
import json

# Global config settings
SERVER_URL = 'http://localhost:8080'

# possible routes
routes = {
    "addTwoNums": "/addTwoNums"
}


# Call addTwoNums route for web services
def addTwoNums(x, y):
    resp = {}
    url = SERVER_URL + routes['addTwoNums']
    params = {"num1": x, "num2": y}
    try:
        resp = requests.post(
            url=url,
            data=json.dumps(params))
    except Exception as e:
        requestError(e)

    data = resp.json()
    return data


def requestError(e):
    return "HTTP Request Error: ".format(e)
