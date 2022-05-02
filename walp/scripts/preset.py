import collections

from walp.utils import storage
from walp.scripts import image as img
from walp.scripts import engine as engine


class Preset(object):
    def __init__(self, name):
        self.name = name
        self.assignation = {}


def list_preset_names():
    preset_list = storage.loadPresets()
    return list(map(lambda x: x["name"], preset_list))


def use_preset(name):
    preset = find_preset(name)
    pairs = preset["assignation"]

    ordered_pairs = collections.OrderedDict(sorted(pairs.items()))

    engine.set_monitor_background_pairs(ordered_pairs)
    return 0


def create_preset(name):
    preset_list = storage.loadPresets()
    new_preset = Preset(name)

    for pres in preset_list:
        if pres["name"] == name:
            return 1

    preset_list.append(new_preset.__dict__)
    storage.savePresets(preset_list)

    return 0


def delete_preset(name):
    preset_list = storage.loadPresets()

    amount = 0
    for i in range(len(preset_list)):
        if preset_list[i]["name"] == name:
            del preset_list[i]
            amount += 1

    if amount == 0:
        return 1
    elif amount > 1:
        return 2

    storage.savePresets(preset_list)

    if amount == 1:
        return 0


def set_image_monitor(preset_name, img_name, monitor_number):
    selected = None
    preset_list = storage.loadPresets()
    for i in range(len(preset_list)):
        if preset_list[i]["name"] == preset_name:
            selected = preset_list[i]

    if selected is None:
        return 1
    elif not img.is_stashed(img_name):
        return 2
    elif monitor_number < 0:
        return 3
    else:
        selected["assignation"][str(monitor_number)] = img_name
        storage.savePresets(preset_list)
        return 0


def find_preset(name):
    preset_list = storage.loadPresets()
    for i in range(len(preset_list)):
        if preset_list[i]["name"] == name:
            return preset_list[i]

