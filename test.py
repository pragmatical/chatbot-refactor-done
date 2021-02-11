import unittest
from main import decide_response


class TestDecideRespons(unittest.TestCase):

    def test_askForName(self):
        input="What is your name?"
        self.assertEqual(decide_response(input),"My name is chatbot! What's yours?","Response was incorrect for input:" + input )
    
    def test_otherInput(self):
        input="Something else"
        self.assertEqual(decide_response(input),"Sorry I didn't understand that.","Response incorrect for input: " + input)

if __name__ == '__main__':
    unittest.main()