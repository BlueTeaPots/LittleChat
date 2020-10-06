#!/bin/python3

from irc import IRC
from parser import *

irc = IRC()
irc.connect("bajo")
while True:
    text = irc.get_response()
    if text != "":
        print(parseString(text))
