'''
Program has 3 main functions
1. strength_checker
    returns the password strength, based on the number of conditions met when given a string(password)

2. is_common does 2 things
    a. reads the common txt file and converts it to a list
    b. Converts entered pswds to lowercase and searches in common pswds

3. search
    does a binary search given a search string and a list to search from


CITATIONS
1. http://effbot.org/tkinterbook/
2. https://docs.python.org/3/library/tk.html
3. https://www.tutorialspoint.com/python/python_gui_programming.htm
4. http://stackoverflow.com/questions/2260235/how-to-clear-the-entry-widget-after-a-button-is-pressed-in-tkinter

'''
import csv
import unittest
import re
import tkinter as tk

def strength_checker(password):
    conditions_met = 0
    msg = ''
    unmet = []
    met = []
    valid_strength_feedback = {'0': 'is very weak',
                               '1': 'is weak',
                               '2': 'has medium strength',
                               '3': 'has high medium strength',
                               '4': 'is strong'}
    
    unmet_conditions_feedback = {'length': '\n\tIt should be at least six characters',
                                 'case': '\n\tIt should have at least one uppercase and at least one lowercase letter',
                                 'digit': '\n\tIt should have at least one digit',
                                 'special': '\n\tIt should have at least one character that is not a letter or a digit'}
    met_conditions_feedback = {'length': '\n\tIt\'s at least six characters',
                      'case': '\n\tIt has at least sone uppercase and at least one lowercase letter',
                      'digit': '\n\tIt has at least one digit',
                      'special': '\n\tIt has at least one character that is not a letter or a digit'}
    #Checks the 4 conditions 
    if len(str(password)) >=6: #length
        conditions_met += 1
        met.append(met_conditions_feedback['length'])
    else:
        unmet.append(unmet_conditions_feedback['length'])
        
    if re.search('[a-z]',password) and re.search('[A-Z]',password): #atleast one upper and one lower-case letter
        conditions_met += 1
        met.append(met_conditions_feedback['case'])
    else:
        unmet.append(unmet_conditions_feedback['case'])
        
    if re.search('[\d]',password):#atleast one digit
        conditions_met += 1
        met.append(met_conditions_feedback['digit'])
    else:
        unmet.append(unmet_conditions_feedback['digit'])
        
    if re.search('[^a-z^A-Z^\d]',password): #atleast one character that is not a letter/a digit
        met.append(met_conditions_feedback['special'])
        conditions_met += 1
    else:
        unmet.append(unmet_conditions_feedback['special'])

    #returns a message on the strength of the password
 
    msg = valid_strength_feedback[str(conditions_met)]
    return conditions_met, msg,unmet,met


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
    msg = ''
    f = open('common.txt', 'r')
    common_pwds =  [e.rstrip() for e in list(f)]
    f.close()
    search_results = search (pswd.lower(),common_pwds)
    return search_results

        
class Pswd_check():
    def __init__(self):
        self.top = tk.Tk()
        self.top.minsize(width=300,height=150)
        L1 = tk.Label(master=self.top, text="Please enter  password or type \'finish\' to exit\n")
        L1.pack()
        self.create_entry_widget()
        self.password = ''
        self.top.attributes("-topmost", True)
        self.top.mainloop()

    def quit(self):
        self.top.destroy()
       
    def create_entry_widget(self):
        self.ps_widget = tk.Entry(self.top, show='*') 
        self.ps_widget.bind("<Return>", self.callback)
        self.ps_widget.pack()
        self.ps_widget.focus_set()        

    def callback(self,event):
        ps = self.ps_widget.get()
        if ps != 'finish':
            s_check = strength_checker(ps)
            no_of_met_cond = s_check[0]
            strength = s_check[1]
            unmet_cond = s_check[2]
            met_cond = s_check[3]

            print('\n\nYour password '+strength)
            if len(met_cond)>0:
                print('\nIt meets the following conditions:')
                for met in met_cond:
                    print(met)
                    
            if len(unmet_cond)>0:
                print('\nTo make it stronger, ensure it meets the following conditions')
                for unmet in unmet_cond:
                    print(unmet)
            if is_common(ps)[0] == True:#Part 2: Checks if the pswd is common 
                 print("Your password is common-\nComparisons done are :" + str(is_common(ps)[1]))
                 
            else: 
                print('\nComparisons done are :' + str(is_common(ps)[1])+ '\nPassword not common.')
            self.clear()
            self.password = ps
        else:
            print('Thank you. Adios!!')
            #print(self.password)
            self.quit()
            
    def clear(self):
        print('\n------------------------------------------')
        self.ps_widget.delete(0,'end')
       


def main():
    #Create an instance of pswd_check() that runs until terminated
    checker = Pswd_check()



class TestPasswordStrengthChecker(unittest.TestCase):
    
    #This test function uses a test file (test_file.txt) to carry out the check faster.This file needs to be saved in local directory and is include in hw2-test.monicah.wambugu.pdf
    '''
    def test_strength_checker(self):
        #Validate individual conditions and a combination of conditions
        with open('test_file.txt', newline='') as csvfile:
             spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
             for row in spamreader:
                 sc = strength_checker(row[0])
                 conditions_met = str(sc[0])
                 strength_feedback = str(sc[1])
                 self.assertEqual(conditions_met,row[1])
                 
                 #Validate whether returned conditions match return message
                 valid_strength_feedback = {
                     '0': 'is very weak',
                     '1': 'is weak',
                     '2': 'has medium strength',
                     '3': 'has high medium strength',
                     '4': 'is strong'}
                 self.assertEqual(valid_strength_feedback[conditions_met],strength_feedback )
    '''

    def test_search(self):
         #Validate Comparisons
         truesearch = search('apple',['apple','bg0od','bye','duties','Friday'])
         falsesearch = search('zucchini',['apple','bg0od','bye','duties','Friday','hood','monday'])
         self.assertEqual(truesearch[1],3)
         self.assertEqual(falsesearch[1],3)       
         #Validate return value
         self.assertTrue(truesearch[0])
         self.assertFalse(falsesearch[0])

    def test_is_common(self):
        #Validate return value
        self.assertTrue(is_common('007bond')[0])
        self.assertFalse(is_common('tH1Ka*')[0])

        

       

        


if __name__ == '__main__':
    main()
    unittest.main()
   

   
