from logging import root
import tkinter as tk
from tkinter import font, ttk
import random
from os import listdir
from os.path import isfile, join

class FrameSudoku:
    
    def __init__(self, color, root, program_data):
        self.root = root
        self.color = color
        self.program_data = program_data

        self.submit = tk.PhotoImage(file = r".\\images\\submit_default.png")
        self.submit_pressed = tk.PhotoImage(file = r".\\images\\submit_pressed.png")

        # self.dial_img = self.program_data.dial_img_dic_gen()
        
        # [dial light ON][dial light OFF]
        self.dial_light = [[tk.PhotoImage(file = r".\\images\\dial_1_on.png"), tk.PhotoImage(file = r".\\images\\dial_1_off.png")],
                        [tk.PhotoImage(file = r".\\images\\dial_2_on.png"), tk.PhotoImage(file = r".\\images\\dial_2_off.png")],
                        [tk.PhotoImage(file = r".\\images\\dial_3_on.png"), tk.PhotoImage(file = r".\\images\\dial_3_off.png")],
                        [tk.PhotoImage(file = r".\\images\\dial_4_on.png"), tk.PhotoImage(file = r".\\images\\dial_4_off.png")],
                        [tk.PhotoImage(file = r".\\images\\dial_5_on.png"), tk.PhotoImage(file = r".\\images\\dial_5_off.png")],
                        [tk.PhotoImage(file = r".\\images\\dial_6_on.png"), tk.PhotoImage(file = r".\\images\\dial_6_off.png")],
                        [tk.PhotoImage(file = r".\\images\\dial_7_on.png"), tk.PhotoImage(file = r".\\images\\dial_7_off.png")],
                        [tk.PhotoImage(file = r".\\images\\dial_8_on.png"), tk.PhotoImage(file = r".\\images\\dial_8_off.png")],
                        [tk.PhotoImage(file = r".\\images\\dial_9_on.png"), tk.PhotoImage(file = r".\\images\\dial_9_off.png")]]
        
        self.dial_status = ('TButton', 'TButton_Locked')

        for x in range(len(self.dial_light)):
            for y in range(len(self.dial_light[x])):
                self.dial_light[x][y] = self.dial_light[x][y].subsample(2,2)

        # Generator Frame Definitions----------
        self.frameGen = tk.LabelFrame(self.root, bd=0, padx=5, pady=5, bg=self.color['background'])
        self.frameGen.grid(row=0, column=0)

        # Create 2d-List to hold buttons
        rows, cols = (3,3)
        self.button_dials = [[0 for i in range(cols)] for j in range(rows)]
        for x in range(0, 3):
            for y in range(0,3):
                if self.program_data.puzzle_dic["locked"][x][y] == 'x':
                    self.button_dials[x][y] = ttk.Button(self.frameGen, style = self.dial_status[1], image = self.dial_light[int(self.program_data.puzzle_dic["start"][x][y])-1][random.randint(0, 1)])
                else:
                    self.button_dials[x][y] = ttk.Button(self.frameGen, style = self.dial_status[0], image = self.dial_light[int(self.program_data.puzzle_dic["start"][x][y])-1][random.randint(0, 1)])
                self.button_dials[x][y].grid(row=x, column=y, sticky="nsew", padx=5, pady=5)

        self.button_submit = ttk.Button(self.frameGen, image = self.submit)
        self.button_submit.grid(row=0, column=3, rowspan=3, sticky="nsew", padx=5, pady=5)
        self.button_submit.bind('<Button-1>', self.button_pressed)
        self.button_submit.bind('<ButtonRelease-1>', self.button_released)
        
        # example get image path of assigned picture mapped to button
        # button.cget('image')==str(flag)

    def button_pressed(self, event):
        self.button_submit.config(image=self.submit_pressed)
    
    def button_released(self, event):
        self.button_submit.config(image=self.submit)
