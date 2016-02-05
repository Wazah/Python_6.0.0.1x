low=0
high=100
ans='l'
guess=0
print('Please think of a number between 0 and 100!')
while (True):
    if(ans=='c' or ans == 'h' or ans == 'l'):
        if (ans=='c'):
            print("Game Over. Your secret nuber was: "+str(guess))
            break
        elif(ans=='l'):
            low=guess
        elif (ans=='h'):
            high=guess
        guess=(high + low)/2
        print('Is your secret number '+str(guess)+'?')
        ans=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    else:
        print('Sorry, I did not understand your input.')
        print('Is your secret number '+str(guess)+'?')
        ans=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")