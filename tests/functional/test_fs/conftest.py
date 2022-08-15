import pytest

from src.fs.builder import Node


@pytest.fixture
def simple_tree() -> list[Node]:
    base_node = Node(name='base', parent=None, is_directory=True)
    directory_one = Node(name='directory_one', parent=base_node, is_directory=True)

    return [base_node, directory_one]
