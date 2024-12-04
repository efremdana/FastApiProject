from typing import (
    TYPE_CHECKING,
    Annotated,
)

from fastapi import Depends

from core.models import UserDB
from core.models.db_helper import db_helper

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_users_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.get_scoped_session),
    ],
):
    # TODO: изменить на User
    yield UserDB.get_db(session=session)