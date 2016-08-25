'''
the program generates a random number with number of digits equal to length. If the command line argument length is not provided, the default value is 3.
This means that, by default, the random number is in the range of 000 and 999. 

The program will establish a maximum number of rounds, maxrounds, equal to (2^length) + length. 

The program prompts the user to type in a guess, informing the user of the number of digits expected.
The program will then read the user input, and provide 'bulls and cows' feedback to the user.A matching digit in the correct position will result in a 'bull',
while a matching digit in the wrong position will result in a 'cow'. 
At each round, if the user guess is incorrect and maxrounds is not yet reached, the program should increment the counter for round and issue a new prompt for user input.
Otherwise, the program should print a congratulatory or an apologetic message with the number of guesses made, and terminate the game.

'''
import random


def bulls_and_cows(user_guess,match_string):
    bulls = 0
    cows = 0
    to_pop=[]
    #right character in the right position
    for i in range(len(match_string)):
        try:
            if match_string[i] == user_guess[i]:
                bulls = bulls+1
                to_pop.append(i)
        except IndexError:
            pass
    if to_pop:
        count = 0
        for index in to_pop:
            user_guess.pop(index-count)
            match_string.pop(index-count)
            count = count+1

    #right character in the wrong position
    for x in range(len(user_guess)):
        if user_guess[x] in match_string:
            cows = cows +1
            #print('\n Moooh for cow.')
    return bulls, cows


def get_user_input(len_match_string):
    valid =0
    user_guess = []
    guess = ''
    while valid == 0:
        g = input('Please guess a '+ str(len_match_string) +' digit number ')
        try:
            x=int(g)
            guess = str(g)
            if len(guess) != len_match_string:
                print ('Please enter exactly '+ str(len_match_string) +' characters')
            else:
                valid =1
        except ValueError:
            print('\nYou did not enter a valid integer')
        
        
    for i in guess: user_guess.append(i)
    return user_guess

def generate_match_string(ln):
    #Generate ln random characters
    match_string = []
    floor_value = "".join('0' for i in range(ln))
    ceiling_value = "".join('9' for i in range(ln))
    m = str(random.randrange(int(floor_value), int(ceiling_value)))
    for e in m: match_string.append(e)
    return match_string


    


def main(*args):
    tries = 0
    matched = 0
    len_match_string = 3
    
    if len(args) > 0:
        len_match_string = args[0]
        
    max_tries = (2**len_match_string)+len_match_string
    m_string = generate_match_string(len_match_string)
    print('Welcome!! Lets play the Mastermind game. You have '+str(max_tries)+ ' tries. Good luck!!')
    
    while tries<max_tries and matched ==0:
        tries =tries+1
        u_guess = get_user_input(len_match_string)
        if u_guess == m_string:
            matched = 1
            print('Congratulations. You got the correct answer after only ' +str(tries)+' tries')
        else:
            bc = bulls_and_cows(u_guess,m_string)
            print(str(bc[0])+' bulls, '+str(bc[1])+'cows. Try again!' )
    
    if max_tries <= tries:
        print('You have run out guesses!! Sorry you lose')



if __name__ == '__main__':
    len_match_string = (random.randint(3,5))
    main(len_match_string)

