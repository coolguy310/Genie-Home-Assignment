import strawberry

from .asset import get_assets
from .user import get_users
from .trade import get_trade_results


@strawberry.type
class Management:
    users = strawberry.field(resolver=get_users)
    assets = strawberry.field(resolver=get_assets)
    trade_results = strawberry.field(resolver=get_trade_results)


@strawberry.type
class Query:
    management: Management = strawberry.field(resolver=Management)
