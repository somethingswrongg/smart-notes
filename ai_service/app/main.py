from fastapi import FastAPI
from app.schemas import SummaryRequest, SummaryResponse
from app.services import summarize_text
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Smart Notes AI Service")


@app.post("/summarize", response_model=SummaryResponse)
async def summarize(request: SummaryRequest):
    summary = await summarize_text(request.text)
    return SummaryResponse(summary=summary)
