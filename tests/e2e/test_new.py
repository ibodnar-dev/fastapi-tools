import os

from typer.testing import CliRunner

from cli.main import app


runner = CliRunner()


def test_creates_file_tree_in_passed_path(session_directory):
    app_name = 'users'

    result = runner.invoke(app, ['new', 'app', app_name, '--where', str(session_directory)])

    assert result.exit_code == 0
    assert (session_directory / app_name).exists()


def test_creates_file_tree_in_cwd_if_no_path_passed(tmp_path):
    os.chdir(tmp_path)
    app_name = 'users'

    result = runner.invoke(app, ['new', 'app', app_name])

    assert result.exit_code == 0
    assert (tmp_path / app_name).exists()
