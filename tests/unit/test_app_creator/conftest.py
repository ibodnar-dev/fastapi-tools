from collections import namedtuple

import pytest

from src.app_creator.builder import Node

examples_result = namedtuple('examples_result', ['blueprint', 'tree'])


@pytest.fixture
def blueprint_and_tree_example_one() -> examples_result:
    blueprint = {
        'base': [
            'file_one',
            {
                'directory_one': [
                    'file_two'
                ]
            }
        ]
    }

    base_node = Node(name='base', parent=None, is_directory=True)
    file_one_node = Node(name='file_one', parent=base_node)
    directory_one_node = Node(name='directory_one', parent=base_node, is_directory=True)
    file_two_node = Node(name='file_two', parent=directory_one_node)

    tree = [
        base_node,
        file_one_node,
        directory_one_node,
        file_two_node
    ]

    return examples_result(blueprint=blueprint, tree=tree)


@pytest.fixture
def nodes_list() -> list[Node]:
    return [Node('directory', is_directory=True), Node('file', is_directory=False)]
