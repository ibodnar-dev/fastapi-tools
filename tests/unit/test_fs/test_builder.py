from unittest.mock import Mock

import pytest

from src.fs.builder import Node


class TestNode:
    def test_instantiates_with_arguments(self):
        name = 'name'
        parent = Mock()
        is_directory = True

        node = Node(name=name, parent=parent, is_directory=is_directory)

        assert node.name == name
        assert node.parent == parent
        assert node.is_directory == is_directory

    @pytest.mark.parametrize('parent, is_root_result', [(Mock(spec=Node), False), (None, True)])
    def test_is_root_returns_correct_result(self, parent, is_root_result):
        node = Node(name='name', parent=parent)

        assert node.is_root == is_root_result
