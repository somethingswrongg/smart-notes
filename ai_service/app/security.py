import os
from fastapi import Header, HTTPException

INTERNAL_API_TOKEN = os.getenv("INTERNAL_API_TOKEN")

def verify_internal_token(x_internal_token: str = Header(...)):
    if x_internal_token != INTERNAL_API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid internal token")
