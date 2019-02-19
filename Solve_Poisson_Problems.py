# Solve a simple Poisson word problem. 
# There are functions in scipy.stats library, but this doesn't use those.

from math import exp
import sys
print("What kind of Poisson problem is this?")
typeofpoisson = str(input("Type me for more or equal to, le for less or equal to, m for more, l for less, e for equal: "))
if typeofpoisson == "me" or typeofpoisson == "le"or typeofpoisson == "m" or typeofpoisson == "l" or typeofpoisson == "e":
    print()
else:
    print("Bad input. Goodbye!")
    sys.exit()
givensize = float(input("What is your specified time interval length or given group size? "))
unitvalue = float(input("What is the usual unit value? As in, blank times per unit. Solve algebraically if needed. Use decimals. "))
notthatlambda = givensize*unitvalue
desiredevent= int(input("What is the event frequency you are seeking, in reference to the more/less/equal requirement? Whole number only. This is discrete probability, after all! "))
def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
def donttakethepoisson(notthatlambda, desiredevent, typeofpoisson):
    result = 0
    sum = 0
    if typeofpoisson == 'e':
        result = notthatlambda**desiredevent * exp(-notthatlambda) / factorial(desiredevent)
    elif typeofpoisson == 'me':
        for num in range(desiredevent):
            sum += notthatlambda**num * exp(-notthatlambda) / factorial(num) 
        result = 1 - sum
    elif typeofpoisson == 'le':
        for num in range(desiredevent+1):
            result += notthatlambda**num * exp(-notthatlambda) / factorial(num)  
    elif typeofpoisson == 'm':
        for num in range(desiredevent+1):
            sum += notthatlambda**num * exp(-notthatlambda) / factorial(num) 
        result = 1 - sum
    elif typeofpoisson ==  'l':
        for num in range(desiredevent):
            result += notthatlambda**num * exp(-notthatlambda) / factorial(num) 
    return result
print()
print("This is your probability: ", round(100*donttakethepoisson(notthatlambda, desiredevent, typeofpoisson),2), "%.")
