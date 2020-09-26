import numpy as np
Stack_Pointer = -1
BaseOfStack = 0
TopOfStack = -1
stack = ["--"]*5
stack_size = 5

for i in stack:
    print(i)
print("\nStack Initialised")

#def Initisialise_Stack():
#    Stack_Pointer = -
#    BaseOfStack = 0
#    TopOfStack = -1
#    stack = ["--"]*5
#    stack_size = 5
#
#for i in stack:
#    print(i)
#print("\nStack Initialised")



def Push_Stack():
    global Stack_Pointer
    while Stack_Pointer < stack_size:
        

        print("Stack has Space")
        print("Stack Pointer = ",Stack_Pointer)
        Value_to_enter = input("Please input the value you would like to enter\n")
        print(Value_to_enter)
        Stack_Pointer = Stack_Pointer + 1
        stack[Stack_Pointer] = Value_to_enter
        Stack_Pointer += 1

        for i in stack:
            print(i)

    else:
        print("False")
    










print("Choose one of the following options:")
print("1) Initialise Stack")
print("2) Add a new item to the stack")
print("3) Remove an item from the stack")
print("4) Display the list")
print("5) Exit")
choice = int(input("\nPlease choose an option from 1-5\n"))
if choice == 1:
    print("1")
    #Initisialise_Stack()
elif choice == 2:
    Push_Stack()
elif choice == 3:
    print("You chose 3")
elif choice == 4:
    print("you choose 4")
elif choice == 5:
    print("Exiting Program...")
    quit()
else:
    print("Please choose an item from the menu above")







