from pathlib import Path

from src.fs.builder import Node
from src.fs.exceptions import NodeExistsError


def tree_writer(tree: list[Node]):
    for node in tree:
        path_object = Path(node.path)
        try:
            if node.is_directory:
                path_object.mkdir()
            else:
                path_object.touch()
        except FileExistsError as e:
            raise NodeExistsError(e)
