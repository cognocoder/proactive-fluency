
import tkinter as tk

from PIL import ImageTk

from .config import CONFIG
from .icons import ICONS
from .window import Window
from .state import State

def buttons_gridconfig(window: Window, state: State):
        for section, section_cfg in BUTTONS.items():
            frame = window.getframe_bysection(section)
            window.buttons[section] = {}
            for label, button_builder in section_cfg.items():
                button = button_builder(frame, state)
                if button.enabled:
                    button.widget.grid(row=button.grid[0], column=button.grid[1], padx=8)
                    button.widget.config(cursor="hand2")
                    button.widget.config(bg=CONFIG.theme.bg)
                    button.widget.config(activebackground=CONFIG.theme.bghover)
                    button.widget.config(highlightbackground=CONFIG.theme.bg)
                    button.widget.config(border=0)
                    button.widget.config(highlightthickness=0)
                    window.buttons[section][label] = button

class Button:
    ready: ImageTk.PhotoImage
    busy: ImageTk.PhotoImage

    enabled: bool
    
    grid: tuple

    widget: tk.Button

    def __init__(self, frame, grid: tuple, state: State, ready: str, busy: str, enabled: bool = True):
        self.ready = ICONS[ready]
        self.busy = ICONS[busy]

        self.enabled = enabled
        
        self.grid = grid
                                                                              
        self.widget = tk.Button(frame, image=self.ready if not state.busy else self.busy, relief="flat")

    def geticon(self, busy: bool):
        return self.busy if busy else self.ready

    def seticon(self, busy: bool):
        self.widget.config(image=self.geticon(busy))

BUTTONS = {
    "user": {
        "microphone": lambda frame, state: Button(frame, (0,0), state, "microphone", "microphone-disabled"),
        "microphone-outline": lambda frame, state: Button(frame, (0,1), state, "microphone-outline", "microphone-outline-disabled"),
        "player-play-outline": lambda frame, state: Button(frame, (0,2), state, "player-play-outline", "player-play-outline-disabled"),
    },
    "bot": {
        "message-chatbot": lambda frame, state: Button(frame, (0,0), state, "message-chatbot", "message-chatbot-disabled"),
        "player-play": lambda frame, state: Button(frame, (0,1), state, "player-play", "player-play-disabled"),
    },
    "text": {
        "typography": lambda frame, state: Button(frame, (0,0), state, "typography", "typography"),
        "text-size": lambda frame, state: Button(frame, (0,1), state, "text-size", "text-size"),
    },
    "language": {
        "language": lambda frame, state: Button(frame, (0,0), state, "language", "language"),
    },
    "nav": {
        "first": lambda frame, state: Button(frame, (0,0), state, "square-rounded-chevrons-left", "square-rounded-chevrons-left-disabled"),
        "prev": lambda frame, state: Button(frame, (0,1), state, "square-rounded-chevron-left", "square-rounded-chevron-left-disabled"),
        "next": lambda frame, state: Button(frame, (0,3), state, "square-rounded-chevron-right", "square-rounded-chevron-right-disabled"),
        "last": lambda frame, state: Button(frame, (0,4), state, "square-rounded-chevrons-right", "square-rounded-chevrons-right-disabled"),
    },
    "session": {
        "save": lambda frame, state: Button(frame, (0,5), state, "square-rounded-check", "square-rounded-check-disabled"),
        "delete": lambda frame, state: Button(frame, (0,6), state, "square-rounded-x", "square-rounded-x-disabled"),
    },
    "folder": {
        "folder": lambda frame, state: Button(frame, (0,0), state, "folder", "folder-disabled"),
    },
    "help": {
        "busy": lambda frame, state: Button(frame, (0,0), state, "hourglass", "hourglass-busy", False),
        "help": lambda frame, state: Button(frame, (0,1), state, "help-square-rounded", "help-square-rounded", False),
    }
}
