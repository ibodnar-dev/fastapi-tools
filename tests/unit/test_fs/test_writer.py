from pathlib import Path
from unittest.mock import patch, MagicMock, Mock

import pytest

import src.fs.writer as writer_module
from src.fs.builder import Node
from src.fs.exceptions import BasePathDoesNotExist
from src.fs.writer import write_tree, _build_path  # noqa


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
    base_path = 'base_path'
    node_path = 'node_path'

    def test_returns_concatenated_path_object_when_base_path_passed(self):
        expected = Path(self.base_path) / Path(self.node_path)
        Path.exists = Mock(return_value=True)

        result = _build_path(base_path=self.base_path, node_path=self.node_path)

        assert expected == result

    @pytest.mark.parametrize(['base_path'], [(None,), ('',)])
    def test_returns_node_path_object_when_base_path_is_none_or_empty_str(self, base_path):
        expected = Path(self.node_path)

        result = _build_path(base_path=base_path, node_path=self.node_path)

        assert expected == result

    def test_raises_when_base_path_does_not_exist(self):
        Path.exists = Mock(return_value=False)

        with pytest.raises(BasePathDoesNotExist) as exc_info:
            _build_path(base_path=self.base_path, node_path=self.node_path)

        assert self.base_path in str(exc_info.value)
