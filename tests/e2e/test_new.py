from typer.testing import CliRunner

from cli.main import app


runner = CliRunner()


def test_creates_file_tree_in_passed_path(testing_directory):
    app_name = 'users'

    result = runner.invoke(app, ['new', 'app', app_name, '--where', str(testing_directory)])

    assert result.exit_code == 0
    assert (testing_directory / app_name).exists()
