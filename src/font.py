
from tkinter import font

from .state import FontState

from .config import CONFIG

def fontconfig(state: FontState, status_bar_label, text_area):
    font_names = CONFIG.fonts.names
    font_sizes = CONFIG.fonts.sizes

    name = font_names[state.name]
    size = font_sizes[state.size]

    status_bar_label.config(text=f"Font set to '{name}, {size}'")
    new_font = font.Font(family=name, size=size, weight="normal")
    text_area.config(font=new_font)

def font_rotatename(state: FontState, status_bar_label, text_area):
    font_names = CONFIG.fonts.names
    state.name = state.name + 1 if state.name < len(font_names) - 1 else 0
    fontconfig(state, status_bar_label, text_area)

def font_rotatesize(state: FontState, status_bar_label, text_area):
    font_sizes = CONFIG.fonts.sizes
    state.size = state.size + 1 if state.size < len(font_sizes) - 1 else 0
    fontconfig(state, status_bar_label, text_area)
