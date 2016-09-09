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
    while end == 0:
        for character in ln:
            if end == 0:
                if is_int_or_float(character) :
                    first_characters = first_characters +character
                elif str(character) == '.' and allowed_decimals ==0:
                   first_characters = first_characters +character
                   allowed_decimals = 1              
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
    if is_int_or_float(ln):
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
        

def validate(ln_list):
    stop = False
    valid_numbers = []
    while stop == False:
        for x in ln_list:
            if stop ==False:               
                if first_check(x) == 'string':
                    #do the 2nd check
                    sc = second_check(x)
                    if sc[0]:
                        if third_check(x,len(sc[1])):
                            valid_numbers.append(float(sc[1]))
                            exit
                        else:
                            logging('Though '+str(x)+' starts with integer it is not a valid integer/float')
                    else:
                        logging(str(x)+' is an invalid string with text characters')
                else: #is a +/-ve integer
                    if float(x) >=0:
                        valid_numbers.append(float(x))
                    else:                    
                        others = other_numbers(x)
                        if others == 'Terminator':
                            stop = True
                        else:
                            logging(str(x)+' is an invalid negative number that is ignored')
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
    

if __name__ == '__main__':
    main('rainfall.txt')
























