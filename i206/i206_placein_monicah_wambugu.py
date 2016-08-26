
#returns true if a number is an integer or a float
def is_int_or_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

'''
Read all characters in the string that are integers or floats
first_characters('3garbage')   returns 3
first_characters('3.05garbage')   returns 3.05
first_characters('3.55.4433')   returns 3.55
first_characters('34444')   returns 34444
first_characters('555 444')   returns  555
first_characters('555 ')   returns  555 

first_characters('gdgdgd')   returns  empty
first_characters('-999')   returns  empty


'''
def first_characters(ln):
    end = 0
    first_characters = ''
    allowed_decimals = 0
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
        return True,len(fc)
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
            if first_check(x) == 'string':
                #do the 2nd check
                sc = second_check(x)
                if sc[0]:
                    if third_check(x,sc[1]):
                        print (str(x) +' to the mean!!!')
                        valid_numbers.append(float(x))
                        exit
                    else:
                        print ('Though string starts with integer it is not a valid integer/float')
                else:
                    print('Likely to be a string with text characters')
            else: #is a +/-ve integer
                if float(x) >0:
                    print (str(x) +' to the mean!!!')
                    valid_numbers.append(float(x))
                else:                    
                    others = other_numbers(x)
                    if others == 'Terminator':
                        stop = True
                        print('terminator')
                    else:
                        print('Other negative invalid numbers-ignore this')
        return valid_numbers

def mean(my_list):
    my_sum = float(sum(my_list))
    mean = float(my_sum/len(my_list))
    return mean



#print(validate(['-999']))
#print(validate(['3','3.05','3garbage','hdhdgdggd','555','563 ','3.5.3']))
print(mean([3.0, 3.05, 555.0, 563.0]))

#print(first_check('3garbage'))













#If the line begins with a real number or integer followed by a space, use that value and ignore the rest of whatever is on that line.
#Real numbers include integers,floats/fractions




'''
if len(first_characters('2222hdhhd')) == 0:


1.read a file called rainfall.txt (assumed to be in the current directory the program is running in).
rainfall.txt consists of a list of real numbers or integers that represent rainfall observed on different days (one number per line).

If the line begins with a real number or integer followed by a space, use that value and ignore the rest of whatever is on that line.
The list ends when the file ends or when the number -999 appears on a line -- whichever comes first!

Your task is to take the non-negative numbers (negative numbers are a mistake) and average them to come up with the average rainfall. You should output

Average rainfall = X inches

or an appropriate error message

This problem is trickier than it seems. Your program should be robust even when the input is not in the form expected. Here are some examples




#1.Read the file

f = open('rainfall 1.txt', 'r')
#print(list(f))

for line in f:
    print(line)
print(f.size())
#2.Clean the data

#3. Output the mean





'''



















