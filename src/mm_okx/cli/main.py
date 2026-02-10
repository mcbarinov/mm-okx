from typing import Annotated

from click import get_current_context
from mm_clikit import TyperPlus
from typer import Option

from mm_okx.cli.commands import account_commands, public_commands
from mm_okx.logger import configure_debug_logging

app = TyperPlus(package_name="mm-okx", help="A command-line interface for OKX API.")


app.add_typer(public_commands.app, name="public", aliases=["p"])
app.add_typer(account_commands.app, name="account", aliases=["a"])


@app.callback()
def main(
    debug: Annotated[bool, Option("--debug", "-d", help="Debug mode")] = False,
) -> None:
    if debug:
        configure_debug_logging()

    ctx = get_current_context()
    ctx.obj = {"debug": debug}
