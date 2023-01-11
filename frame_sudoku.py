from logging import root
import tkinter as tk
from tkinter import font, ttk

class FrameSudoku:
    
    def __init__(self, color, root, program_data):
        self.root = root
        self.color = color
        self.program_data = program_data

        self.submit = tk.PhotoImage(file = r".\\images\\submit_default.png")
        self.submit_pressed = tk.PhotoImage(file = r".\\images\\submit_pressed.png")

        self.dial_on = [tk.PhotoImage(file = r".\\images\\dial_1_on.png",),
                        tk.PhotoImage(file = r".\\images\\dial_2_on.png"),
                        tk.PhotoImage(file = r".\\images\\dial_3_on.png"),
                        tk.PhotoImage(file = r".\\images\\dial_4_on.png"),
                        tk.PhotoImage(file = r".\\images\\dial_5_on.png"),
                        tk.PhotoImage(file = r".\\images\\dial_6_on.png"),
                        tk.PhotoImage(file = r".\\images\\dial_7_on.png"),
                        tk.PhotoImage(file = r".\\images\\dial_8_on.png"),
                        tk.PhotoImage(file = r".\\images\\dial_9_on.png")]

        self.dial_off = [tk.PhotoImage(file = r".\\images\\dial_1_off.png"),
                        tk.PhotoImage(file = r".\\images\\dial_2_off.png"),
                        tk.PhotoImage(file = r".\\images\\dial_3_off.png"),
                        tk.PhotoImage(file = r".\\images\\dial_4_off.png"),
                        tk.PhotoImage(file = r".\\images\\dial_5_off.png"),
                        tk.PhotoImage(file = r".\\images\\dial_6_off.png"),
                        tk.PhotoImage(file = r".\\images\\dial_7_off.png"),
                        tk.PhotoImage(file = r".\\images\\dial_8_off.png"),
                        tk.PhotoImage(file = r".\\images\\dial_9_off.png")]

        for i in range(len(self.dial_on)):
            self.dial_on[i] = self.dial_on[i].subsample(2,2)
        for i in range(len(self.dial_off)):
            self.dial_off[i] = self.dial_off[i].subsample(2,2)

        # Generator Frame Definitions----------
        self.frameGen = tk.LabelFrame(self.root, bd=0, padx=5, pady=5, bg=self.color['background'])
        self.frameGen.grid(row=0, column=0)

        # Create 2d-List to hold buttons
        rows, cols = (3,3)
        self.button_dials = [[0 for i in range(cols)] for j in range(rows)]
        for x in range(0, 3):
            for y in range(0,3):
                self.button_dials[x][y] = ttk.Button(self.frameGen, image = self.dial_off[int(self.program_data.puzzle_dic["start"][x][y])-1])
                self.button_dials[x][y].grid(row=x, column=y, sticky="nsew", padx=5, pady=5)

        
        # button_row_col
        # self.button_0_0 = ttk.Button(self.frameGen, image = self.dial_off[int(self.program_data.puzzle_dic["start"][0][0])-1])
        # self.button_0_1 = ttk.Button(self.frameGen, image = self.dial_off[int(self.program_data.puzzle_dic["start"][0][1])-1])
        # self.button_0_2 = ttk.Button(self.frameGen, image = self.dial_off[int(self.program_data.puzzle_dic["start"][0][2])-1])
        # self.button_1_0 = ttk.Button(self.frameGen, image = self.dial_off[int(self.program_data.puzzle_dic["start"][1][0])-1])
        # self.button_1_1 = ttk.Button(self.frameGen, image = self.dial_off[int(self.program_data.puzzle_dic["start"][1][1])-1])
        # self.button_1_2 = ttk.Button(self.frameGen, image = self.dial_off[int(self.program_data.puzzle_dic["start"][1][2])-1])
        # self.button_2_0 = ttk.Button(self.frameGen, image = self.dial_off[int(self.program_data.puzzle_dic["start"][2][0])-1])
        # self.button_2_1 = ttk.Button(self.frameGen, image = self.dial_off[int(self.program_data.puzzle_dic["start"][2][1])-1])
        # self.button_2_2 = ttk.Button(self.frameGen, image = self.dial_off[int(self.program_data.puzzle_dic["start"][2][2])-1])
        self.button_submit = ttk.Button(self.frameGen, image = self.submit)

        # self.button_0_0.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        # self.button_0_1.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        # self.button_0_2.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        # self.button_1_0.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        # self.button_1_1.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        # self.button_1_2.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
        # self.button_2_0.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        # self.button_2_1.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        # self.button_2_2.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
        self.button_submit.grid(row=0, column=3, rowspan=3, sticky="nsew", padx=5, pady=5)

        self.button_submit.bind('<Button-1>', self.button_pressed)
        self.button_submit.bind('<ButtonRelease-1>', self.button_released)
        
        # example get image path of assigned picture mapped to button
        # button.cget('image')==str(flag)

    def button_pressed(self, event):
        self.button_submit.config(image=self.submit_pressed)
    
    def button_released(self, event):
        self.button_submit.config(image=self.submit)
