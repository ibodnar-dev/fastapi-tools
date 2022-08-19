from unittest.mock import patch, MagicMock, Mock

import src.fs.main as main_module
from src.fs.main import create_app


class TestCreateApp:
    app_name = 'app_name'
    base_path = 'base_path'

    @patch.object(main_module, 'write_tree')
    @patch.object(main_module, 'build_tree')
    @patch.object(main_module, 'app_blueprint')
    def test_calls_functions_with_correct_arguments(
            self,
            app_blueprint_mock: MagicMock,
            build_tree_mock: MagicMock,
            write_tree_mock: MagicMock
    ):
        app_blueprint_result = Mock()
        build_tree_result = Mock()
        app_blueprint_mock.return_value = app_blueprint_result
        build_tree_mock.return_value = build_tree_result

        create_app(app_name=self.app_name, base_path=self.base_path)

        app_blueprint_mock.assert_called_once_with(app_name=self.app_name)
        build_tree_mock.assert_called_once_with(blueprint=app_blueprint_result)
        write_tree_mock.assert_called_once_with(tree=build_tree_result, base_path=self.base_path)
