from walp.utils import storage


def getState():
    return storage.loadState()


def setState(new_current, new_type):
    obj = {
        "current": new_current,
        "type": new_type
    }
    storage.saveState(obj)
