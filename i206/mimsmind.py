'''
In this version, the program generates a random number with number of digits equal to length. If the command line argument length is not provided, 
the defa8ult value is 1. Then, the program prompts the user to type in a guess, informing the user of the number of digits expected. 
The program will then read the user input, and provide basic feedback to the user. If the guess is correct, the program will print a congratulatory message 
with the number of guesses made and terminate the game. Otherwise, the program will print a message asking the user to guess a higher or lower number, 
and prompt the user to type in the next guess.

'''
import random

def main(*args):
    len_match_string = 1
    if len(args) > 0:
        len_match_string = args[0]
    print(len_match_string)


    #Generate X characters
    floor_value = "".join('0' for i in range(len_match_string))
    ceiling_value = "".join('9' for i in range(len_match_string))
    match_string = str(random.randrange(int(floor_value), int(ceiling_value)))
    tries = 0
    matched = 0

    while matched == 0:
        tries =tries+1
        try:
            user_guess = int(input('Please guess a number between '+ floor_value + ' and ' + ceiling_value +'\n'))               
            if len(str(user_guess)) != len_match_string:
                print ('Please enter exactly '+ str(len_match_string) +' characters')
            elif user_guess < int(match_string):
                print('Nice try!! You guess was a little lower that the correct answer. Try a greater number')
            elif user_guess > int(match_string):
                print('Nice try!! You guess was a little higher that the correct answer. Try a smaller number')
            elif  user_guess == int(match_string):
                print('Congratulations!! You have guessed the correct answer after only ' +str(tries) + ' tries')
                matched = 1
                return
            else:
                #not sure what other scenario exists
                print('')
        except ValueError:
            print('\nYou did not enter a valid integer')
            exit


if __name__ == '__main__':
    len_match_string = (random.randint(0,5))
    main(len_match_string)


