import requests
import json


# res = requests.get(url, headers=headers, params=params) #пример


# latitude = '55'
# longitude = '37'
# res = requests.get( "http://api.open-notify.org/iss-pass.json?lat="+latitude+"&lon="+longitude)
# print(res.text)

def get_api_key(email: str, passwd: str):
    headers = {
        'sorvanezz@gmail.com': email,
        'Raty567': passwd,
    }
    res = requests.get('https://petfriends1.herokuapp.com/api/key', headers=headers)
    status = res.status_code
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return status, result


print(get_api_key('sorvanezz@gmail.com', 'Raty567'))
