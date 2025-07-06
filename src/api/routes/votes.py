from typing import Any

from fastapi import APIRouter
from sqlmodel import select

from src.models import Vote
from src.api.deps import CurrentUser, SessionDep


router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=Vote)
async def get_all_votes(
    session: SessionDep, current_user: CurrentUser
) -> Any:
    """
    Возвращает все голоса для текущего пользователя.
    """
    query = select(Vote).filter_by(
        user_id=current_user,
    )
    votes = session.exec(query).all()

    return Vote(data=votes)

