class colors:
    NAME = "\033[92m"
    ENDC = "\033[0m"

def parseString(rawString):
    name = colors.NAME + rawString.split("!", 1)[0][1:] + colors.ENDC
    messege = rawString.split(" :", 1)[1][:-1]
    return name + ": " + messege
