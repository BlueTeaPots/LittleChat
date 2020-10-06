class colors:
    NAME = "\033[92m"
    ENDC = "\033[0m"

def parseString(rawString):
    nameSplit = rawString.split("!", 1)
    messageSplit = rawString.split(" :", 1)
    if len(nameSplit) == 2 and len(messageSplit) == 2:
        name = colors.NAME + nameSplit[0][1:] + colors.ENDC
        message = messageSplit[1][:-1]
        return name + ": " + message
    return ""
