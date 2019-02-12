#Find maximum of unspecified list of user-input numbers without using max function 

print("Let's calculate the maximum of a list of numbers. ")
n = int(input("How many numbers would you like to input? "))
if n >= 1:
    largest = int(input("What is the first number you would like to input? "))

    for i in range(n):
        if n == 1:
            break
        elif n < 1:
            break
        else:
            while n > 1:
                addanumber = int(input("Add a number to the list: "))
                if addanumber >= largest:
                    largest = addanumber
                    n -= 1
                else:
                    n -= 1
    print("")
    print(largest, " is the maximum. Have a nice day!")
else:
    print("Game over. That entry is invalid for this game. Have a nice day!")

  
            
            
    