from core_window import *
from data_handler import *
import file_management as fm

program_data = Data_Handler()
# my_window = Core_Window(program_data)
# my_window.start()

puzzle_path = ".\\puzzles\\"
# Read in Puzzle Type Options
puzzle_types = fm.get_subdirectories(puzzle_path)
puzzle_dic = {}
for x in puzzle_types:
    puzzle_dic[x] = fm.get_txts_in_dir(puzzle_path + x + "\\")

# Create prompt, importing puzzle_types & puzzle_dic
