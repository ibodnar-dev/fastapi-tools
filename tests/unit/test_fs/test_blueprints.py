from src.fs.blueprints import app_blueprint


class TestAppBlueprint:
    def test_returns_dict(self):
        result = app_blueprint(app_name='app')

        assert isinstance(result, dict)
