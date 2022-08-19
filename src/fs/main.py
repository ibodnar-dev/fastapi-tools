from src.fs.blueprints import app_blueprint
from src.fs.builder import build_tree
from src.fs.writer import write_tree


def create_app(app_name: str, base_path: str | None = None) -> None:
    blueprint = app_blueprint(app_name=app_name)
    tree = build_tree(blueprint=blueprint)
    write_tree(tree=tree, base_path=base_path)
