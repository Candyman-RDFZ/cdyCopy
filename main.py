from tkinterdnd2 import TkinterDnD, DND_FILES
import tkinter
from tkinter import ttk

class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title('Copier')
        
        self.hFrame = ttk.Frame(self)
        

app = App()
app.mainloop()