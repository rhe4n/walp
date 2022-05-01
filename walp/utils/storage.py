from appdirs import user_data_dir
from . import parser
from pathlib import Path
import os
import json

tree_structure = parser.parseKeyValue(Path(__file__).parent.parent.resolve() / "dirs.dat")

DATA_DIR = user_data_dir(tree_structure["APP_NAME"], tree_structure["APP_AUTHOR"])
directories = [tree_structure["COLLECTIONS_DIR_NAME"], tree_structure["PRESETS_DIR_NAME"]]


def init():
    for i in directories:
        if not os.path.exists(DATA_DIR + "/" + i):
            os.makedirs(DATA_DIR + "/" + i)

    collections_dat_path = DATA_DIR + "/" + directories[0] + "/" + tree_structure["COLLECTIONS_FILE_NAME"]
    if not os.path.exists(collections_dat_path):
        os.mknod(collections_dat_path)

    presets_dat_path = DATA_DIR + "/" + directories[1] + "/" + tree_structure["PRESETS_FILE_NAME"]
    if not os.path.exists(presets_dat_path):
        os.mknod(presets_dat_path)


def loadCollections():
    with open(DATA_DIR + "/" + directories[0] + "/" + tree_structure["COLLECTIONS_FILE_NAME"], "r") as file:
        data = json.load(file)
    return data
