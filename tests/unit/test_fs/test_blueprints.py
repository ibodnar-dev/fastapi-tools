from src.fs.blueprints import app_blueprint


class TestAppBlueprint:
    def test_returns_dict(self):
        result = app_blueprint(app_name='app')

        assert isinstance(result, dict)

    def test_returns_passed_app_name(self):
        app_name = 'app'
        result = app_blueprint(app_name=app_name)

        assert app_name in result
