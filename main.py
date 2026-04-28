from tkinterdnd2 import TkinterDnD, DND_FILES
import ctypes
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import platform, shutil
from pathlib import Path, PureWindowsPath
from settings import Settings

ONWIN = platform.system() == 'Windows'
if ONWIN:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    scale = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100


def change_path(path):
    if ONWIN:
        return str(PureWindowsPath(path))
    else:
        return str(Path(path).as_posix())

class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        WIDTH = self.winfo_screenwidth()
        HEIGHT = self.winfo_screenheight()
        PADDING = WIDTH // 200
        BTNSZ = int(min(WIDTH, HEIGHT) * 0.2)

        self.title('EasyCopy Copier')
        if ONWIN:   
            self.tk.call('tk', 'scaling', scale * 1.3)
        self.resizable(False, False)
        self.attributes('-topmost', True)
        self.photo = tk.PhotoImage(file='./assets/icon.png')
        self.iconphoto(True, self.photo)

        self.srcFiless = ''
        self.destDirss = ''

        self.style = ttk.Style()
        self.style.theme_use('vista' if ONWIN else 'clam')
        self.style.configure('SRC.TButton', font=('Arial', 15))
        self.style.configure('SRC.TCheckbutton', font=('Arial', 12))
        self.style.configure('SRC.TRadiobutton', font=('Arial', 15))
        
        self.hFrame = ttk.Frame(self)
        self.hFrame.grid(row=0, column=1, padx=PADDING, pady=PADDING)

        self.header = ttk.Label(self.hFrame, text='EasyCopy Copier', font=('Arial', 25), anchor='center')
        self.header.pack()

        self.srcFrame = ttk.Frame(self, width=BTNSZ, height=BTNSZ)
        self.srcFrame.grid(row=1, column=0, padx=PADDING, pady=PADDING, sticky='e')
        self.srcFrame.pack_propagate(False)

        self.srcFrame.drop_target_register(DND_FILES)
        self.srcFrame.dnd_bind('<<Drop>>', self.drop_src)

        self.sourceButton = ttk.Button(self.srcFrame, text='Choose or drag in\n     source files', command=self.chooseSrc, style='SRC.TButton')
        self.sourceButton.pack(fill='both', expand=True, anchor='center')

        self.arrowFrame = ttk.Frame(self)
        self.arrowFrame.grid(row=1, column=1, padx=PADDING, pady=PADDING)

        DWIDTH = BTNSZ * 1.3
        DHEIGHT = BTNSZ * 0.8
        self.arrow = tk.Canvas(self.arrowFrame, width=DWIDTH, height=DHEIGHT)
        
        self.arrow.pack()
        self.arrow.create_polygon(0, DHEIGHT // 4, DWIDTH // 2, DHEIGHT // 4, DWIDTH // 2, 0, DWIDTH, DHEIGHT // 2, DWIDTH // 2, DHEIGHT, DWIDTH // 2, DHEIGHT * 3 // 4, 0, DHEIGHT * 3 // 4, fill='green')

        self.destFrame = ttk.Frame(self, width=BTNSZ, height=BTNSZ)
        self.destFrame.grid(row=1, column=2, padx=PADDING, pady=PADDING, sticky='w')
        self.destFrame.pack_propagate(False)

        self.destFrame.drop_target_register(DND_FILES)
        self.destFrame.dnd_bind('<<Drop>>', self.drop_dest)

        self.destButton = ttk.Button(self.destFrame, text='Choose or drag in\n destination folder', command=self.chooseDest, style='SRC.TButton')
        self.destButton.pack(fill='both', expand=True, anchor='center')

        self.srcFileFrame = ttk.Frame(self)
        self.srcFileFrame.grid(row=2, column=0, sticky='w', padx=PADDING * 2, pady=PADDING * 2)

        self.srcFileFrame.drop_target_register(DND_FILES)
        self.srcFileFrame.dnd_bind('<<Drop>>', self.drop_src)
        
        self.sbar = tk.Scrollbar(self.srcFileFrame)
        self.sbar.grid(row=1, column=1, sticky='wns')

        self.hbar = tk.Scrollbar(self.srcFileFrame, orient='horizontal')
        self.hbar.grid(row=2, column=0, sticky='ew')

        self.srcFileTitle = ttk.Label(self.srcFileFrame, text='Chosen Files:', font=('Arial', 15))
        self.srcFileTitle.grid(row=0, column=0, sticky='w')

        self.shrinkVar = tk.IntVar()
        self.shrinkVar.set(1)
        self.shrinkPath = ttk.Checkbutton(self.srcFileFrame, text='Shorten paths', variable=self.shrinkVar, command=self.toggle_shrink, style='SRC.TCheckbutton')
        self.shrinkPath.grid(row=0, column=0, sticky='e')

        self.srcFiles = tk.Text(self.srcFileFrame, width=30, height=10, font=('Consolas', 13), wrap='none', xscrollcommand=self.hbar.set, yscrollcommand=self.sbar.set, state='disabled')
        self.srcFiles.grid(row=1, column=0)

        self.sbar.config(command=self.srcFiles.yview)
        self.hbar.config(command=self.srcFiles.xview)

        self.methodFrame = ttk.Frame(self)
        self.methodFrame.grid(row=2, column=1, sticky='n', padx=PADDING, pady=PADDING)

        self.method = ttk.Label(self.methodFrame, text='Method: ', font=('Arial', 15))
        self.method.grid(row=0, column=0)

        self.methodVar = tk.IntVar()
        self.methodVar.set(0)

        self.copyButton = ttk.Radiobutton(self.methodFrame, text='Copy', variable=self.methodVar, value=0, style='SRC.TRadiobutton')
        self.copyButton.grid(row=0, column=1, padx=PADDING)
        self.cutButton = ttk.Radiobutton(self.methodFrame, text='Cut', variable=self.methodVar, value=1, style='SRC.TRadiobutton')
        self.cutButton.grid(row=0, column=2, padx=PADDING)

        self.destDirFrame = ttk.Frame(self)
        self.destDirFrame.grid(row=2, column=2, sticky='nw', padx=PADDING * 2, pady=PADDING * 2)

        self.destDirFrame.drop_target_register(DND_FILES)
        self.destDirFrame.dnd_bind('<<Drop>>', self.drop_dest)
        
        self.dhbar = tk.Scrollbar(self.destDirFrame, orient='horizontal')
        self.dhbar.grid(row=2, column=0, sticky='ew')

        self.dstDirTitle = ttk.Label(self.destDirFrame, text='Destination Folder:', font=('Arial', 15))
        self.dstDirTitle.grid(row=0, column=0, sticky='w')

        self.destDir = tk.Text(self.destDirFrame, width=30, height=1, font=('Consolas', 13), wrap='none', xscrollcommand=self.dhbar.set, state='disabled')
        self.destDir.grid(row=1, column=0)

        self.dhbar.config(command=self.destDir.xview)

        self.pasteButton = ttk.Button(self.methodFrame, text='Paste', command=self.paste, style='SRC.TButton')
        self.pasteButton.grid(row=1, column=0, columnspan=3, pady=PADDING, sticky='nsew', ipady=PADDING // 2)

        self.settingsButton = ttk.Button(self.methodFrame, text='Settings', command=lambda: self.open_settings(0), style='SRC.TButton')
        self.settingsButton.grid(row=2, column=0, columnspan=3, pady=PADDING * 5, sticky='nsew', ipady=PADDING // 2)

    def chooseSrc(self):
        tmp = filedialog.askopenfilenames(title='Choose the source files to copy', filetypes=[('All files', '*.*')])
        if tmp:
            self.srcFiless = tmp
            self.toggle_shrink()

    def drop_src(self, event):
        tmp = self.tk.splitlist(event.data)
        if tmp:
            self.srcFiless = tmp
            self.toggle_shrink()

    def toggle_shrink(self):
        isShrunk = self.shrinkVar.get()
        self.srcFiles.config(state='normal')
        if isShrunk:
            result = '\n'.join([str(Path(self.srcFiless[i]).name) for i in range(len(self.srcFiless))])
        else:
            result = '\n'.join([change_path(self.srcFiless[i]) for i in range(len(self.srcFiless))])
        self.srcFiles.delete('1.0', 'end')
        self.srcFiles.insert('1.0', result)
        self.srcFiles.config(state='disabled')

    def chooseDest(self):
        tmp = filedialog.askdirectory(title='Choose the destination directory')
        if tmp:
            self.destDirss = change_path(tmp)
            self.update_dest()

    def drop_dest(self, event):
        tmp = self.tk.splitlist(event.data)
        if tmp:
            tmp = ''.join(tmp)
            print(tmp)
            if Path(tmp).is_dir():
                self.destDirss = change_path(tmp)
                self.update_dest()
    
    def update_dest(self):
        self.destDir.config(state='normal')
        result = self.destDirss
        self.destDir.delete('1.0', 'end')
        self.destDir.insert('1.0', result)
        self.destDir.config(state='disabled')

    def paste(self):
        if not self.srcFiless:
            messagebox.showerror('Error', 'Please select the files to be copied.')
            return
        if not self.destDirss:
            messagebox.showerror('Error', 'Please select the destination folder the files will be copied into.')
            return
        for file in self.srcFiless:
            if not Path(file).exists():
                messagebox.showerror('Error', f'The file {change_path(file)} is not found.')
                return
        copy = not self.methodVar.get()
        for file in self.srcFiless:
            try:
                if copy:
                    shutil.copy(file, self.destDirss)
                else:
                    shutil.move(file, self.destDirss)
            except:
                messagebox.showerror('Error', f'Error copying the file {change_path(file)} to {change_path(self.destDirss)}.')
                return
            
        self.srcFiless = ''
        self.destDirss = ''
        self.toggle_shrink()
        self.update_dest()
    
    def open_settings(self, page):
        sapp = Settings(self, page)
        self.wait_window(sapp)
        sapp.mainloop()
        
app = App()
app.mainloop()