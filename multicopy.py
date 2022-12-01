import pyperclip as pc
import time
import keyboard
from collections import deque
import os
#TODO: create a branch of this for testing out option to create list of copies as either a stack or a queue
#FIXME: this code currently cannot be used to paste into programs running as administrator. need to fix this.
#FIXME: infinite append loop bug (happens when there's a ton of background tasks running in pycharm)


def depletecopyqueue():
    time.sleep(.5) #might not need this but might be necessary
    try:
        copies.pop()
    except IndexError:
        return
    try:
        pc.copy(copies.pop())
    except IndexError:
        return


copies = deque([])
pc.copy('')
keyboard.add_hotkey('ctrl + alt + e', lambda: os._exit(0))
keyboard.add_hotkey('ctrl + shift + v', lambda: depletecopyqueue())
keyboard.add_hotkey('ctrl + v', lambda: depletecopyqueue())

while True:
    print(copies)
    copies.append(pc.waitForNewPaste())

#input() #don't know why but without this, the script rapidly opens, runs through the code and shuts down when not running it through a terminal
