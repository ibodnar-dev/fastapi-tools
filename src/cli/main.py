from typer import Typer

import src.cli.new as new

app = Typer()

app.add_typer(new.app, name='new')


def run():
    app()
