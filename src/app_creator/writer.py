from pathlib import Path

from src.app_creator.builder import Node
from src.app_creator.exceptions import NodeExistsError, BasePathDoesNotExist


def write_tree(tree: list[Node], base_path: str | None = None):
    for node in tree:
        path_object = _build_path(base_path=base_path, node_path=node.path)
        try:
            if node.is_directory:
                path_object.mkdir()
            else:
                path_object.touch()
        except FileExistsError as e:
            raise NodeExistsError(e)


def _build_path(base_path: str | None = None, *, node_path: str) -> Path:
    node_path_object = Path(node_path)

    if not base_path:
        return node_path_object

    base_path_object = Path(base_path)

    if not base_path_object.exists():
        raise BasePathDoesNotExist(message=f'directory {base_path} does not exist')

    return base_path_object / node_path_object
