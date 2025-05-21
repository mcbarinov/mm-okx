from pathlib import Path

from mm_std import fatal, print_table

from mm_okx.clients.account import AccountClient, AccountConfig


async def run(account: Path, ccy: str) -> None:
    client = AccountClient(AccountConfig.from_toml_file(account))
    res = await client.get_deposit_address(ccy)
    if res.is_err():
        fatal(res.unwrap_error())

    headers = ["ccy", "chain", "address"]

    rows = [[a.ccy, a.chain, a.addr] for a in res.unwrap()]

    print_table(title="Deposit Address", columns=headers, rows=rows)
