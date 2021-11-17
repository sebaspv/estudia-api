from fastapi import APIRouter
from Questgen.main import QGen

router = APIRouter()
model = QGen()


@router.get("/english/{prompt}")
async def faq(prompt: str) -> dict:
    payload = {"input_text": prompt}
    output = model.predict_shortq(payload)
    return output
