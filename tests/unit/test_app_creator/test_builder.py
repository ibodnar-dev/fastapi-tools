from unittest.mock import Mock

import pytest

from src.app_creator.builder import Node, build_tree


class TestNode:
    def test_instantiates_with_arguments(self):
        name = 'name'
        parent = Mock()
        is_directory = True

        node = Node(name=name, parent=parent, is_directory=is_directory)

        assert node.name == name
        assert node.parent == parent
        assert node.is_directory is is_directory

        node = Node(name=name, parent=parent)

        assert node.is_directory is False

    @pytest.mark.parametrize('parent, is_root_result', [(Mock(spec=Node), False), (None, True)])
    def test_is_root_returns_correct_result(self, parent, is_root_result):
        node = Node(name='name', parent=parent)

        assert node.is_root == is_root_result

    @pytest.mark.parametrize(
        'parent, name, path_result',
        [
            (Mock(spec=Node, name='parent', path='parent'), 'current', 'parent/current'),
            (None, 'current', 'current')
        ]
    )
    def test_path_returns_correct_result(self, parent, name, path_result):
        node = Node(name=name, parent=parent)

        assert node.path == path_result

    def test_repr_returns_path(self):
        current_name = 'current_name'
        parent_name = 'parent_name'

        node = Node(name=current_name, parent=Mock(spec=Node, path=parent_name))

        assert repr(node) == f'{parent_name}/{current_name}'


class TestBuildTree:
    def test_returns_correct_tree(self, blueprint_and_tree_example_one):
        blueprint = blueprint_and_tree_example_one.blueprint
        tree = blueprint_and_tree_example_one.tree

        result = build_tree(blueprint=blueprint)

        # All the resulting tuples from zip(tree, result) should have
        # len == 1 when converted into a set if its Node objects have the same path
        assert all([(len(set(pair)) == 1) for pair in zip(tree, result)])
