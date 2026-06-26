import requests
from config import REST_API_KEY, REFRESH_TOKEN

def get_access_token():
    url = "https://kauth.kakao.com/oauth/token"

    data = {
        "grant_type": "refresh_token",
        "client_id": REST_API_KEY,
        "refresh_token": REFRESH_TOKEN
    }

    response = requests.post(url, data=data)
    result = response.json()

    return result["access_token"]