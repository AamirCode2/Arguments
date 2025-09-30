def factorial(x):
    '''This is a recursive function to find the factorial of an integer\n'''

    if x == 0 or x == 1:
        return 1
    else:
        #calling function inside a function
        return x*factorial(x-1)

#display result
print(factorial.__doc__)

num = int(input("Enter a number to find its factorial: "))

print("the factorial of your number: ", factorial(num))