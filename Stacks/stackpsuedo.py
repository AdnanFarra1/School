NullPointer = -1
MaxStackSize = 8
Stack = ["--"]*8
print("Stack")
for i in Stack:
    print(i)

def init_Stack():
    global Top_Of_Stack
    global Base_Of_Stack
    Base_Of_Stack = 0
    print("BOS",Base_Of_Stack)
    Top_Of_Stack = NullPointer
init_Stack()

def Push():
    global Top_Of_Stack
    global MaxStackSize
    

    if Top_Of_Stack < MaxStackSize - 1:
        Top_Of_Stack += 1
        NewItem = input("Please input item ")
        Stack[Top_Of_Stack] = NewItem
    for i in Stack:
        print(i)


Push()