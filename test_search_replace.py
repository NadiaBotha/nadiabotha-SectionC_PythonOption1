#Import unittest - classes need to inherit methods for unit testing
import unittest
#Import the search_replace file to access it.
import search_replace

#Define a class TestSearchAndReplace and inherit TestCase method.
class TestSearchAndReplace(unittest.TestCase):

    #For this specific scenario, there are four test cases:
    # 1. Substring is replaced successfully at the start of a main string
    # 2. Substring is replaced successfully in the middle of a main string
    # 3. Substring is replaced successfully at the end of a main string
    # 4. Exception handling when the substring entered is not in the main string.

    #Two tests have been created for each test case.

    # Test case 1 - check if the substring is successfully replaced at the start of the main string
    def test_search_and_replace_beginning_one(self):
        result = search_replace.search_and_replace("Hello World!", "Hel", "@@", 0)
        self.assertEqual(result, "@@lo World!")

    def test_search_and_replace_beginning_two(self):
        result = search_replace.search_and_replace("I am Batman", "I", "!!", 0)
        self.assertEqual(result, "!! am Batman")

    # Test case 2 - check if the substring is successfully replaced in the middle of the main string
    def test_search_and_replace_middle_one(self):
        result = search_replace.search_and_replace("Hello World!", "llo", "@@",0)
        self.assertEqual(result,"He@@ World!")

    def test_search_and_replace_middle_two(self):
        result = search_replace.search_and_replace("I am Batman", "am", "!!",0)
        self.assertEqual(result,"I !! Batman")

    # Test case 3 - check if the substring is successfully replaced at the end of the main string
    def test_search_and_replace_end_one(self):
        result = search_replace.search_and_replace("Hello World!", "ld!", "@@",0)
        self.assertEqual(result,"Hello Wor@@")

    def test_search_and_replace_end_two(self):
        result = search_replace.search_and_replace("I am Batman", "man", "!!",0)
        self.assertEqual(result,"I am Bat!!")

    # Test case 4 - check if the error message is displayed when the user enters a substring that is not
    # in the main string
    def test_search_and_replace_notfound_one(self):
        result = search_replace.search_and_replace("Hello World!", "lde", "@@",0)
        self.assertEqual(result,"ERROR: The substring entered is not found.")

    def test_search_and_replace_notfound_two(self):
        result = search_replace.search_and_replace("I am Batman", "Robin", "!!",0)
        self.assertEqual(result,"ERROR: The substring entered is not found.")
    
