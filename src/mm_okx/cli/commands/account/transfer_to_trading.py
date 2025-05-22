from decimal import Decimal
from pathlib import Path

from mm_std import fatal, print_json, print_table

from mm_okx.clients.account import AccountClient, AccountConfig


async def run(account: Path, ccy: str, amt: Decimal, debug: bool) -> None:
    client = AccountClient(AccountConfig.from_toml_file(account))
    res = await client.transfer_to_trading(ccy, amt)
    if debug:
        print_json(res)
        return

    if res.is_err():
        fatal(res.unwrap_error())

    headers = ["trans_id", "ccy", "client_id", "from", "amt", "to"]
    rows = [[t.trans_id, t.ccy, t.client_id, t.from_, t.amt, t.to] for t in res.unwrap()]
    print_table("Transfer to Trading", headers, rows)
