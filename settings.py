import tkinter as tk
from tkinter import ttk
from core.startup import startupManager
from core.loader import getConfig as g
from core.writer import writeConfig as w

startup = startupManager('EasyCopy')

class Settings(tk.Toplevel):
    def __init__(self, parent, defaultPage):
        super().__init__(parent)

        self.title('Settings')
        self.transient(parent)
        self.resizable(False, False)
        self.grab_set()
        self.focus()

        _w = int(self.winfo_screenwidth() * 0.3)
        _h = int(self.winfo_screenheight() * 0.7)
        PADDING = _w // 30
        w = self.winfo_width()
        h = self.winfo_height()
        px = parent.winfo_rootx()
        py = parent.winfo_rooty()
        pw = parent.winfo_width()
        ph = parent.winfo_height()
        x = px + (pw - w) // 2 - _w // 2
        y = py + (ph - h) // 2 - _h // 2
        self.geometry(f'{_w}x{_h}+{x}+{y}')

        style = ttk.Style()

        style.configure('OK.TButton', font=('Arial', 11))
        style.configure('TNotebook.Tab', background='#ffffff', foreground='black', padding=(PADDING // 5, PADDING // 5), font=('Arial', 11))
        style.map('TNotebook.Tab', background=[('selected', "#ec1eff")], foreground=[('selected', 'black')], focuscolor=[('selected', '')])
        style.configure('NB.TFrame', background='white')
        style.configure('TCheckbutton', background='white')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.notebookFrame = ttk.Frame(self)
        self.notebookFrame.grid(row=0, column=0, sticky='nsew', padx=PADDING // 2, pady=(PADDING // 5, PADDING * 3))

        self.notebook = ttk.Notebook(self.notebookFrame)
        self.notebook.pack(fill='both', expand=True)

        self.general = ttk.Frame(self.notebook, style='NB.TFrame')
        self.notebook.add(self.general, text='General')

        self.templates = ttk.Frame(self.notebook, style='NB.TFrame')
        self.notebook.add(self.templates, text='Templates' )

        self.notebook.select(defaultPage)

        self.buttonFrame = ttk.Frame(self)
        self.buttonFrame.grid(row=0, column=0, sticky='sew', pady=PADDING * 4 // 5)
        self.buttonFrame.columnconfigure(1, weight=1)

        self.okButton = ttk.Button(self.buttonFrame, text='OK', style='OK.TButton', command=self.ok)
        self.okButton.grid(row=0, column=1, ipady=PADDING // 5, sticky='e')

        self.cancelButton = ttk.Button(self.buttonFrame, text='Cancel', command=self.destroy, style='OK.TButton')
        self.cancelButton.grid(row=0, column=2, padx=(PADDING // 3, PADDING // 2), ipady=PADDING // 5, sticky='e')

        self.helpButton = ttk.Button(self.buttonFrame, text='Help', style='OK.TButton')
        self.helpButton.grid(row=0, column=0, padx=PADDING // 2, ipady=PADDING // 5, sticky='w')

        self.general.columnconfigure(0, weight=1)
        self.runFrameTitle = tk.Label(self.general, text='Run', bg='white')
        self.runFrameTitle.config(padx=PADDING // 5)
        self.runFrame = tk.LabelFrame(self.general, labelwidget=self.runFrameTitle, bg='white')
        self.runFrame.grid(row=0, column=0, padx=PADDING, pady=PADDING, sticky='ew')

        self.runOnStartupVar = tk.IntVar()
        self.runOnStartupVar.set(int(g('General', 'runOnStartup')))
        self.runOnStartup = ttk.Checkbutton(self.runFrame, text='Run on startup', variable=self.runOnStartupVar)
        self.runOnStartup.grid(row=0, column=0, padx=PADDING, pady=PADDING)

        self.runMinimizedVar = tk.IntVar()
        self.runMinimizedVar.set(int(g('General', 'runMinimized')))
        self.runMinimized = ttk.Checkbutton(self.runFrame, text='Run minimized', variable=self.runMinimizedVar)
        self.runMinimized.grid(row=0, column=1, padx=PADDING * 3, pady=PADDING)
    
    def ok(self):
        if self.runOnStartupVar.get():
            startup.enable()
            w('General', 'runOnStartup', 1)
        else:
            startup.disable()
            w('General', 'runOnStartup', 0)
        
        if self.runMinimizedVar.get():
            w('General', 'runMinimized', 1)
        else:
            w('General', 'runMinimized', 0)

        self.destroy()