from pathlib import Path

from mm_std import fatal, print_table

from mm_okx.clients.account import AccountClient, AccountConfig


async def run(account: Path, ccy: str | None = None) -> None:
    client = AccountClient(AccountConfig.from_toml_file(account))
    res = await client.get_currencies(ccy)
    if res.is_err():
        fatal(res.unwrap_error())

    headers = ["ccy", "chain", "can_dep", "can_wd", "max_fee", "min_fee", "max_wd", "min_wd"]
    rows = [
        [
            currency.ccy,
            currency.chain,
            currency.can_dep,
            currency.can_wd,
            currency.max_fee,
            currency.min_fee,
            currency.max_wd,
            currency.min_wd,
        ]
        for currency in res.unwrap()
    ]

    print_table(title="Currencies", columns=headers, rows=rows)
