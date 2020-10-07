class colors:
    NAME = "\033[92m"
    ENDC = "\033[0m"

def parseBuffer(rawBuffer):
    messages = rawBuffer.split("\n")
    parsedBuffer = ""
    for message in messages:
        parsedBuffer += parseLine(message)
    return parsedBuffer

def parseLine(rawLine):
    nameSplit = rawLine.split("!", 1)
    messageSplit = rawLine.split(" :", 1)
    if len(nameSplit) == 2 and len(messageSplit) == 2:
        name = colors.NAME + nameSplit[0][1:] + colors.ENDC
        message = messageSplit[1]
        return name + ": " + message
    return ""
