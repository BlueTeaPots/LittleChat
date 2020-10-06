#!/bin/python3

from irc import IRC

irc = IRC()
irc.connect("blueteapots")
while True:
    text = irc.get_response()
    if text != "":
        print(text)
