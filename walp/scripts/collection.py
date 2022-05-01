from walp.utils import storage


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


def delete_collection(name):
    collection_list = storage.loadCollections()

    amount = 0
    for i in range(len(collection_list)-1):
        if collection_list[i]["name"] == name:
            del collection_list[i]
            amount += 1

    if amount == 0:
        return 1
    elif amount > 1:
        return 2

    storage.saveCollections(collection_list)

    if amount == 1:
        return 0

