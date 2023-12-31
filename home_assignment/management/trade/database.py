from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from ...db import TradeEntity


def query_trades(session: Session, symbol=None) -> Sequence[TradeEntity]:
    query = select(TradeEntity)

    results = session.execute(query)
    return results.scalars().fetchall()
