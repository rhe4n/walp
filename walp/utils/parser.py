
def parseKeyValue(param):
    toret = {}

    with open(param, "r") as file:
        for line in file:
            split = line.split("=")
            toret[split[0]] = split[1].split("\n")[0]

    return toret
