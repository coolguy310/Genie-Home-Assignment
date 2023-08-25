import strawberry
from strawberry.fastapi import GraphQLRouter

from ..management.user.resolver import get_users
from .context import get_context


@strawberry.type
class Management:
    users = strawberry.field(resolver=get_users)


@strawberry.type
class Query:
    management: Management = strawberry.field(resolver=Management)


router = GraphQLRouter(
    strawberry.Schema(Query),
    graphiql=True,
    context_getter=get_context,
)
