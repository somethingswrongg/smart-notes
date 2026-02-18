import dotenv
import httpx
import os

from dotenv import load_dotenv

load_dotenv()

YANDEX_API_KEY = os.getenv("YANDEX_API_KEY")
YANDEX_FOLDER_ID = os.getenv("YANDEX_FOLDER_ID")

url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

headers = {
    "Authorization": f"Api-Key {YANDEX_API_KEY}",
    "Content-Type": "application/json",
}

payload = {
    "modelUri": f"gpt://{YANDEX_FOLDER_ID}/yandexgpt/latest",
    "completionOptions": {
        "stream": False,
        "temperature": 0.3,
        "maxTokens": 50,
    },
    "messages": [
        {"role": "user", "text": "Привет, напиши короткий ответ."}
    ],
}

response = httpx.post(url, headers=headers, json=payload)
print("FOLDER:", YANDEX_FOLDER_ID)

print(response.status_code)
print(response.text)
