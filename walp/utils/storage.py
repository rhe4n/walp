from appdirs import user_data_dir
from . import parser
from pathlib import Path
import os
import json
import shutil

tree_structure = parser.parseKeyValue(Path(__file__).parent.parent.resolve() / "dirs.dat")
data_dir = user_data_dir(tree_structure["APP_NAME"], tree_structure["APP_AUTHOR"])

collections_dir_path = Path(data_dir) / tree_structure["COLLECTIONS_DIR"]
collections_file_path = Path(data_dir) / collections_dir_path / tree_structure["COLLECTIONS_FILE"]

presets_dir_path = Path(data_dir) / tree_structure["PRESETS_DIR"]
presets_file_path = Path(data_dir) / presets_dir_path / tree_structure["PRESETS_FILE"]

images_dir_path = Path(data_dir) / tree_structure["IMAGES_DIR"]

state_file_path = Path(data_dir) / tree_structure["STATE_FILE"]


def init():
    if not os.path.exists(collections_dir_path):
        os.makedirs(collections_dir_path)

    if not os.path.exists(presets_dir_path):
        os.makedirs(presets_dir_path)

    if not os.path.exists(images_dir_path):
        os.makedirs(images_dir_path)

    if not os.path.exists(state_file_path):
        from walp.utils import defaults
        print(json.dumps(defaults.initial_state()))
        with open(state_file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(defaults.initial_state()))

    if not os.path.exists(collections_file_path):
        # os.mknod(collections_data_path)
        emptylist = []
        with open(collections_file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(emptylist))

    if not os.path.exists(presets_file_path):
        # os.mknod(presets_data_path)
        emptylist = []
        with open(presets_file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(emptylist))


def loadJSONData(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def loadCollections():
    return loadJSONData(collections_file_path)


def loadState():
    return loadJSONData(state_file_path)


def loadPresets():
    return loadJSONData(presets_file_path)


def saveImage(sourcePath, newFileName):
    shutil.copy(sourcePath, images_dir_path / newFileName)


def saveCollections(collection_list):
    with open(collections_file_path, "w", encoding="utf-8") as file:
        file.write(json.dumps(collection_list))


def savePresets(preset_list):
    with open(presets_file_path, "w", encoding="utf-8") as file:
        file.write(json.dumps(preset_list))


def build_path_for_image(stashed_image_name):
    return images_dir_path / stashed_image_name
