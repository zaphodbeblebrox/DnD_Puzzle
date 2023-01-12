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

        self.locked = 'x'

        # Import Dial/Button Images
        self.attempt_img = [tk.PhotoImage(file = r".\\images\\attempt_0.png"),
                        tk.PhotoImage(file = r".\\images\\attempt_1.png"),
                        tk.PhotoImage(file = r".\\images\\attempt_2.png"),
                        tk.PhotoImage(file = r".\\images\\attempt_3.png")]

        self.submit = tk.PhotoImage(file = r".\\images\\submit_c.png")
        self.submit_pressed = tk.PhotoImage(file = r".\\images\\submit_uc.png")
        self.dial_img = self.program_data.dial_img_dic_gen()
        
        # Generator Frame Definitions----------
        self.frameGen = tk.LabelFrame(self.root, bd=0, padx=5, pady=5, bg=self.color['background'])
        self.frameGen.grid(row=0, column=0)

        # Create 2d-List to hold buttons
        rows, cols = (3,3)
        self.button_dials = [[0 for i in range(cols)] for j in range(rows)]
        for x in range(0, 3):
            for y in range(0,3):
                key = self.generate_key((x,y))
                # light_status = 'F' if random.randint(0, 1) == 0 else 'N'
                # lock_status = 'L' if self.program_data.puzzle_dic["locked"][x][y] == self.locked else 'U'
                # key = light_status + lock_status

                self.button_dials[x][y] = ttk.Button(self.frameGen, image = self.dial_img[self.program_data.puzzle_dic["start"][x][y]][key], command=lambda id=(x,y): self.exe_dial_evt(id))
                self.button_dials[x][y].grid(row=x, column=y, sticky="nsew", padx=5, pady=5)

        self.label_attempt = ttk.Label(self.frameGen, image = self.attempt_img[0])
        self.label_attempt.grid(row=0, column=3, padx=5, pady=5)

        self.button_submit = ttk.Button(self.frameGen, image = self.submit, command = self.check_solution)
        self.button_submit.grid(row=1, column=3, rowspan=2, sticky="nsew", padx=5, pady=5)
        self.button_submit.bind('<Button-1>', self.button_pressed)
        self.button_submit.bind('<ButtonRelease-1>', self.button_released)
        
    def button_pressed(self, event):
        self.button_submit.config(image=self.submit_pressed)
    
    def button_released(self, event):
        self.button_submit.config(image=self.submit)

    def check_solution(self):
        pass
    
    def generate_key(self, id):
        #id is formatted as (x,y) for self.program_data.puzzle_dic[key][x][y] 
        light_status = 'F' if random.randint(0, 1) == 0 else 'N'
        lock_status = 'L' if self.program_data.puzzle_dic["locked"][id[0]][id[1]] == self.locked else 'U'
        return light_status + lock_status

    def exe_dial_evt(self, id):
        #id is formatted as (x,y) for self.program_data.puzzle_dic[key][x][y] 
        # check if dial is locked
        if self.program_data.puzzle_dic["locked"][id[0]][id[1]] == self.locked:
            return

        key = self.generate_key(id)
        value = int(self.program_data.puzzle_dic["current"][id[0]][id[1]])
        if value < 4:
            value = value + 1
        elif value == 4:
            value = 1
        elif value < 8:
            value = value + 1
        elif value == 8:
            value = 5
        self.program_data.puzzle_dic["current"][id[0]][id[1]] = str(value)
        self.button_dials[id[0]][id[1]].config(image = self.dial_img[self.program_data.puzzle_dic["current"][id[0]][id[1]]][key])

        pass