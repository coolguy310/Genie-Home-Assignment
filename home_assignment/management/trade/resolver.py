import strawberry

from ...deps import GenieInfo
from .database import query_trades
from re import search
@strawberry.type
class LabelKeyValue:
    key: str
    value: str
@strawberry.type
class Fee:
    amount: str
    currency: str
@strawberry.type
class Trade:
    base: str
    quote: str
    fee: Fee
    transaction_time: str
    labels: list[LabelKeyValue] 

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

        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        paged_trades = trades[start_idx:end_idx]

        trade_list = []
        for trade in paged_trades:
            labels = [
                LabelKeyValue(key=label.key.name, value=label.value)
                for label in trade.labels
            ]
            trade_entry = Trade(
                base=trade.base.name,
                quote=trade.quote.name,
                fee = Fee(amount=trade.fee.amount, currency=trade.fee.currency.name),
                transaction_time=trade.placed_at,
                labels=labels
            )
            if search(base_asset_symbol.lower(), trade.base.name.lower()):
                trade_list.append(trade_entry)

        return TradeResultSet(total_count=len(trade_list), trades=trade_list)
