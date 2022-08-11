from pathlib import Path

from src.fs.builder import Node


def tree_writer(tree: list[Node]):
    for node in tree:
        path_object = Path(node.path)
        if node.is_directory:
            path_object.mkdir()
        else:
            path_object.touch()
