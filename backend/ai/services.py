import os
import httpx

INTERNAL_API_TOKEN = os.getenv("INTERNAL_API_TOKEN")

def summarize_text(text: str) -> str:
    if not INTERNAL_API_TOKEN:
        raise RuntimeError("INTERNAL_API_TOKEN is not set")

    response = httpx.post(
        "http://ai_service:8001/summarize",
        json={"text": text},
        headers={
            "X-Internal-Token": INTERNAL_API_TOKEN
        },
        timeout=10,
    )

    response.raise_for_status()
    return response.json()["summary"]
