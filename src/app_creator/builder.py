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

    def __eq__(self, other: 'Node') -> bool:
        return self.path == other.path

    def __ne__(self, other: 'Node') -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.path)


class _TreeBuilder:
    """
    The rationale for creating a callable type is that
    we must keep _nodes and _current_parent outside the scope
    of the callable, since it's recursive, and creating global
    variables provokes issues if this is a simple function because
    they remain with the same values when the function is run multiple times.
    This solution keeps the variables outside the callable's scope but in
    a local namespace.
    """
    def __init__(self):
        self._nodes: list[Node] = []
        self._current_parent: Node | None = None

    def __call__(self, blueprint: dict) -> list[Node]:
        """
        Recursive method that creates a Node from every dict
        in the blueprint.

        :param blueprint: dict representation of the file tree
        to build.
        """
        for name, children in blueprint.items():
            current = Node(name=name, parent=self._current_parent, is_directory=True)
            self._nodes.append(current)
            self._current_parent = current
            for child in children:
                if isinstance(child, dict):
                    self(child)
                else:
                    self._nodes.append(Node(name=child, parent=self._current_parent))

        return self._nodes


def build_tree(blueprint: dict) -> list[Node]:
    """
    Module's public interface.
    """
    tb = _TreeBuilder()
    return tb(blueprint)
