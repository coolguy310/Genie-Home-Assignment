from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from ...db import AssetEntity


def query_assets(session: Session) -> Sequence[AssetEntity]:
    query = select(AssetEntity)

    results = session.execute(query)
    return results.scalars().fetchall()
