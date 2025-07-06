from sqlmodel import Session, create_engine

from src.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)


def init_db(session: Session) -> None:
    ...
