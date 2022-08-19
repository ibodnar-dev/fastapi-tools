from src.app_creator.blueprints import app_blueprint
from src.app_creator.builder import build_tree
from src.app_creator.writer import write_tree


def create_app(app_name: str, base_path: str | None = None) -> None:
    blueprint = app_blueprint(app_name=app_name)
    tree = build_tree(blueprint=blueprint)
    write_tree(tree=tree, base_path=base_path)
