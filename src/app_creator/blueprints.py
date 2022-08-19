INIT = '__init__.py'


def app_blueprint(app_name: str) -> dict:
    """
    Returns a dict suitable to act as a blueprint
    to create a fs tree for an app.
    """
    return {
        app_name: [
            INIT,
            {
                'domain': [
                    INIT,
                    'models.py',
                    {
                        'services': [
                            INIT,
                        ]
                    }
                ]
            },
            {
                'adapters': [
                    INIT,
                    'orm.py',
                    'repositories.py',
                    'schemas.py'
                ]
            }
        ]
    }
