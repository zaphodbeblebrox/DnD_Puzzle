from Core_Window import *
from Data_Import import *

class Data_Handler:
    def __init__(self):
        # self.fileName = fileName
        self.itemTypeList = []
        self.masterList = Data_Import.read_file('.\\File_Master_List.txt')
        self.itemTypeList = Data_Import.parse_dataset(Data_Import.read_file(self.masterList[1]), ";")
        
        path_individual = Data_Import.read_file(self.masterList[2])
        self.individualTreasure = {
            "0-4":Data_Import.read_file(path_individual[0]),
            "5-10":Data_Import.read_file(path_individual[1]),
            "11-16":Data_Import.read_file(path_individual[2]),
            "17-20":Data_Import.read_file(path_individual[3])
            }
        
        path_horde = Data_Import.read_file(self.masterList[3])
        self.hordeTreasureCoins = {
            "0-4":Data_Import.read_file(path_horde[0]),
            "5-10":Data_Import.read_file(path_horde[1]),
            "11-16":Data_Import.read_file(path_horde[2]),
            "17-20":Data_Import.read_file(path_horde[3])
        }
        self.hordeTreasureItems = {
            "0-4":Data_Import.read_file(path_horde[4]),
            "5-10":Data_Import.read_file(path_horde[5]),
            "11-16":Data_Import.read_file(path_horde[6]),
            "17-20":Data_Import.read_file(path_horde[7])
        }
        self.tags = Data_Import.create_dictionary(self.masterList[4])
        self.mit = Data_Import.create_dictionary(self.masterList[5])

        # Import Time
        armor = Data_Import.create_dictionary(self.masterList[6]) # Import Armors - Basic and Magic
        self.potion = Data_Import.create_dictionary(self.masterList[7]) # Import Potions
        ring = Data_Import.create_dictionary(self.masterList[8]) # Import Rings
        rod = Data_Import.create_dictionary(self.masterList[9]) # Import Rods
        shield = Data_Import.create_dictionary(self.masterList[10]) # Import Shields - Basic and Magic
        self.spell = Data_Import.create_dictionary(self.masterList[11]) # Import Spells
        staff = Data_Import.create_dictionary(self.masterList[12]) # Import Staffs
        wand = Data_Import.create_dictionary(self.masterList[13]) # Import Wands
        weapon = Data_Import.create_dictionary(self.masterList[14]) # Import Weapons - Basic and Magic
        wondrous = Data_Import.create_dictionary(self.masterList[15]) # Import Wondrous

        self.asw = armor | shield | weapon
        self.rrsww = ring | rod | staff | wand | wondrous

        self.enchantments = Data_Import.create_dictionary(self.masterList[16]) # Import Enchantments
        self.elt = Data_Import.create_dictionary(self.masterList[17])
        self.asw_loot_table = Data_Import.create_dictionary(self.masterList[18])

        self.aglt = Data_Import.create_dictionary(self.masterList[19])

        pause = ""










