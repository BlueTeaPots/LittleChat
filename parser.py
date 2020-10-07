class colors:
    NAME = "\033[92m"
    ENDC = "\033[0m"

def parseBuffer(rawBuffer):
    messages = rawBuffer.split("\n")
    messages.pop() # remove the empty string from the split
    for i in range(0, len(messages)):
        messages[i] = parseLine(messages[i])
    return messages

def parseLine(rawLine):
    nameSplit = rawLine.split("!", 1)
    messageSplit = rawLine.split(" :", 1)
    if len(nameSplit) == 2 and len(messageSplit) == 2:
        name = nameSplit[0][1:]
        message = messageSplit[1]
        return name + ": " + message
    return ""
