from src.app_creator.blueprints import app_blueprint, INIT


class TestAppBlueprint:
    def test_returns_dict(self):
        result = app_blueprint(app_name='app')

        assert isinstance(result, dict)

    def test_returns_passed_app_name(self):
        app_name = 'app'
        result = app_blueprint(app_name=app_name)

        assert app_name in result

    def test_returns_correct_app_structure(self):
        app_name = 'app'
        result = app_blueprint(app_name=app_name)
        app: list = result[app_name]
        domain: list = app[1]['domain']
        adapters: list = app[2]['adapters']
        services: list = domain[2]['services']

        assert INIT in app
        assert INIT in domain
        assert 'models.py' in domain
        assert INIT in adapters
        assert 'orm.py' in adapters
        assert 'repositories.py' in adapters
        assert 'schemas.py' in adapters
        assert INIT in services
