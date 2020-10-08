def parseBuffer(rawBuffer):
    messages = rawBuffer.split("\n")
    messages.pop() # remove the empty string from the split
    return [parseLine(msg) for msg in messages if msg != ""]

def parseLine(rawLine):
    nameSplit = rawLine.split("!", 1)
    messageSplit = rawLine.split(" :", 1)
    if len(nameSplit) == 2 and len(messageSplit) == 2:
        name = nameSplit[0][1:]
        message = messageSplit[1]
        returned = (name + ":", " " + message)
        return returned
    returned = ("", "")
    return returned
