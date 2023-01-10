import tkinter as tk
from tkinter import ttk, font
from frame_sudoku import *

class Core_Window:
    def __init__(self, program_data):

        # self.p_style = StyleHandler()
        
        self.root = tk.Tk() #Makes the window
        self.root.title("Puzzle")
        self.root.iconbitmap("dnd.ico")
        # self.root.geometry('1500x700')

        # --- Definitions
        self.color = {
            "notebookbg":"#1a1a1a",
            "notebookfg":"#000000",
            "background":"#232323",
            "button":"#333333",
            "untab":"#BB86FC",
            "selected":"#FFDD03",
            "not selected":"#333333",
            "header":"#FFDD00",
            "label text":"#BB86FC",
            "pressed":"#D3D3D3",
            "txt bg":"#232323",
            "txt fg":"#ffffff",
            "highlight":"#D3D3D3",
            "disabled":"#FF9494",
            "scrollbar":"#4d4d4d",
        }

        self.root.config(background = self.color['background'])
              
        # Create Notebook Style
        f = ('Segoe UI','10','bold')
        t = ('Segoe UI','10','normal')
        flabel = ('Segoe UI','16','underline')
        style = ttk.Style()
        style.theme_use('default')
        
        # Label Style
        style.configure('TLabel', font = flabel, padx=0, pady=0, background=self.color['background'], foreground=self.color['selected'], 
                        height=4, width=5, focuscolor=self.color['button'], justify ="center")

        # Button Style
        style.configure('TButton', font = f, borderwidth=0, padx=0, pady=0, background=self.color['background'], foreground=self.color['background'], 
                        height=4, width=18, focuscolor=self.color['background'], justify ="center")
        style.map('TButton', 
            foreground = [('disabled', self.color["background"]),
                        ('pressed', self.color["background"]),
                        ('selected', self.color['background'])], 
            background = [('disabled', self.color["background"]),
                        ('pressed', self.color["background"]),
                        ('active', self.color["background"])])
        
        # Future do comparison of puzzle type and call appropriate Frame_XXX
        self.puzzle_display = FrameSudoku(self.color, self.root, program_data)     





    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI