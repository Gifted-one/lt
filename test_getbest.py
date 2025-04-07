import unittest
import sys
import os
import getbest

'''Gets the path of the csv file'''
dir = os.path.dirname(__file__)


class TestTheMark(unittest.TestCase):
	''' Setup componet to open the csv file'''
	def setUp(self):
	    self.just_data = getbest.data(os.path.join(dir,"bestdat0.csv"))
	    self.mark_data = getbest.getCols(self.just_data)


	'''Tests if the mark is on the third column'''
	def testMarkcolumn(self):
	    num_col, mark_col = self.mark_data
	    self.assertEqual(mark_col, 2)

	'''Test if the student no is in the second column'''
	def testStuNo_Column(self):
	    num_col, mark_col = self.mark_data
	    self.assertEqual(num_col, 1)

	'''Test if the highest mark is 90'''
	def testHighestMark(self):
	    num_col, mark_col = self.mark_data
	    StudenNo, Mark = getbest.findTop(self.just_data, num_col, mark_col)
	    self.assertEqual(Mark,90)




if __name__ == '__main__': 
    
    unittest.main()

