from tkinterdnd2 import TkinterDnD, DND_FILES
import ctypes
import tkinter as tk
from tkinter import ttk
import platform

ctypes.windll.shcore.SetProcessDpiAwareness(2)
scale = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
ONWIN = platform.system() == 'Windows'

class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        WIDTH = self.winfo_screenwidth()
        HEIGHT = self.winfo_screenheight()
        PADDING = WIDTH // 200
        BTNSZ = int(min(WIDTH, HEIGHT) * 0.2)

        self.title('EasyCopy Copier')
        self.tk.call('tk', 'scaling', scale * 1.3)
        self.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use('vista' if ONWIN else 'clam')
        self.style.configure('SRC.TButton', font=('Arial', 15))
        
        self.hFrame = ttk.Frame(self)
        self.hFrame.grid(row=0, column=1, padx=PADDING, pady=PADDING)

        self.header = ttk.Label(self.hFrame, text='EasyCopy Copier', font=('Arial', 25), anchor='center')
        self.header.pack()

        self.srcFrame = ttk.Frame(self, width=BTNSZ, height=BTNSZ)
        self.srcFrame.grid(row=1, column=0, padx=PADDING, pady=PADDING)
        self.srcFrame.pack_propagate(False)

        self.sourceButton = ttk.Button(self.srcFrame, text='Choose or drag in\n     source files', command=lambda: None, style = 'SRC.TButton')
        self.sourceButton.pack(fill='both', expand=True, anchor='center')

        self.arrowFrame = ttk.Frame(self)
        self.arrowFrame.grid(row=1, column=1, padx=PADDING, pady=PADDING)

        DWIDTH = BTNSZ * 1.3
        DHEIGHT = BTNSZ * 0.8
        self.arrow = tk.Canvas(self.arrowFrame, width=DWIDTH, height=DHEIGHT)
        
        self.arrow.pack()
        self.arrow.create_polygon(0, DHEIGHT // 4, DWIDTH // 2, DHEIGHT // 4, DWIDTH // 2, 0, DWIDTH, DHEIGHT // 2, DWIDTH // 2, DHEIGHT, DWIDTH // 2, DHEIGHT * 3 // 4, 0, DHEIGHT * 3 // 4, fill='green')

        self.dstFrame = ttk.Frame(self, width=BTNSZ, height=BTNSZ)
        self.dstFrame.grid(row=1, column=2, padx=PADDING, pady=PADDING)
        self.dstFrame.pack_propagate(False)

        self.distButton = ttk.Button(self.dstFrame, text='Choose or drag in\n destination folder', command=lambda: None, style='SRC.TButton')
        self.distButton.pack(fill='both', expand=True, anchor='center')

app = App()
app.mainloop()