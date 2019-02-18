# Solve a simple Poisson word problem. (Strictly for those 'equal to' questions.)
# There are functions in scipy.stats library, but this doesn't use those.

import math
thistimeperiod = float(input("What is your specified time interval length? "))
normaltimeperiod = float(input("What is the usual unit time? As in, once every blank time units. "))
notthatlambda = thistimeperiod/normaltimeperiod
desiredevent= float(input("What is the event frequency you are seeking, given the specified time interval? "))
def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
def donttakethepoisson(notthatlambda, desiredevent):
        return notthatlambda**desiredevent * math.exp(-notthatlambda) / factorial(desiredevent) 
print()
print("This is your probability, in decimal form: ", donttakethepoisson(notthatlambda, desiredevent))