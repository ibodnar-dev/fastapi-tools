from pathlib import Path

import pytest

from src.fs.builder import Node
from src.fs.exceptions import NodeExistsError
from src.fs.writer import tree_writer


class TestWriter:
    def test_writes_tree(self, setup_path: Path, simple_tree: list[Node]):
        tmp_path = setup_path
        base, directory_one = simple_tree

        tree_writer(simple_tree)

        assert (tmp_path / base.name).exists()
        assert (tmp_path / base.name / directory_one.name).exists()

    def test_raises_when_directory_already_exists(self, setup_path: Path, simple_tree: list[Node]):
        base: Node
        directory_one: Node
        base, directory_one = simple_tree
        tmp_path = setup_path

        Path(tmp_path / base.name).mkdir()

        with pytest.raises(NodeExistsError) as exc_info:
            tree_writer(simple_tree)

        assert 'FileExistsError' in str(exc_info.value)
