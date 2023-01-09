from logging import root
import tkinter as tk
from tkinter import font, ttk

class FrameSudoku:
    
    def __init__(self, color, root, program_data):
        self.root = root
        self.color = color
        self.program_data = program_data

        self.submit = tk.PhotoImage(file = r".\\images\\submit.png")

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
        # self.submit = self.submit.subsample(2,2)
        f = font.Font(weight = "bold", size= 10)

        # Generator Frame Definitions----------

        self.frameGen = tk.LabelFrame(self.root, bd=0, padx=5, pady=5, bg=self.color['background'])
        self.frameGen.grid(row=0, column=0)

        # button_row_col
        self.button_0_0 = tk.Button(self.frameGen, padx=5, pady=5, bg=self.color['background'], image = self.dial_off[int(self.program_data.puzzle_dic["start"][0][0])-1])
        self.button_0_1 = tk.Button(self.frameGen, padx=5, pady=5, bg=self.color['background'], image = self.dial_off[int(self.program_data.puzzle_dic["start"][0][1])-1])
        self.button_0_2 = tk.Button(self.frameGen, padx=5, pady=5, bg=self.color['background'], image = self.dial_off[int(self.program_data.puzzle_dic["start"][0][2])-1])
        self.button_1_0 = tk.Button(self.frameGen, padx=5, pady=5, bg=self.color['background'], image = self.dial_off[int(self.program_data.puzzle_dic["start"][1][0])-1])
        self.button_1_1 = tk.Button(self.frameGen, padx=5, pady=5, bg=self.color['background'], image = self.dial_off[int(self.program_data.puzzle_dic["start"][1][1])-1])
        self.button_1_2 = tk.Button(self.frameGen, padx=5, pady=5, bg=self.color['background'], image = self.dial_off[int(self.program_data.puzzle_dic["start"][1][2])-1])
        self.button_2_0 = tk.Button(self.frameGen, padx=5, pady=5, bg=self.color['background'], image = self.dial_off[int(self.program_data.puzzle_dic["start"][2][0])-1])
        self.button_2_1 = tk.Button(self.frameGen, padx=5, pady=5, bg=self.color['background'], image = self.dial_off[int(self.program_data.puzzle_dic["start"][2][1])-1])
        self.button_2_2 = tk.Button(self.frameGen, padx=5, pady=5, bg=self.color['background'], image = self.dial_off[int(self.program_data.puzzle_dic["start"][2][2])-1])
        self.button_submit = tk.Button(self.frameGen, padx=5, pady=5, bg=self.color['background'], image = self.submit)

        self.button_0_0.grid(row=0, column=0, sticky="nsew", padx=5, pady=5, ipadx=5, ipady=5)
        self.button_0_1.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.button_0_2.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        self.button_1_0.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.button_1_1.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self.button_1_2.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
        self.button_2_0.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        self.button_2_1.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        self.button_2_2.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
        self.button_submit.grid(row=0, column=3, rowspan=3, sticky="nsew", padx=5, pady=5)
