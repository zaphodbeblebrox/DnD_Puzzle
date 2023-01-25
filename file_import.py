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
    
# Returns a array of all scripts belonging to given UUT P/N and the path to them
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

# Reads in ATP script file and rtns baud rate and 2-d array containing the rest of the file dilimitated.
def read_script_file(file):
    data = read_in_file(file)
    baud_rate = data.pop(0)
    data = delimitate_array(data)
    return baud_rate, data

# Grab each unique item in array - targeted for script files
def get_unique_cmd_formats(array):
    unique_formats = []
    for data in array:
        if data[1] not in unique_formats:
            unique_formats.append(data[1])
    return unique_formats

# Grab each unique item in array 
def get_unique_array_items(array):
    unique_formats = []
    for data in array:
        if data not in unique_formats:
            unique_formats.append(data)
    return unique_formats

