from unittest.mock import patch, MagicMock, Mock

import src.fs.writer as writer_module
from src.fs.builder import Node
from src.fs.writer import write_tree


@patch.object(writer_module, 'Path')
class TestTreeWriter:
    def test_creates_path_object_from_path_attribute(self, path_mock: MagicMock, nodes_list: list[Node]):
        directory, file = nodes_list

        write_tree(tree=nodes_list)

        path_mock.assert_any_call(directory.path)
        path_mock.assert_any_call(file.path)
        assert path_mock.call_count == 2

    def test_calls_mkdir_if_directory_and_touch_if_file(self, path_mock: MagicMock, nodes_list: list[Node]):
        path_instance_mock = Mock()
        path_mock.return_value = path_instance_mock

        write_tree(tree=nodes_list)

        path_instance_mock.mkdir.assert_called_once()
        path_instance_mock.touch.assert_called_once()
        assert path_mock.call_count == 2


class TestBuildPath:
    pass
