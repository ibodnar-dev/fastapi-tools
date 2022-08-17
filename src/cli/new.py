from typer import Typer

from src.fs import create_app

app = Typer()


@app.command('app')
def _create_app(app_name: str):
    create_app(app_name)
