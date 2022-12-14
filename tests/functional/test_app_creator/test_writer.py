from pathlib import Path

import pytest

from src.app_creator.builder import Node
from src.app_creator.exceptions import NodeExistsError
from src.app_creator.writer import write_tree


class TestWriter:
    def test_writes_tree(self, setup_path: Path, simple_tree: list[Node]):
        tmp_path = setup_path
        base, directory_one = simple_tree

        write_tree(simple_tree)

        assert (tmp_path / base.name).exists()
        assert (tmp_path / base.name / directory_one.name).exists()

    def test_raises_when_directory_already_exists(self, setup_path: Path, simple_tree: list[Node]):
        base: Node
        directory_one: Node
        base, directory_one = simple_tree
        tmp_path = setup_path

        Path(tmp_path / base.name).mkdir()

        with pytest.raises(NodeExistsError) as exc_info:
            write_tree(simple_tree)

        assert 'FileExistsError' in str(exc_info.value)
