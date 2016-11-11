'''
(1) A reversi number is a number that reads the same forwards and backwards, such as 303.
   The largest reversi number that is a product of two 2-digit numbers is 9009 = 91 x 99.
   Write a Python program to find the largest reversi number that is a product of two 3-digit numbers.

Your output format should be "abc x def = ghiihg" (where the letters are replaced by digits).
'''
from itertools import combinations as c

def isReversi(string):
    if str(string) == ''.join(reversed(str(string))):
        return True
    else:
        return False
    

def largestReversi():
    largestR=0
    x=0
    y=0
    for i in range(100,1000):
        for j in range(100,1000):
            if isReversi(i*j) and (i*j) > largestR:
                largestR = i*j
                x=i
                y=j                  
    return str(x)+' x '+ str(y) + ' = ' + str(largestR)


print(largestReversi())
