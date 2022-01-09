import unittest
from lib import sorting, search

class TestAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.l = [9,4,6,2,1,3,5,7,8]
        self.expected = [1,2,3,4,5,6,7,8,9]
        self.unExpected = [1,2,3,4,5,6,7,9,8]

    def testBubbleSort(self):
        self.assertEqual(sorting.Sorting.bubbleSort(self.l), self.expected)

    def testInsertionSort(self):
        self.assertEqual(sorting.Sorting.insertionSort(self.l), self.expected)

    def testSelectionSortEqual(self):
        self.assertEqual(sorting.Sorting.selectionSort(self.l), self.expected)

    def testSelectionSortNotEqual(self):
        self.assertNotEqual(sorting.Sorting.selectionSort(self.l),self.unExpected)
        
    def testLinearSearchIsTrue(self):
        self.assertTrue(search.Search.linearSearch(self.l, 6))
    
    def testLinearSearchIsFalse(self):
        self.assertFalse(search.Search.linearSearch(self.l, 20))

    def testBubbleSearchIsTrue(self):
        self.assertTrue(search.Search.binarySearch(self.expected, 5))

    def testBubbleSearchIsFalse(self):
        self.assertFalse(search.Search.binarySearch(self.expected, 10))

    def testJumpSearchIsTrue(self):
        self.assertTrue(search.Search.jumpsearch(self.expected, 6))

    def testJumpSearchIsFalse(self):
        self.assertFalse(search.Search.jumpsearch(self.expected, 10))

    def tearDown(self):
        self.l.clear()
        self.expected.clear()
