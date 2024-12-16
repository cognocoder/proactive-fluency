
import tkinter as tk

from .state import State

def setbusy(state: State, busy: bool, buttons: dict, statuslabel: tk.Label):
    state.busy = busy

    for section in buttons:
        for label in buttons[section]:
            buttons[section][label].seticon(busy)
    
    if (not busy):
        state.setenabled_navbuttons(buttons)
