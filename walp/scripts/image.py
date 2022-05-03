from pathlib import Path
import PIL
from PIL import Image
from walp.utils import storage
import os


def importImage(raw_path):
    cool_path = Path(raw_path)
    if cool_path.is_dir():
        return 1
    else:
        return handle_image(cool_path)


def handle_image(path):
    if check_is_image(path):
        storage.saveImage(path, os.path.basename(path))
        return 0
    else:
        return 1


def check_is_image(path):
    try:
        im = Image.open(path).copy()
        im.verify()
        return True
    except PIL.UnidentifiedImageError:
        return False


def is_stashed(name):
    """checks if this image is loaded in the stash"""
    directory = Path(storage.images_dir_path)
    for i in os.listdir(directory):
        if i == name:
            return True
    return False
