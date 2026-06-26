import requests
import json
from refresh import get_access_token

def send_kakao(message):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    access_token = get_access_token()

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    data = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": message,
            "link": {
                "web_url": "https://finance.yahoo.com"
            }
        })
    }

    response = requests.post(url, headers=headers, data=data)

    print("상태코드:", response.status_code)
    print("응답:", response.text)