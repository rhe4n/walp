from pathlib import Path
import PIL
from PIL import Image
from walp.utils import storage
import os


def importImage(rawpath):
    coolpath = Path(rawpath)
    if coolpath.is_dir():
        return handledir(coolpath)
    else:
        return handleimg(coolpath)


def handledir(path):
    files = os.listdir(path)
    retcode = 0
    for i in files:
        if handleimg(Path(i)) != 0:
            retcode = 1
    return retcode


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
