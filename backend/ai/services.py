import os

import httpx

AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "http://ai_service:8001")


def summarize_text(text: str):
    response = httpx.post(
        f"{AI_SERVICE_URL}/summarize",
        json={"text": text},
        timeout=30.0
    )

    response.raise_for_status()
    return response.json()
