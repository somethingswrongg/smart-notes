from fastapi import FastAPI, Depends
from app.schemas import SummaryRequest, SummaryResponse
from app.security import verify_internal_token
from app.services import summarize_text, AIProviderError

app = FastAPI(title="AI Service")


@app.post("/summarize", response_model=SummaryResponse)
async def summarize(
    request: SummaryRequest,
    _: None = Depends(verify_internal_token),
):
    try:
        summary = await summarize_text(request.text)
        return SummaryResponse(summary=summary)

    except AIProviderError:
        return SummaryResponse(
            summary="Сервис временно недоступен. Попробуйте позже."
        )


@app.get("/health")
async def health():
    return {"status": "ok"}
