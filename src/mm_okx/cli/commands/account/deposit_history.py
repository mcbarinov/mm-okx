from datetime import UTC, datetime
from pathlib import Path

from mm_std import fatal, print_json, print_table

from mm_okx.clients.account import AccountClient, AccountConfig


async def run(account: Path, ccy: str | None, debug: bool) -> None:
    client = AccountClient(AccountConfig.from_toml_file(account))
    res = await client.get_deposit_history(ccy)
    if debug:
        print_json(res)
        return

    if res.is_err():
        fatal(res.unwrap_error())

    headers = ["dep_id", "ccy", "chain", "to", "amt", "ts", "tx_id", "state", "blk_confirm"]
    rows = [
        [
            a.dep_id,
            a.ccy,
            a.chain,
            a.to,
            a.amt,
            datetime.fromtimestamp(a.ts / 1000, tz=UTC).strftime("%Y-%m-%d %H:%M:%S"),
            a.tx_id,
            a.state,
            a.actual_dep_blk_confirm,
        ]
        for a in res.unwrap()
    ]
    print_table("Deposit History", headers, rows)
