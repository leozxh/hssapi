import unittest



class StartEnd(unittest.TestCase):

    def setUp(self):
        print("start testing")

    def tearDown(self):
        print("End testing")