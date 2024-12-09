
import tkinter as tk

from icons import ICONS

BUTTONS = {
    "record": {
        "play": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["play"], relief="flat"),
            "grid": (0,1)
        },
        "record": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["record"], relief="flat"),
            "grid": (0,0)
        },
        "save": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["save"], relief="flat"),
            "grid": (0,2)
        },
    },
    "listen": {
        "record": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["record"], relief="flat"),
            "grid": (0,0)
        },
        "play": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["play"], relief="flat"),
            "grid": (0,1)
        },
        "save": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["save"], relief="flat"),
            "grid": (0,2)
        }
    },
    "text": {
        "save": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["save"], relief="flat"),
            "grid": (0,0)
        },

    }
}
