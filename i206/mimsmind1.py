'''
In this version, the program generates a random number with number of digits equal to length. If the command line argument length is not provided, 
the defa8ult value is 1. Then, the program prompts the user to type in a guess, informing the user of the number of digits expected. 
The program will then read the user input, and provide basic feedback to the user. If the guess is correct, the program will print a congratulatory message 
with the number of guesses made and terminate the game. Otherwise, the program will print a message asking the user to guess a higher or lower number, 
and prompt the user to type in the next guess.

'''
import random

def main(*args):
    len_match_string = 3
    if len(args) > 0:
        len_match_string = args[0]
    print(len_match_string)


    #Generate X characters
    floor_value = "".join('0' for i in range(len_match_string))
    ceiling_value = "".join('9' for i in range(len_match_string))
    #match_string = str(random.randrange(int(floor_value), int(ceiling_value)))

    match_string = '123'
    tries = 0
    matched = 0
    max_tries = (2**len_match_string)+len_match_string
    print('the maximum number of tries is ' +str(max_tries))

    print('solution is ' + str(match_string))

    
    while matched == 0 and max_tries > tries:
        tries =tries+1
        bulls = 0
        cows = 0
        try:
            user_guess = int(input('Please guess a '+ str(len_match_string) +' digit number between '+ floor_value + ' and ' + ceiling_value +'\n'))
            user_guess = str(user_guess)
            if len(user_guess) != len_match_string:
                print ('Please enter exactly '+ str(len_match_string) +' characters')
                
            for i in range(len(match_string)):
                #right character in the right position
                if match_string[i] == user_guess[i]:
                    bulls = bulls+1
                    user_guess.pop(i)
                    match_string.pop(i) 
                elif user_guess[i] in match_string:
                    #if 
                    cows = cows +1

            print(str(bulls)+' bulls and ' +str(cows) + ' cows')

        except ValueError:
            print('\nYou did not enter a valid integer')
            exit
    if max_tries <= tries:
        print('You have run out guesses!! Sorry you lose')


if __name__ == '__main__':
    len_match_string = (random.randint(1,5))
 #   main(len_match_string)
    main(3)
