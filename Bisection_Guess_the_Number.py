print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = (low + high)//2
answer = 'b'
while answer.upper() != "C":
    print("Is your secret number ", guess, "?")
    answer = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    if answer.upper() == 'H':
        high = guess
        guess = (low+high)//2
    elif answer.upper() == 'L':
        low = guess
        guess = (low+high)//2
    elif answer.upper() == 'C':
        break
    else:
        print("Please try again.")
print("Game over. Your secret number was: ", guess)