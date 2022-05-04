
def parseKeyValue(param):
    to_return = {}

    with open(param, "r") as file:
        for line in file:
            split = line.split("=")
            to_return[split[0]] = split[1].split("\n")[0]

    return to_return
