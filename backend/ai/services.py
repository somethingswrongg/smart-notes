import httpx

AI_SERVICE_URL = "http://127.0.0.1:8001"


def summarize_text(text: str):
    response = httpx.post(
        f"{AI_SERVICE_URL}/summarize",
        json={"text": text},
        timeout=30.0
    )

    response.raise_for_status()
    return response.json()
