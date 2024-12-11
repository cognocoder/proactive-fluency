
import tkinter as tk

from icons import ICONS

BUTTONS = {
    "user": {
        "microphone-outline": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["microphone-outline"], relief="flat"),
            "grid": (0,0),
            "enabled": False,
        },
        "microphone": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["microphone"], relief="flat"),
            "grid": (0,1)
        },
        "stop": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["stop"], relief="flat"),
            "grid": (0,2),
            "enabled": False,
        },
        "player-play-outline": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["player-play-outline"], relief="flat"),
            "grid": (0,3)
        },
    },
    "bot": {
        "message-chatbot": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["message-chatbot"], relief="flat"),
            "grid": (0,0)
        },
        "player-play": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["player-play"], relief="flat"),
            "grid": (0,1)
        }
    },
    "text": {
        "typography": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["typography"], relief="flat"),
            "grid": (0,0)
        },
        "text-size": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["text-size"], relief="flat"),
            "grid": (0,1)
        },
    },
    "save": {
        "save": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["save"], relief="flat"),
            "grid": (0,0),
            "enabled": False,
        },
    },
    "language": {
        "language": {
            "widget": lambda frame : tk.Button(frame, image=ICONS["language"], relief="flat"),
            "grid": (0,0)
        },
    }
}
