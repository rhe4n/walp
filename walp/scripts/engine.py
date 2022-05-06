from walp.utils import storage
import subprocess


def set_monitor_background_pairs(pairs):
    command = ["feh", "--no-fehbg"]

    for i in list(pairs):
        imgPath = storage.build_path_for_image(pairs[i])
        command.append("--bg-fill")
        command.append(imgPath)

    result = subprocess.run(command, stdout=subprocess.DEVNULL).returncode
    if result == 0:
        return 0
    else:
        print(result)
        return 1

