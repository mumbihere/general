
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
    if is_int_or_float(ln):
        return ln
    else:
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
def next_character(ln):
    fc = first_characters(ln)
    if is_int_or_float(fc):
        try:
            next_character = ln[len(fc)]
        except IndexError:
            next_character = None
            
        return next_character

def valid_number(ln):
    nc = next_character(ln)
    if nc ==' ' or nc == None:
        return True
    else:
        return False
        

#Distinguishes between -ve numbers, text and -999
def other_numbers(ln):
    try:
        x = is_int_or_float(ln)
        print(x)
        if x:
            ln = float(ln) 
            if ln<0:
                if ln == -999:
                    return 'Terminator'
                else:
                    return 'Invalid- negative number'
        
    except ValueError:
        return 'Invalid-possible a string'


print(other_numbers('gdgdgdgd'))
print(other_numbers('-12'))
print(other_numbers('-999'))


        
'''
print( '3garbage'+ ' '+str(valid_number('3garbage')))
print('3.05garbage'+ ' '+str(valid_number('3.05garbage')))
print('3.55.4433'+ ' '+str(valid_number('3.55.4433')))
print('34444'+ ' '+str(valid_number('34444')))
print('3.667'+ ' '+str(valid_number('3.667')))


print('555 444'+ ' '+str(valid_number('555 444')))
print('555 '+ ' '+str(valid_number('555 ')))

'''












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



















