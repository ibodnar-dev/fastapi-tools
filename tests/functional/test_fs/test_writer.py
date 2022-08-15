from pathlib import Path

from src.fs.builder import Node
from src.fs.writer import tree_writer


class TestWriter:
    def test_writes_tree(self, setup_path: Path, simple_tree: list[Node]):
        tmp_path = setup_path
        base, directory_one = simple_tree

        tree_writer(simple_tree)

        assert (tmp_path / base.name).exists()
        assert (tmp_path / base.name / directory_one.name).exists()
