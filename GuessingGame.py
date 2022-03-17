number =45
guess =9
counter=0
while(guess!=0):
    guess =guess-1
    counter=counter+1
    num = int(input("Guess a number"))
    if guess==0:
            print("SORRY, You have",guess,"guess left, GAME OVER")
    elif num ==45:
        print("Congratulations, you guessed correctly")
        print("It took you",counter,"guesses to complete this game.")
        break
    elif(num>=45 and num<=65):
        print("You are close,Try Again. ")
        print("WRONG ANSWER, You have",guess,"guess left")
    else:
        print("WRONG ANSWER, You have",guess,"guess left")






