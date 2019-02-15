import random 
randnum = random.randint(1,1000000)
print("A number that is a palindrome is the same backwards and forwards.")
print("Is a random number from one up to a million a palindrome?")
thestring = str(randnum)
revstring = thestring[::-1]
print(thestring)
if thestring == revstring:
    print("This number is a palindrome.")
else:
    print("This number is not a palindrome.")
print("So what is the likelihood that a number in this range is a palindrome?")
numofpals = 0
for i in range(1,1000000):
    newstring = str(i)
    revnewstring = newstring[::-1]
    if newstring == revnewstring:
        numofpals += 1
print("There are ", numofpals, " out of a million whole numbers, so the probability ")
print("of getting a palindrome is ", numofpals, "/1000000, or ", float(numofpals*100/1000000), "%.")