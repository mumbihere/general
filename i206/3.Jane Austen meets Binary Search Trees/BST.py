#---------------------------------------------------------
# Monicah Mumbi Wambugu
# monicah_wambugu@berkeley.edu
# Homework #3
# September 20, 2016
# BST.py
# BST
# References: http://www.geeksforgeeks.org/ http://stackoverflow.com/
# ---------------------------------------------------------

class Node:
    #Constructor Node() creates node
    def __init__(self,word):
        self.word = word
        self.right = None
        self.left = None
        self.count = 1



class BSTree:
    #Constructor BSTree() creates empty tree
    def __init__(self, root=None):
        self.root = root
    
    #These are "external functions" that will be called by your main program - I have given these to you
    
    #Find word in tree
    def find(self, word):
        return _find(self.root, word)
    
    #Add node to tree with word
    def add(self, word):
        if not self.root:
            self.root = Node(word)
            return
        _add(self.root, word)

    #Print in order entire tree
    def in_order_print(self):
        _in_order_print(self.root)

    def size(self):
        return _size(self.root)

    def height(self):
        return _height(self.root)
    


#These are "internal functions" in the BSTree class - You need to create these!!!


#Function to add node with word as word attribute
def _add(root, word):
    if root.word == word:
        root.count +=1
        return
    if root.word > word:
        if root.left == None:
            root.left = Node(word)           
        else:
            _add(root.left, word)       
    else:
        if root.right == None:
            root.right =Node(word)

        else:
            _add(root.right, word)
            
    
    
#Function to find word in tree
def _find(root, word):
    if root.word == word:
        print('The word '+word+' appears '+str(root.count)+' time(s) in the tree ')
        return True
    elif root.word > word:
        if root.left == None:
            print('The word '+word+' does not appear in the tree ')
            return False
        else:
            _find(root.left, word)
    else:
        if root.right == None:
            print('The word '+word+' does not appear in the tree ')
            return False
        else:
            _find(root.right, word)



#Get number of nodes in tree
def _size(root):
    #YOU FILL THIS IN
    #1. If tree is empty then return 0
    if root == None:
        return 0
    else:
        left_subtree = _size( root.left)
        right_subtree = _size( root.right)
        size = left_subtree + right_subtree + 1
        return size
    

#Get height of tree
def _height(root):
    #YOU FILL THIS IN
    # A tree consisting only of one item (root) has a height of 1
    # An empty tree has a height of 0
    
    if root ==None: #If tree is empty then return 0
        return 0
    else:
        left_subtree = _height(root.left)
        right_subtree = _height(root.right)
        depth = max(left_subtree,right_subtree) + 1
        return depth

    
#Function to print tree in order
def _in_order_print(root):
    if not root:
        return
    _in_order_print(root.left)
    print(root.word)
    print(_height(root))
    _in_order_print(root.right)

    
    




    
    
