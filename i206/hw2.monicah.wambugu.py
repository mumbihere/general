'''
In this assignment, you will write a password strength checker in Python.

Part (1)

In this part, you will prompt the user for a test password.  Check the password for the following conditions:

(a)  It has at least one uppercase and at least one lowercase letter
(b)  It has at least one digit
(c)  It has at least one character that is not a letter or a digit
(d)  It has a length of at least six characters

If exactly no conditions are met:  report that the password is "very weak"
If exactly one condition is met:  report that the password is "weak"
If exactly two conditions are met:  report that the password is "medium strength"
If exactly three conditions are met:  report that the password "high medium strength"
If all four conditions are met:  report that the password is "strong"

You should also output which conditions are met and not met.

The program should continue prompting the user for passwords until the user types "finish"



Part (2)

In this part you will add a further check:  that the password does not appear in a list of common passwords.  We have procured a sorted list of common passwords common.txt (posted on the class resource page)


1. First, change all capital letters in the users password to lower case letters.

You should use the binary search algorithm we discuss in class to search whether the user's password is on the list of common passwords or not.
 
Please output the total number of times your algorithm makes a comparison between the user's password and an entry on the list of common passwords. What is the relationship between this number and the size of the list?

(Extra credit:  convert your binary search to a recursive algorithm e.g., search(value, high_index, low_index).)

Please extensively test your assignment.  When it is complete, put it in a script named hw2.USERID.py.  Write a document (acceptable formats include pdf and text files) explaining how you tested your program (what test cases and strategies did you use) as hw2-test.USERID.txt or hw2-test.USERID.pdf.  Upload these files using the file upload tool available at https://www.ischool.berkeley.edu/uploader/?s=i206 

CITATIONS:


'''
import unittest
import re


''''''


'''
Program has 3 main functions
1. strength_checker
    returns the password strength, based on the number of conditions met when given a string(password)

2. is_common does 2 things
    a. reads the common txt file and converts it to a list
    b. Converts entered pswds to lowercase and searches in common pswds

3. search
    does a binary search given a search string and a list to search from

'''


def strength_checker(password):
    conditions_met = 0
    msg = ''
    
    #Checks the 4 conditions 
    if len(str(password)) >=6: #length
        conditions_met += 1
    if re.search('[a-z]',password) and re.search('[A-Z]',password): #atleast one upper and one lower-case letter
        conditions_met += 1       
    if re.search('[\d]',password):#atleast one digit
        conditions_met += 1
    if re.search('[^a-z^A-Z^\d]',password): #atleast one character that is not a letter/a digit
        conditions_met += 1

    #returns a message on the strength of the password
    if conditions_met == 0:
        msg = 'Your password is very weak'
    elif conditions_met == 1:
        msg = 'Your password is weak'
    elif conditions_met ==2:
        msg = 'Your password has medium strength'
    elif conditions_met ==3:
        msg = 'Your password has high medium strength'
    elif conditions_met ==4:
        msg = 'Your password is strong'       
    return msg



def search(search_text,array):
    comparisons = 0
    stop = False
    while stop == False and len(array)>0:
        mid = int((len(array)/2))
        current_node = array[mid]
        comparisons += 1
        if search_text == current_node:
            stop =  True
            return True,comparisons
        elif search_text < current_node:
            stop = False
            array = array[:(mid)] #Ignore the right side of the array           
        elif search_text > current_node:
            stop = False
            array = array[mid+1:] #Ignore the left side of the array
        else:
            stop =  True
            return False,comparisons   
    if len(array) == 0:
        return False,comparisons
    

def is_common(pswd):
    f = open('common.txt', 'r')
    common_pwds =  [e.rstrip() for e in list(f)]
    f.close()
    search_results = search (pswd.lower(),common_pwds) 
    if search_results[0] == True:
        print('Your password is very common-')
        print('Comparisons done are :' + str(search_results[1]))
    else: 
        print('Comparisons done are :' + str(search_results[1])+ '\nPassword not common.')

def password_prompter(*args):
    print('hurray!!')
    

def main():
    #Part 1: Password prompter + strength checker
    pswd = ''
    ps = str(input('Please enter  password or type \'finish\' to exit\n'))
    while ps != 'finish':
        print(strength_checker(ps))
        is_common(ps)     #Part 2: Checks if the pswd is common 
        pswd = ps
        ps = str(input('Please enter  password or type \'finish\' to exit\n'))
    return pswd




class TestPasswordStrengthChecker(unittest.TestCase):
    def test_strength_checker(self):
        f = open('test_file.txt', 'r') #reads the file and converts to a list
        test_passwords =  [e.rstrip() for e in list(f)]
        f.close()
        self.assertEqual([strength_checker(ps) for ps in test_passwords],[0,0,1,2,2,1,2,3,4])



if __name__ == '__main__':
    main()
    #    unittest.main()
   

   
