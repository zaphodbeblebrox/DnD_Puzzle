import unittest
# from main import *
import file_import as fi

class FileImportTests(unittest.TestCase):
    def test_read_file(self):
        file_path = ".\\config\\display_config.txt"
        t = fi.read_in_file(file_path)
        self.assertEqual(t[0], "zoom;3")

    def test_delimitate_array(self):
        file_path = ".\\config\\display_config.txt"
        t = fi.read_in_file(file_path)
        s = fi.delimitate_array(t)
        self.assertEqual(s[0], ["zoom","3"])

    def test_get_subdirectory_list(self):
        dir_path = ".\\"
        directories = fi.get_subdirectories(dir_path)
        result = False
        if "puzzles" in directories:
            result = True
        self.assertEqual(result, True)

    def test_get_txts_in_dir(self):
        dir_path = ".\\config\\"
        files = fi.get_txts_in_dir(dir_path)
        result = False
        if "display_config.txt" in files:
            result = True
        self.assertEqual(result, True)