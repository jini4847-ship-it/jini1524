import requests
import json
from config import ACCESS_TOKEN

def send_kakao(message):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
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