
import tkinter as tk

def select_all(root: tk.Tk, text_area: tk.Text):
    input = root.focus_get()
    if not isinstance(input, (tk.Text)):
        text_area.focus_set()
        input = text_area

    if isinstance(input, tk.Text):
        input.tag_add("sel", "1.0", "end")
        input.mark_set("insert", "end")
        input.see("insert")
    
    return "break"