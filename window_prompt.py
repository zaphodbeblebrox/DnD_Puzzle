import tkinter as tk
from tkinter import ttk, font
from frame_sudoku import *

class WindowPrompt:
    def __init__(self, puzzle_types, puzzle_dic):
        self.puzzle_types = puzzle_types
        self.puzzle_dic = puzzle_dic

        self.root = tk.Tk() #Makes the window
        self.root.title("Puzzle Selection")
        self.root.iconbitmap("dnd.ico")
        # self.root.geometry('1500x700')

        # --- Definitions
        self.color = {
            "background":"#232323",
            "button":"#333333",
            "selected":"#FFDD03",
            "not selected":"#333333",
            "label text":"#BB86FC",
            "pressed":"#D3D3D3",
            "txt bg":"#232323",
            "txt fg":"#ffffff",
            "highlight":"#D3D3D3",
            "disabled":"#FF9494",
        }

        self.root.config(background = self.color['background'])
        #---------------------------------------------------------------------------------------------------------------------------------- 
        # Create Styles
        f = ('Segoe UI','10','bold')
        t = ('Segoe UI','10','normal')
        flabel = ('Segoe UI','16','underline')
        style = ttk.Style()
        style.theme_use('default')
        
        # Label Style
        style.configure('TLabel', font = flabel, padx=0, pady=0, background=self.color['background'], foreground=self.color['selected'], 
                        height=4, width=5, focuscolor=self.color['button'], justify ="center")

        # Button Style
        # style.configure('TButton', font = f, borderwidth=0, padx=0, pady=0, background=self.color['background'], foreground=self.color['background'], 
        #                 height=4, width=18, focuscolor=self.color['background'], justify ="center")
        style.configure('TButton', font = f, borderwidth=0, padx=0, pady=0, background=self.color['background'], foreground=self.color['background'], 
                focuscolor=self.color['background'], justify ="center")
        style.map('TButton', 
            foreground = [('disabled', self.color["background"]),
                        ('pressed', self.color["background"]),
                        ('selected', self.color['background'])], 
            background = [('disabled', self.color["background"]),
                        ('pressed', self.color["background"]),
                        ('active', self.color["background"])])
        #---------------------------------------------------------------------------------------------------------------------------------- 
        
        # Create the Frame in which elements shall be placed
        self.frameGen = tk.LabelFrame(self.root, bd=0, padx=5, pady=5, bg=self.color['background'])
        self.frameGen.grid(row=0, column=0)

        ttk.Label("D&D Puzzle Selection").grid(row=0, column=0, columnspan=2)
        
        ttk.Label("Select Puzzle Type:").grid(row=1, column=0)


        ttk.Label("Select Puzzle:").grid(row=2, column=0)




    def start(self):
        self.root.mainloop() # Start monitoring and updating the GUI

    def stop(self):
        self.root.destroy()  # Close tk window