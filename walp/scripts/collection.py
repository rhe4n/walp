from walp.utils import storage


def list_collections():
    collection_list = storage.loadCollections()
    return list(map(lambda x: x["name"], collection_list))


def use_collection(name):
    pass


def set_value_collection(collection_name, key_name, value):
    pass
