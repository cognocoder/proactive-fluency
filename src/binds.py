
import tkinter as tk

from .text import select_all

def keybindsconfig(root: tk.Tk, **kwargs):
    if 'text_area' in kwargs:
        root.bind("<Control-a>", lambda event: select_all(root, kwargs['text_area']))