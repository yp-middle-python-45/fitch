from typing import Optional

from sqlmodel import Field, SQLModel


class Vote(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    value: int
    user_id: str
    object_id: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None
