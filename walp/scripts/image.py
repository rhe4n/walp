from pathlib import Path
import PIL
from PIL import Image
from walp.utils import storage
import os


def importImage(rawpath):
    coolpath = Path(rawpath)
    if coolpath.is_dir():
        return 1
    else:
        return handleimg(coolpath)


def handleimg(path):
    if checkisimage(path):
        storage.saveImage(path, os.path.basename(path))
        return 0
    else:
        return 1


def checkisimage(path):
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
