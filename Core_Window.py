import tkinter as tk
from tkinter import ttk, font



class Core_Window:
    def __init__(self, program_data):

        self.p_style = StyleHandler()
        
        self.root = tk.Tk() #Makes the window
        self.root.title("Puzzle")
        self.root.iconbitmap("dnd.ico")
        # self.root.geometry('1500x700')
        self.root.config(background = self.p_style.color['background'])

        # --- Definitions





    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI