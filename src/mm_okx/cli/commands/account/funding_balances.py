from pathlib import Path

from mm_std import fatal, print_json, print_table

from mm_okx.clients.account import AccountClient, AccountConfig


async def run(account: Path, ccy: str | None, debug: bool) -> None:
    client = AccountClient(AccountConfig.from_toml_file(account))
    res = await client.get_funding_balances(ccy)

    if debug:
        print_json(res)

    if res.is_err():
        fatal(res.unwrap_error())

    headers = ["ccy", "avail", "frozen"]

    rows = [[b.ccy, b.avail, b.frozen] for b in res.unwrap()]
    print_table("Funding Balances", headers, rows)
