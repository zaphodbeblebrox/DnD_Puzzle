from os import listdir, walk
from os.path import isfile, join, isdir

# Reads in the given file
def read_in_file(filename):
    content_array = []
    with open(filename) as f:
        for line in f:
            content_array.append(line.replace('\n',''))
    return content_array

# Breaks the given array based on the dilimiter
def delimitate_array(array):
    delimiter = ';'
    temp = []
    for i in range(len(array)):
        tempArray = array[i].split(delimiter)
        temp.append(tempArray)
    return temp

# Returns an array of all immediate subdirectories
def get_subdirectories(dir_path):
    subdirectory_list = [item for item in listdir(dir_path) if isdir(join(dir_path, item)) ]
    return subdirectory_list

# Returns an array of all *.txt files in the given directory
def get_txts_in_dir(dir_path):
    file_list = []
    for file in listdir(dir_path):
        if file.endswith(".txt"):
            file_list.append(file)
    return file_list
    
# X Returns a array of all scripts belonging to given UUT P/N and the path to them
def get_scripts(uut_pn):
    path = ".\\RS232_CONFIG_FILES\\UUT\\SCRIPTS\\"
    monitor_type = get_subdirectories(path)
    for dir in monitor_type:
        if uut_pn[0] == dir[0]:
            path += dir
            break
    monitor_type = get_subdirectories(path)
    for dir in monitor_type:
        if uut_pn == dir:
            path += "\\" + dir + "\\"
            break
    return path, get_txts_in_dir(path)

# X Grab each unique item in array 
def get_unique_array_items(array):
    unique_formats = []
    for data in array:
        if data not in unique_formats:
            unique_formats.append(data)
    return unique_formats

