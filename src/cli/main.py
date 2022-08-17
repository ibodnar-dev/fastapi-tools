from typer import Typer

from src.fs import create_app

app = Typer()


@app.command()
def new(app_name: str):
    create_app(app_name)


@app.callback(invoke_without_command=True)
def _new():
    pass


def run():
    app()
