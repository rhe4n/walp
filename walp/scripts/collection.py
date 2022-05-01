from walp.utils import storage
import json


class Collection(object):
    def __init__(self, name):
        self.name = name
        self.images = []

    def addImage(self, image):
        self.images.append(image)


def list_collection_names():
    collection_list = storage.loadCollections()
    return list(map(lambda x: x["name"], collection_list))


def use_collection(name):
    pass


def create_collection(name):
    collection_list = storage.loadCollections()
    newCol = Collection(name)

    for col in collection_list:
        if col["name"] == name:
            return 1

    collection_list.append(newCol.__dict__)
    storage.saveCollections(collection_list)

    return 0

