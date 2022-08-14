from typing import Union


class Node:
    """
    A directory or file in the tree representation.
    """
    def __init__(self, name: str, parent: Union['Node', None] = None, is_directory: bool = False):
        self.name = name
        self.parent = parent
        self.is_directory = is_directory

    @property
    def is_root(self) -> bool:
        return not self.parent

    @property
    def path(self) -> str:
        """
        File path relative to the root directory.
        """
        is_root = self.is_root
        parent = '' if is_root else self.parent.path
        separator = '' if is_root else '/'
        return f'{parent}{separator}{self.name}'

    def __repr__(self) -> str:
        return self.path


_nodes: list[Node] = []
_current_parent: Node | None = None


def _build_tree(blueprint: dict) -> list[Node]:
    """
    Creates a Node from every dict inside the blueprint.

    :param blueprint: dict representation of the file tree
    to build.
    """
    global _current_parent

    for name, children in blueprint.items():
        current = Node(name=name, parent=_current_parent, is_directory=True)
        _nodes.append(current)
        _current_parent = current
        for child in children:
            if isinstance(child, dict):
                _build_tree(child)
            else:
                _nodes.append(Node(name=child, parent=_current_parent))

    return _nodes


def build_tree(blueprint: dict) -> list[Node]:
    return _build_tree(blueprint)
