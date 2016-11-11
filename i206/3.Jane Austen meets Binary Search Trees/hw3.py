#---------------------------------------------------------
# Monicah Mumbi Wambugu
# monicah_wambugu@berkeley.edu
# Homework #3
# September 20, 2016
# hw3.py
# Main
#---------------------------------------------------------

from BST import *


def read_file(filename):
    with open(filename, 'rU',encoding='utf-8') as document:
        text = document.read()
    filter_punc = lambda t: ''.join([x.lower() for x in t if x.isalpha()])
    words = [x for x in map(filter_punc, text.split()) if x]
    return words


def main():
    while(True):
        print("Enter the file name to read:")
        filename = input('> ')
        try:
            words = read_file(filename)
        except IOError:
            print("Unable to find the file {}".format(filename))
        else:
            tree = BSTree()
            for word in words:
                tree.add(word)
            
            
            ######################
            # Begin Student Code #
            ######################
            #tree.in_order_print()
            while(True):
                query_string = str(input('\nQuery? ')).lower()
                if query_string == 'stats':
                    print('\nSize (total entries): ' +str(tree.size()))
                    print('Maximum Height/Depth: ' +str(tree.height()))
                elif query_string == 'terminate':
                    break 
                else:
                    tree.find(query_string)

            break


if __name__ == "__main__":
    main()
