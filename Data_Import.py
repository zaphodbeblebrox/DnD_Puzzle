from Core_Window import *
import glob as glob

class Data_Import:
    def __init__(self):
        # self.fileName = fileName
        self.itemTypeList = []
        self.itpath = '.\\Items\\Item_Types.txt'
        # self.ReadFile(self.itpath)

    def read_file(fileName):
        content_array = []
        with open(fileName) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_array.append(line.replace('\n',''))
        return content_array

    def parse_dataset(array, deliminator):
        temp = []
        for i in range(len(array)):
            tempArray = array[i].split(deliminator)
            temp.append(tempArray)
        return temp

    def create_dictionary(filepath):
        tag_dictionary = {}
        for file in glob.glob(filepath + "*.txt"):
            file = file.replace("\\", "/")
            value = Data_Import.read_file(file)
            file = file.replace(filepath, "")
            file = file.replace(".txt", "")
            key = file
            tag_dictionary[key] = value    
        return tag_dictionary


