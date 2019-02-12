ask = str(input("Would you like to calculate a number's factorial? Press y for yes: "))
while ask.lower() == 'y':
    n = int(input("For what number would you like to find its factorial? "))
    if n < 0:
        print("Invalid input. Game over!")
    else:
        method = str(input("Type i to use iteration, type r to use recursion: "))
        def recursfact(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n*recursfact(n-1)
        def iterfact(n):
            if n == 0:
                return 1
            for i in range(1,n):
                n *= i
            return n

        if method.lower() == 'i':
            print(n, "!  = ", iterfact(n))
    
        elif method.lower() == 'r':    
            print(n, "!  = ", recursfact(n))

        else: 
            print("Invalid input. Game over!")
    ask = str(input("Would you like to calculate a number's factorial? Press y for yes: "))
print("Have a nice day!")
    