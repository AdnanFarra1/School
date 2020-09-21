import numpy as np

def Initisialise_Stack():
    BaseOfStack = 0
    TopOfStack = -1
    SizeOfStack = 0
    stack = ["--"]*5
    for i in stack:
        print(i)
        
    print("\nStack Initialised")


print("Choose one of the following options:")
print("1) Initialise Stack")
print("2) Add a new item to the stack")
print("3) Remove an item from the stack")
print("4) Display the list")
print("5) Exit")
choice = int(input("\nPlease choose an option from 1-5\n"))
if choice == 1:
    Initisialise_Stack()
elif choice == 2:
    print("You chose 2")
elif choice == 3:
    print("You chose 3")
elif choice == 4:
    print("you choose 4")
elif choice == 5:
    print("Exiting Program...")
    quit()
else:
    print("Please choose an item from the menu above")







