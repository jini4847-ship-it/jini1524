import requests
from config import REST_API_KEY, REFRESH_TOKEN, CLIENT_SECRET

def get_access_token():
    url = "https://kauth.kakao.com/oauth/token"

    data = {
        "grant_type": "refresh_token",
        "client_id": REST_API_KEY,
        "refresh_token": REFRESH_TOKEN
    }

    response = requests.post(url, data=data)
    result = response.json()

    print("토큰 응답:", result)   # ← 이 줄 추가

    if "access_token" not in result:
        raise Exception(f"토큰 갱신 실패: {result}")

    return result["access_token"]