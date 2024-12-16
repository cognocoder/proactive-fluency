
import tkinter as tk

from .window import Window

from .config import CONFIG
    
def root_layoutconfig(root: tk.Tk):
    root.title(CONFIG.window.title)
    root.geometry(CONFIG.window.size)
    root.config(padx=24, pady=4)
    root.config(bg=CONFIG.theme.bg)

def textarea_layoutconfig(textarea: tk.Text):
    textarea.config(padx=4, pady=4)
    textarea.config(spacing1=4, spacing2=4, spacing3=4)

    textarea.config(bg=CONFIG.theme.bg)
    textarea.config(fg=CONFIG.theme.fg)

    textarea.config(insertbackground=CONFIG.theme.fg)
    textarea.config(selectbackground=CONFIG.theme.fg)
    
    textarea.config(border=0)
    textarea.config(insertborderwidth=0)
    textarea.config(highlightthickness=0)
    textarea.config(selectborderwidth=0)
    
    textarea.config(insertwidth=2)
    textarea.config(insertofftime=500)
    textarea.config(insertontime=500)

    textarea.config(state=tk.NORMAL)
    textarea.config(wrap=tk.WORD)

    textarea.config(undo=True, maxundo=-1)
    textarea.config(autoseparators=True)

    textarea.focus_set()


def scrollbar_layoutconfig(scrollbar: tk.Scrollbar, textarea: tk.Text):
    scrollbar.config(cursor="hand2")
    
    scrollbar.config(bg=CONFIG.theme.bghover)
    scrollbar.config(activebackground=CONFIG.theme.bgactive)
    scrollbar.config(highlightbackground=CONFIG.theme.bghover)
    scrollbar.config(troughcolor=CONFIG.theme.bg)

    scrollbar.config(border=0)
    scrollbar.config(highlightthickness=0)
    scrollbar.config(borderwidth=0)
    scrollbar.config(elementborderwidth=0)

    textarea.config(yscrollcommand=scrollbar.set)


def controlsframe_layoutconfig(window: Window):
    
    window.controlsframe.config(bg=CONFIG.theme.bg)
    window.recordframe.config(bg=CONFIG.theme.bg)
    window.listenframe.config(bg=CONFIG.theme.bg)
    window.navframe.config(bg=CONFIG.theme.bg)
    window.sessionframe.config(bg=CONFIG.theme.bg)
    window.folderframe.config(bg=CONFIG.theme.bg)
    window.textframe.config(bg=CONFIG.theme.bg)
    window.langframe.config(bg=CONFIG.theme.bg)
    
    window.langstrvar.set(CONFIG.language.supported[0])
    
    window.langlabel.config(bg=CONFIG.theme.bg)
    window.langlabel.config(fg=CONFIG.theme.fg)
    window.langlabel.config(font=(CONFIG.window.font.mono, CONFIG.window.font.size))

    window.filelabel.config(bg=CONFIG.theme.bg)
    window.filelabel.config(fg=CONFIG.theme.fg)
    window.filelabel.config(font=(CONFIG.window.font.mono, CONFIG.window.font.size))
    window.filelabel.config(padx=4)


    window.helpframe.config(bg=CONFIG.theme.bg)

def statuslabel_layoutconfig(statuslabel: tk.Label):
    statuslabel.config(bg=CONFIG.theme.bg, fg=CONFIG.theme.fg)

def layoutconfig(window: Window):
    root_layoutconfig(window.root)
    
    textarea_layoutconfig(window.textarea)
    
    scrollbar_layoutconfig(window.scrollbar, window.textarea)
    
    controlsframe_layoutconfig(window)
    
    statuslabel_layoutconfig(window.statuslabel)