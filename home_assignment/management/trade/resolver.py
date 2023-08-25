import strawberry

from ...deps import GenieInfo
from .database import query_trades
from re import search
@strawberry.type
class Trade:
    base: str
    quote: str
    fee_amount: str
    fee_currency: str
    transaction_time: str
    labels: list[str] 

async def get_trades(info: GenieInfo) -> list[Trade]:
    with info.context.session_factory.begin() as session:
        trades = query_trades(session)

        trade_list = []
        for trade in trades:
            trade_entry = Trade(
                base=trade.base.name,
                quote=trade.quote.name,
                fee_amount=trade.fee.amount,
                fee_currency=trade.fee.currency.name,
                transaction_time=trade.placed_at,
                labels=[label.value for label in trade.labels]
            )
            trade_list.append(trade_entry)

        return trade_list

@strawberry.type
class TradeResultSet:
    total_count: int
    trades: list[Trade]

async def get_trade_results(
    info: GenieInfo,
    base_asset_symbol: str = None,
    page: int = 1,
    page_size: int = 10
) -> TradeResultSet:
    with info.context.session_factory.begin() as session:
        trades = query_trades(session, base_asset_symbol)
        total_count = len(trades)

        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        paged_trades = trades[start_idx:end_idx]

        trade_list = []
        for trade in paged_trades:
            trade_entry = Trade(
                base=trade.base.name,
                quote=trade.quote.name,
                fee_amount=trade.fee.amount,
                fee_currency=trade.fee.currency.name,
                transaction_time=trade.placed_at,
                labels=[label.value for label in trade.labels]
            )
            if search(base_asset_symbol.lower(), trade.base.name.lower()):
                trade_list.append(trade_entry)

        return TradeResultSet(total_count=total_count, trades=trade_list)
