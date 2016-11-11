#---------------------------------------------------------
# Monicah Mumbi Wambugu
# monicah_wambugu@berkeley.edu
# Homework #3
# September 20, 2016
# hw3test.py
# Test
#---------------------------------------------------------

from BST import *
from hw3 import *
import unittest

T = BSTree()

emptyTree = BSTree()
one_node_Tree =BSTree()
one_node_Tree.add("one_node")

T.add("good")
T.add("morning")
T.add("morning")
T.add("america")

#Testing find()
T.find("morning") #True
T.find("august") #False

T.in_order_print()




class TestBST(unittest.TestCase):
    def test_size(self):
         self.assertEqual(emptyTree.size(),0)
         self.assertEqual(one_node_Tree.size(),1)
         self.assertEqual(T.size(),3)

    def test_height(self):
         self.assertEqual(emptyTree.height(),0)
         self.assertEqual(one_node_Tree.height(),1)
         self.assertEqual(T.height(),2)

unittest.main()
