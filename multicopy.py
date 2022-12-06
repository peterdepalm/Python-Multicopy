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

def joinqueue():
    joiner = input('Enter joiner for copy list: ')
    joinedlist = joiner.join(list(deque(copies)))
    pc.copy(joinedlist)

copies = deque([])
pc.copy('')
keyboard.add_hotkey('ctrl + alt + e', lambda: os._exit(0))
keyboard.add_hotkey('ctrl + shift + v', lambda: depletecopyqueue())
keyboard.add_hotkey('ctrl + v', lambda: depletecopyqueue())
keyboard.add_hotkey('ctrl + alt + c', lambda: pc.copy(str(list(deque(copies)))))
keyboard.add_hotkey('ctrl + alt + j', lambda: joinqueue())

while True:
    print(copies)
    copies.append(pc.waitForNewPaste())
