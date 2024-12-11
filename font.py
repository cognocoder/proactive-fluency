
from tkinter import font

from window import ROOT

def change_font(selected_font, status_bar_label, text_area):
    font_names = ROOT["fonts"]["names"]
    font_sizes = ROOT["fonts"]["sizes"]

    name = font_names[selected_font["name"]]
    size = font_sizes[selected_font["size"]]

    status_bar_label.config(text=f"Font set to {name} [{size}]")
    new_font = font.Font(family=name, size=size, weight="normal")
    text_area.config(font=new_font)

def rotate_font_name(selected_font, status_bar_label, text_area):
    font_names = ROOT["fonts"]["names"]
    selected_font["name"] = selected_font["name"] + 1 if selected_font["name"] < len(font_names) - 1 else 0
    change_font(selected_font, status_bar_label, text_area)

def rotate_font_size(selected_font, status_bar_label, text_area):
    font_sizes = ROOT["fonts"]["sizes"]
    selected_font["size"] = selected_font["size"] + 1 if selected_font["size"] < len(font_sizes) - 1 else 0
    change_font(selected_font, status_bar_label, text_area)
