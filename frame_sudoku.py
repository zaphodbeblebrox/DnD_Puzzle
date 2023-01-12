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

        # Import Dial/Button Images
        self.attempt_img = [tk.PhotoImage(file = r".\\images\\attempt_0.png"),
                        tk.PhotoImage(file = r".\\images\\attempt_1.png"),
                        tk.PhotoImage(file = r".\\images\\attempt_2.png"),
                        tk.PhotoImage(file = r".\\images\\attempt_3.png")]
        

        # self.submit = tk.PhotoImage(file = r".\\images\\submit_default.png")
        # self.submit_pressed = tk.PhotoImage(file = r".\\images\\submit_pressed.png")
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
                light_status = 'F' if random.randint(0, 1) == 0 else 'N'
                lock_status = 'L' if self.program_data.puzzle_dic["locked"][x][y] == 'x' else 'U'
                key = light_status + lock_status

                self.button_dials[x][y] = ttk.Button(self.frameGen, image = self.dial_img[self.program_data.puzzle_dic["start"][x][y]][key], command=lambda id=str(x)+str(y): self.exe_dial_evt(id))
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
    
    def exe_dial_evt(self, id):
        pass