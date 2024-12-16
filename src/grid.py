
import tkinter as tk

from .window import Window

def root_gridconfig(window: Window):
    window.root.grid_rowconfigure(0, weight=0)
    window.root.grid_rowconfigure(1, weight=0)
    window.root.grid_rowconfigure(2, weight=1)
    window.root.grid_rowconfigure(6, weight=0)

    window.root.grid_columnconfigure(0, weight=0)
    window.root.grid_columnconfigure(1, weight=1)
    window.root.grid_columnconfigure(2, weight=1)
    window.root.grid_columnconfigure(3, weight=0)
    window.root.grid_columnconfigure(4, weight=0)

    window.controlsframe.grid(row=1, column=1, columnspan=3, pady=24, sticky=tk.EW)
    window.textarea.grid(row=2, column=1, columnspan=2, pady=4, sticky=tk.NSEW)
    window.scrollbar.grid(row=2, column=3, sticky=tk.NS)
    window.statuslabel.grid(row=6, column=0, columnspan=4, sticky=tk.EW, padx=2, pady=2)

def controlsframe_gridconfig(window):
    window.controlsframe.grid_columnconfigure(0, weight=1)
    window.controlsframe.grid_columnconfigure(9, weight=1)

    window.recordframe.grid(row=0, column=1, sticky=tk.EW, padx=24)
    window.listenframe.grid(row=0, column=2, sticky=tk.EW, padx=24)
    window.navframe.grid(row=0, column=3, sticky=tk.EW, padx=24)
    window.sessionframe.grid(row=0, column=4, sticky=tk.EW, padx=24)
    window.filelabel.grid(row=0, column=2, sticky=tk.EW, padx=4, pady=2) # sessionframe
    window.folderframe.grid(row=0, column=5, sticky=tk.EW, padx=24)
    window.textframe.grid(row=0, column=6, sticky=tk.EW, padx=24)
    window.langframe.grid(row=0, column=7, sticky=tk.EW, padx=24)
    window.langlabel.grid(row=0, column=1, sticky=tk.W, padx=4, pady=2) # langframe

    window.helpframe.grid(row=0, column=8, sticky=tk.EW, padx=24)

def gridconfig(window: Window):
    root_gridconfig(window)
    controlsframe_gridconfig(window)