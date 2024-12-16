
import tkinter as tk

from pathlib import Path

from .window import Window

def readto_str(path: Path, statuslabel: tk.Label):
    try:
        with open(path, "r") as file:
            return file.read()
    except FileNotFoundError:
        statuslabel.config(text=f"File '{str(path)}' not found.")
    except Exception as e:
        statuslabel.config(text=f"Error reading file '{str(path)}': {str(e)}")
    return None

def readto_textarea(path: Path, textarea: tk.Text, statuslabel: tk.Label):
    try:
        with open(path, "r") as file:
            data = file.read()
            textarea.delete("1.0", tk.END)
            textarea.insert(tk.END, data)
            statuslabel.config(text=f"File '{str(path)}' read.")
    except FileNotFoundError:
        statuslabel.config(text=f"File '{str(path)}' not found.")
    except Exception as e:
        statuslabel.config(text=f"Error reading file '{str(path)}': {str(e)}")

class FileState:
    first = 0
    current = 0
    last = 1
    
class FontState:
    name = 0
    size = 0

class LangState:
    name = 0

class State:
    busy = False
    
    dir = Path("out/example")
    file = FileState()

    font = FontState()
    lang = LangState()

    def openlast(self, window: Window):
        try:
            with open(self.dir / "last", "r") as file:
                self.file.last = int(file.read())
            self.file.current = self.file.last
            window.fileintvar.set(self.file.current)
        except FileNotFoundError:
            self.file.last = 1
            self.file.current = 0
            window.fileintvar.set(self.file.current)
        except Exception as e:
            window.statuslabel.config(text=f"Error opening file: '{str(e)}'.")

    def getname_byext(self, ext: str):
        return self.dir / f"{self.file.current}.{ext}"
    
    def setenabled_navbuttons(self, buttons: dict):
        buttons["nav"]["first"].seticon(not self.hasprev())
        buttons["nav"]["prev"].seticon(not self.hasprev())
        buttons["nav"]["next"].seticon(not self.hasnext())
        buttons["nav"]["last"].seticon(not self.hasnext())

    def hasnext(self):
        return self.file.current < self.file.last
    
    def hasprev(self):
        return self.file.current > self.file.first
    
    def gonext(self, window: Window, create: bool = False):
        if self.busy:
            return
        
        if self.hasnext():
            self.file.current += 1 if self.file.current < self.file.last else 0
            window.fileintvar.set(self.file.current)
            readto_textarea(self.getname_byext("txt"), window.textarea, window.statuslabel)
        elif create:
            self.file.last += 1
            self.gonext(window)
            with open(self.dir / "last", "w") as file:
                file.write(str(self.file.last))
        self.setenabled_navbuttons(window.buttons)
        
    
    def goprev(self, window: Window, delete: bool = False):
        if self.busy:
            return
        
        if delete:
            self.file.last -= 1 if self.file.last > 1 and self.file.current == self.file.last else 0
            with open(self.dir / "last", "w") as file:
                file.write(str(self.file.last))
        if self.hasprev():
            self.file.current -= 1 if self.file.current > 0 else 0
            window.fileintvar.set(self.file.current)
            readto_textarea(self.getname_byext("txt"), window.textarea, window.statuslabel)
        self.setenabled_navbuttons(window.buttons)
            
    
    def gofirst(self, window: Window):
        if self.busy:
            return
        
        if self.hasprev():
            self.file.current = self.file.first
            window.fileintvar.set(self.file.current)
            self.setenabled_navbuttons(window.buttons)
            readto_textarea(self.getname_byext("txt"), window.textarea, window.statuslabel)
    
    def golast(self, window: Window):
        if self.busy:
            return
        
        if self.hasnext():
            self.file.current = self.file.last
            window.fileintvar.set(self.file.current)
            self.setenabled_navbuttons(window.buttons)
            readto_textarea(self.getname_byext("txt"), window.textarea, window.statuslabel)
