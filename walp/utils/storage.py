from appdirs import user_data_dir
from . import parser
from pathlib import Path
import os
import json

tree_structure = parser.parseKeyValue(Path(__file__).parent.parent.resolve() / "dirs.dat")
data_dir = user_data_dir(tree_structure["APP_NAME"], tree_structure["APP_AUTHOR"])

collections_dir_path = Path(data_dir) / tree_structure["COLLECTIONS_DIR_NAME"]
collections_data_path = Path(data_dir) / collections_dir_path / tree_structure["COLLECTIONS_FILE_NAME"]

presets_dir_path = Path(data_dir) / tree_structure["PRESETS_DIR_NAME"]
presets_data_path = Path(data_dir) / presets_dir_path / tree_structure["PRESETS_FILE_NAME"]


def init():
    if not os.path.exists(collections_dir_path):
        os.makedirs(collections_dir_path)

    if not os.path.exists(presets_dir_path):
        os.makedirs(presets_dir_path)

    if not os.path.exists(collections_data_path):
        # os.mknod(collections_data_path)
        emptylist = []
        with open(collections_data_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(emptylist))

    if not os.path.exists(presets_data_path):
        # os.mknod(presets_data_path)
        emptylist = []
        with open(presets_data_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(emptylist))


def loadCollections():
    with open(collections_data_path, "r") as file:
        data = json.load(file)
    return data
