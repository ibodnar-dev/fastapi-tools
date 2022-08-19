from typer import Typer

from src.app_creator import create_app

app = Typer()


@app.command('app')
def _create_app(app_name: str, where: str | None = None):
    create_app(app_name, base_path=where)
