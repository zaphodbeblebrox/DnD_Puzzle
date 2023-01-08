import sys
from Core_Window import *
from os import listdir
from os.path import isfile, join

class Data_Handler:
    def __init__(self):
        # self.fileName = fileName
        puzzle_dir = '.\\puzzles\\'
        puzzle_path = [f for f in listdir('.\\puzzles') if isfile(join(puzzle_dir, f))]
        message = "Available Puzzles:\n"
        for i in puzzle_path:
            message = message + str(i) + '\n'
        message = message + "Select a Puzzle to run: "
        # puzzle_selection = int(input(message)) - 1
        puzzle_selection = 0
        if (puzzle_selection < 0) or (puzzle_selection >= len(puzzle_path)):
            print("Error! Input Out of Bounds!")
            sys.exit()
        
        raw_data = self.read_file(puzzle_dir + puzzle_path[puzzle_selection])
        if len(raw_data) != 9:
            print("Error in File Data!")
            sys.exit()
        
        temp_data = self.parse_data(raw_data)
        
        rows, cols = (3,3)
        self.puzzle_dic = {}
        self.puzzle_dic['start'] = [[0 for i in range(cols)] for j in range(rows)]
        self.puzzle_dic['locked'] = [[0 for i in range(cols)] for j in range(rows)]
        self.puzzle_dic['answer'] = [[0 for i in range(cols)] for j in range(rows)]
        
        self.fill_dic_2d_list(temp_data, 'start', 0, 2)
        self.fill_dic_2d_list(temp_data, 'locked', 3, 5)
        self.fill_dic_2d_list(temp_data, 'answer', 6, 8)

        pause = ""

    def fill_dic_2d_list(self, data, key, start, end):
        for x in range(0, 3):
            for y in range(0,3):
                self.puzzle_dic[key][x][y]=data[x+start][y]
    
    def read_file(self, fileName):
        content_array = []
        with open(fileName) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_array.append(line.replace('\n',''))
        return content_array
    
    def parse_data(self, array):
        deliminator = ';'
        temp = []
        for i in range(len(array)):
            tempArray = array[i].split(deliminator)
            temp.append(tempArray)
        return temp

