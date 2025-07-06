from fastapi import APIRouter

from src.api.routes import votes

api_router = APIRouter()
api_router.include_router(votes.router)

