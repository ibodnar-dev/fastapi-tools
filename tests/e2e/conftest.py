from pathlib import Path

import pytest


@pytest.fixture(scope='session')
def session_directory(tmp_path_factory) -> Path:
    """
    Returns a temporary session-scoped directory
    to share among all the tests in the session
    in order to test name collisions and such.
    """
    return tmp_path_factory.mktemp('session_directory')
