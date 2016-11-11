'''
This program does the following:
1. Reads rainfall.txt and converts it to a list
2. Validates the elements of the list
3. Calculates the mean
4. Prints out the mean

Includes an optional log file description.log
'''

LOG_FILENAME = 'description.log'

#writes description message into logfile 
def logging(msg):
    import logging
    logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
    logging.info(msg)

    
#reads the file and converts to a list
def read_file(filename):
    f = open(filename, 'r')
    return [e.rstrip() for e in list(f)]


#returns true if a number is an integer or a float
def is_int_or_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

#returns the leading interger/float characters of a string
def first_characters(ln):
    end = 0
    first_characters = ''
    allowed_decimals = 0 #to handle strings such as 3.583.56
    #while end == 0:
    for character in ln:
        if end == 0:
            if is_int_or_float(character) :
                first_characters = first_characters +character
            elif str(character) == '.' and allowed_decimals ==0:
               allowed_decimals = 1              
               first_characters = first_characters +character
            else:
                end=1
    return first_characters


#Returns the next character after the integers or float numbers
def next_character(ln,last_index):
    try:
        #next_character = ln[len(fc)]
        next_character = ln[last_index]
    except IndexError:
        next_character = None
        
    return next_character


'''
Cleaning/validating input is done by first checking to find out if the entire string is a +/-ve integer/float or if it is a string
if the input is a number, the program separates +ve and -ve numbers, it inserts the +ves into valid_input[], it stops reading input if its -99 and it ignores the other -ves.
if the input is a string, it does a 2nd check to find out if the string has  leading characters that are real numbers or integers
if it has leading integer or float, followed by a space e.g. '2.0 jjdhdh' it 

'''

def validate(ln_list):
    stop = False
    valid_numbers = []
    #while stop == False:
    for x in ln_list:
        if stop ==False:
            firstcharacters = first_characters(x)
            if len(x) == 0: #handle blank rows
                logging(' This is a BLANK row')
            elif firstcharacters !='' or (firstcharacters ==''and x[0] == '-'): # to handle ' 2' without affecting -999
                if not is_int_or_float(x):
                    if is_int_or_float(firstcharacters):# sc[0]:
                        nc = next_character(x,len(firstcharacters))
                        if nc ==' ' or nc == None:
                            valid_numbers.append(float(firstcharacters))
                            exit
                        else:
                            logging('Though '+str(x)+' starts with integer it is not a valid integer/float')
                    else:
                        logging(str(x)+' is an invalid string with text characters')
                else: #is a +/-ve integer'
                    element = float(x) 
                    if element >=0:
                        valid_numbers.append(float(x))
                    else:                                            
                        if element == -999:
                            stop = True
                        else:
                            logging(str(x)+' is an invalid negative number that is ignored')
            else:
                logging(str(x)+'\'s character is not an integer')
    return valid_numbers
    
#calculates the mean given a list
def mean(my_list):
    my_sum = float(sum(my_list))
    if len(my_list) == 0:
        return None
    else:
        return float(my_sum/len(my_list))


def main(filename):
    
    #reads the file and converts to a list
    my_list = read_file(filename)

    #validate the resulting list above
    valid_list = validate(my_list)
    
    #pass the list for mean calculation
    average = mean(valid_list)
    if average == None:
        print('There are no valid rainfall inputs')
    else:
        print('Average rainfall = ' + str(average) + ' inches')
    

import unittest

class TestRainfallRedux(unittest.TestCase):
    def test_first_characters(self):
        self.assertEqual(first_characters('3garbage'), '3')
        self.assertEqual(first_characters('4.333 46466 22222'), '4.333')
        self.assertEqual(first_characters('g2'), '')

    def test_next_character(self):
        self.assertEqual(next_character('30garbage',2), 'g')
        self.assertEqual(next_character('4.66 43',4), ' ')
        self.assertEqual(next_character('9 hallo',1), ' ')

    def test_validate(self):
        self.assertEqual(validate(['3','4','-999','5']), [3.0,4.0])
        self.assertEqual(validate(['-999']), [])
        self.assertEqual(validate(['1','2 100','3garbage','this is some text 4','-999','5']),[1.0,2.0])
        self.assertEqual(validate(['1.2','2.2','3.2']), [1.2,2.2,3.2])
        self.assertEqual(validate(['2','-1','0','2','-2','4','-999']), [2.0,0.0,2.0,4.0])
        self.assertEqual(validate(['0']), [0])
        self.assertEqual(validate([' 2',]), []) #space and 2, invalid
        self.assertEqual(validate(['2.',]), [2.]) #valid
        self.assertEqual(validate(['2..',]), []) #invalid


    def test_mean(self):
        self.assertEqual(mean([3.0,4.0]),3.5)
        self.assertEqual(mean([]),None)
        self.assertEqual(mean([2.0,0.0,2.0,4.0]),2.0)
        self.assertEqual(mean([0]), 0)

        

if __name__ == '__main__':
    main('rainfall.txt')
    unittest.main()





'''
#Distinguishes between -ve numbers, text and -999
def other_numbers(ln):
    try:
        ln = float(ln)
        if ln<0:
            if ln == -999:
                return 'Terminator'
            else:
                return 'Invalid- negative number'
        
    except ValueError:
        return 'Invalid-possible a string'

#first check is to find out if the entire string is a +/-ve integer/float or if it is a string
def first_check(ln):
    if 
        #+/-ve integer/float
        return 'integer'
    else:
        return'string'

#second check is to find out if the string has  leading characters that are real numbers or integers
def second_check(ln):
    fc = first_characters(ln)
    if is_int_or_float(fc):
        return True,fc
    else:
        return False,None
          
#third check is to find out if the next character after the integers/floats is a space
def third_check(ln,last_index):
    nc = next_character(ln, last_index)
    if nc ==' ' or nc == None:
        return True
    else:
        return False
        
'''



















