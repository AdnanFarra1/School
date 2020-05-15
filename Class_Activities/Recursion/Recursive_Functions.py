#Imports

def factorialFunction():
    
    num = int(input("Please enter a number to find it's factorial\n"))
    def factorial(x):
        if x == 1:
            return 1
        else:
            return(x*factorial(x-1))

    print(factorial(num))

factorialFunction()

word = input("Please enter a word")
def letters(word):