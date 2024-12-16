
import tkinter as tk
from tkinter import filedialog

from pathlib import Path

from .state import State, readto_textarea
from .window import Window

def delete(path: Path, statuslabel: tk.Label):
    try:
        path.unlink()
        statuslabel.config(text=f"File '{str(path)}' deleted.")
    except FileNotFoundError:
        statuslabel.config(text=f"File '{str(path)}' not found.")
    except Exception as e:
        statuslabel.config(text=f"Error deleting file '{str(path)}': {str(e)}")

def delete_goprev(path: Path, statuslabel: tk.Label, state: State, window: Window):
    delete(path, statuslabel)
    state.goprev(window, delete=True)
    
def save(path: Path, mode: str, data: any, statuslabel: tk.Label):
    with open(path, mode) as file:
        file.write(data)

    statuslabel.config(text=f"File '{str(path)}' saved.")

def save_gonext(path: Path, mode: str, data: any, statuslabel: tk.Label, state: State, window: Window):
    save(path, mode, data, statuslabel)
    state.gonext(window, create=True)

def folder_change(window: Window, state: State, path: Path = None):
    if not path:
        try:
            dirpath = Path(filedialog.askdirectory())
            if (dirpath):
                state.dir = dirpath
                with open("lastdir", "w") as file:
                    file.write(str(state.dir))
            else:
                window.statuslabel.config(text="Folder change cancelled.")
        except Exception as e:
            window.statuslabel.config(text=f"Error changing folder: {str(e)}")
    else:
        state.dir = path

    state.dir.mkdir(exist_ok=True, parents=True)
    window.statuslabel.config(text=f"Folder changed to '{str(state.dir)}'.")
    state.openlast(window)
    state.setenabled_navbuttons(window.buttons)
    readto_textarea(state.dir / f"{state.file.current}.txt", window.textarea, window.statuslabel)
    