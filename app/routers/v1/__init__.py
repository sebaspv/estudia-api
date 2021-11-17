from fastapi import APIRouter
from .faq import router as faq_router

router = APIRouter()

router.include_router(
    faq_router,
    prefix="/faq",
    tags=["faq"],
)
