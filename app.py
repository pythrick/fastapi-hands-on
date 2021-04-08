import asyncio
from typing import Optional

import uvicorn
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from trello import services
from trello.db.base import get_session, init_models

app = FastAPI()


@app.get("/")
def index():
    return {"hello": "world"}


class BoardSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class BoardInSchema(BaseModel):
    name: str
    description: Optional[str] = None


@app.get("/boards", response_model=list[BoardSchema])
async def list_boards():
    return [BoardSchema(id=1, name="Primeiro board", description="Descrição")]


@app.post("/board", response_model=BoardSchema)
async def create_board(
    board: BoardInSchema, session: AsyncSession = Depends(get_session)
):
    new_board = await services.create_board(session, board)
    await session.commit()
    return BoardSchema.from_orm(new_board)


if __name__ == "__main__":
    asyncio.run(init_models())
    uvicorn.run("app:app", reload=True)
