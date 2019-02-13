# Print all prime numbers between 1 and the number requested, inclusive 
import math
repeat = 'Y'
while repeat.upper() == 'Y':
    limit = int(input("Find all primes up to and including this number: "))
    if limit > 0:
        for i in range(2,limit+1):
            prime = True
            for j in range(2,int(math.sqrt(i)+1)):
                 if i % j == 0:
                     prime = False
            if prime:
                print(i)
    repeat = str(input("Enter 'Y' or 'y' to play again. Otherwise, you exit. "))
print("Have a nice day!")