import os
from pathlib import Path

import pytest

from src.app_creator.builder import Node


@pytest.fixture
def setup_path(tmp_path: Path) -> Path:
    os.chdir(tmp_path)
    yield tmp_path


@pytest.fixture
def simple_tree() -> list[Node]:
    base_node = Node(name='base', parent=None, is_directory=True)
    directory_one = Node(name='directory_one', parent=base_node, is_directory=True)

    return [base_node, directory_one]
