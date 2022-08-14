from unittest.mock import patch, MagicMock

import src.fs.writer as writer_module
from src.fs.builder import Node
from src.fs.writer import tree_writer


@patch.object(writer_module, 'Path')
class TestTreeWriter:
    def test_creates_path_object_from_path_attribute(self, path_mock: MagicMock, nodes_list: list[Node]):
        directory, file = nodes_list

        tree_writer(tree=nodes_list)

        path_mock.assert_any_call(directory.path)
        path_mock.assert_any_call(file.path)
        assert path_mock.call_count == 2
