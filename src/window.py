import tkinter as tk

class Window:
    def __init__(self):
        self.root = tk.Tk()

        # TODO: add another text
        self.textarea = tk.Text(self.root)
        self.scrollbar = tk.Scrollbar(self.root, command=self.textarea.yview)

        self.controlsframe = tk.Frame(self.root)
        self.recordframe = tk.Frame(self.controlsframe)
        self.listenframe = tk.Frame(self.controlsframe)
        
        self.navframe = tk.Frame(self.controlsframe)
        self.fileintvar = tk.IntVar()
        self.fileintvar.set(0)
        self.filelabel = tk.Label(self.navframe, textvariable=str(self.fileintvar), justify=tk.CENTER, anchor=tk.W)
        
        self.sessionframe = tk.Frame(self.controlsframe)
        
        self.folderframe = tk.Frame(self.controlsframe)
        
        self.textframe = tk.Frame(self.controlsframe)
        
        self.langframe = tk.Frame(self.controlsframe)
        self.langstrvar = tk.StringVar()
        self.langlabel = tk.Label(self.langframe, textvariable=self.langstrvar, justify="left", anchor="w")
        
        self.helpframe = tk.Frame(self.controlsframe)

        self.statuslabel = tk.Label(self.root, text="Ready", justify="left", anchor="w")

        self.buttons = {}

    def getframe_bysection(self, section):
        if section == "user":
            return self.recordframe
        elif section == "bot":
            return self.listenframe
        elif section == "nav":
            return self.navframe
        elif section == "session":
            return self.sessionframe
        elif section == "folder":
            return self.folderframe
        elif section == "text":
            return self.textframe
        elif section == "language":
            return self.langframe
        elif section == "help":
            return self.helpframe
        else:
            return None

        # self.textseparator = tk.Frame(self.root, height=1, bg=CONFIG.theme.bghover)
        # self.textseparator.grid(row=2, column=0, columnspan=3, sticky=tk.EW)