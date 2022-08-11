from unittest.mock import Mock

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
