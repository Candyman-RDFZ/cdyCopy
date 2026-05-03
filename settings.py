import tkinter as tk
from tkinter import ttk

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

        style.configure('OK.TButton', font=('Arial', 13))
        style.configure('TNotebook.Tab', background='#ffffff', foreground='black', padding=(PADDING // 5, PADDING // 5), font=('Arial', 12))
        style.map('TNotebook.Tab', background=[('selected', "#ec1eff")], foreground=[('selected', 'black')], focuscolor=[('selected', '')])
        style.configure('NB.TFrame', background='white')
        style.configure('TLabelframe', background='white', foreground='black')

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
        self.buttonFrame.grid(row=0, column=0, sticky='se', pady=PADDING * 4 // 5)

        self.okButton = ttk.Button(self.buttonFrame, text='OK', style='OK.TButton')
        self.okButton.grid(row=0, column=0, ipady=PADDING // 6)

        self.cancelButton = ttk.Button(self.buttonFrame, text='Cancel', command=self.destroy, style='OK.TButton')
        self.cancelButton.grid(row=0, column=1, padx=(PADDING // 3, PADDING // 2), ipady=PADDING // 6)

        self.runFrame = ttk.LabelFrame(self.general, text='Run')
        self.runFrame.grid(row=0, column=0)

        test = ttk.Label(self.runFrame, text='hello')
        test.pack(padx=10, pady=10)