'''
das
'''
import unittest
import simple3

class Testsimple3(unittest.Testcase):
    '''
    rfe
    '''
    def test_one_word(self):
        text = "python"
        result = simple3.cap_text(text)
        self.assertEqual(result,"Python")

    def test_multiple_words(self):
        text = "monty python"
        result = simple3.cap_text(text)
        self.assertEqual(result,"Monty Python")

if __name__ == "__main__":
    unittest.main()
