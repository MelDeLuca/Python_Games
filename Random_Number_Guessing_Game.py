from random import randint

playagain = str(input("Would you like to play a game? Type YES if yes, something else if no. "))
print()
print("If at any time you want to stop playing, type in something not requested.")
while playagain.upper() == 'YES':
    end = int(input("Enter the highest positive integer you would like to possibly guess: "))
    thenumber = randint(0,end)
    guess = int(input("Enter your guess for the Mystery Number: "))
    while guess != thenumber:
        if guess < thenumber: 
            print("Too low! Try again!")
        elif guess > thenumber: 
            print("Too high! Try again!")
        else:
            print("That wasn't a number!")    
        guess = int(input("Enter your guess for the Mystery Number: "))
        
    print("That's it! The Mystery Number is ", thenumber)
    playagain = str(input("Would you like to play again? Yes or No: "))
print("Game Over! Bye bye!")


    
