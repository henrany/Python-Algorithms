import unittest
from lib import bubbleSort

class TestAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.l = [9,4,6,2,1,3,5,7,8]
        self.expected = [1,2,3,4,5,6,7,8,9]
        self.bubble = bubbleSort()

    def testBubbleSort(self):
        self.assertEqual(self.bubble(self.l), self.expected)
