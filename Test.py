import unittest
from lib import bubbleSort

class TestAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.l = [9,4,6,2,1,3,5,7,8]
        self.expected = [1,2,3,4,5,6,7,8,9]

    def testBubbleSort(self):
        self.assertEqual(bubbleSort(self.l), self.expected)
