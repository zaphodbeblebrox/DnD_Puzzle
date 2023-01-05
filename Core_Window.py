import tkinter as tk
from tkinter import ttk, font
from Tab_Enchantments import *
from style_handler import *
from Tab_Loot_Generator import *
# from Tab_Gem_Art import *

class Core_Window:
    def __init__(self, program_data):

        self.p_style = StyleHandler()
        
        self.root = tk.Tk() #Makes the window
        self.root.title("Random Loot Generator")
        self.root.iconbitmap("dnd.ico")
        # self.root.geometry('1500x700')
        self.root.config(background = self.p_style.color['background'])

        # Tab Definitions
        self.notebook = ttk.Notebook(self.root)

        self.tabGen = ttk.Frame(self.notebook)
        self.tabEnchantment = ttk.Frame(self.notebook)
        self.tabGems = ttk.Frame(self.notebook)
        self.tabMagic = ttk.Frame(self.notebook)
        self.tabStatusEffects = ttk.Frame(self.notebook)
        self.tag_definitions = ttk.Frame(self.notebook)

        self.notebook.add(self.tabGen, text="Loot Generator")
        self.notebook.add(self.tabEnchantment, text="Enchantments")
        self.notebook.add(self.tabGems, text="Gem & Art Table")
        self.notebook.add(self.tabMagic, text="Magic Reference")
        self.notebook.add(self.tabStatusEffects, text="Status Effects")
        self.notebook.add(self.tag_definitions, text="Tag Definitions")
        self.notebook.grid(row=0, column=0)

        Tab_Loot_Generator(self.p_style.color, self.tabGen, program_data)
        Tab_Enchantments(self.p_style.color, self.tabEnchantment, program_data)
        # Tab_Gem_Art(self.color, self.tabEnchantment, program_data)

    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI