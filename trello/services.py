from sqlalchemy.ext.asyncio import AsyncSession

from app import BoardInSchema
from trello.models import Board


async def create_board(session: AsyncSession, board: BoardInSchema) -> Board:
    new_board = Board(name=board.name, description=board.description)
    session.add(new_board)
    return new_board
