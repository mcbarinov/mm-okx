import mm_clikit

from mm_okx.api.public import PublicClient


async def run(inst_id: str, inst_type: str, proxy: str | None) -> None:
    client = PublicClient(proxy=proxy)
    res = await client.get_instrument_raw(inst_id, inst_type)
    mm_clikit.print_json(res.value_or_error())
