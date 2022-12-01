import pyperclip as pc
import time
import keyboard
from collections import deque
import os
#FIXME: this code currently cannot be used to paste into programs running as administrator. need to fix this.
#FIXME: infinite append loop bug (heppens when there's a ton of background tasks running in pycharm)


def depletecopyqueue():
    time.sleep(.5) #might not need this but might be necessary
    copies.pop()
    try:
        pc.copy(copies.pop())
    except IndexError:
        os._exit(0)


copies = deque([])
pc.copy('')
keyboard.add_hotkey('ctrl + shift + v', lambda: depletecopyqueue())
keyboard.add_hotkey('ctrl + v', lambda: depletecopyqueue())

while True:
    try:
        print(copies)
        copies.append(pc.waitForNewPaste())
    except

#input() #don't know why but without this, the script rapidly opens, runs through the code and shuts down when not running it through a terminal
