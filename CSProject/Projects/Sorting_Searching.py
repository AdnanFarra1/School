#Functions and classes (Structures or records) and some initializations defined right below
class Student:
    #User defined data type, in python it is called a class, same as a structure or record

    def __init__(self, Student_ID, Student_Name, Student_Score):
        self.Student_ID = Student_ID
        self.Student_Name = Student_Name
        self.Student_Score = Student_Score
    #Class method to ask user for data entry
    @classmethod
    def from_input(cls):
        return cls(
            input("Please input Student ID: "),
            input("Please input Student Name: "),
            float(input("Please input Student Score: ")),
        )
Students = []
def Score_Entry():
    No_Scores = int(input("How many scores would you like to enter? "))
    #For loop to store user inputs in an array, list in python
    for i in range(No_Scores):
        Students.append(Student.from_input())
    #Data Entry Checks
    #print(Students[0].Student_ID)
    #print(Students[0].Student_Name)
    #print(Students[0].Student_Score, "M")
def BubbleSort(Students):
    indexing_length = len(Students) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if Students[i].Student_Score > Students[i+1].Student_Score:
                sorted = False
                #Swaps index values together if i value is greater than i + 1 value
                Students[i], Students[i+1] = Students[i+1], Students[i]
    return Students
def InsertionSort(Students):
    indexing_length = range(1,len(Students))
    for i in indexing_length:
        value_to_sort = Students[i].Student_Score

        while Students[i-1].Student_Score > value_to_sort and i > 0:
            Students[i], Students[i-1] = Students[i-1], Students[i]
            i = i - 1
    return Students


position = -1
def Linear_Search(Students, Search_Value):
    i = 0
    while i < len(Students):
        if Students[i] == Search_Value:
            globals() ["position"] = i
            print("Func Called")
            return True
        i += 1
    return False








print("1) Enter Student Scores")
print("2) End the program")
choice = int(input("Please choose an option from the list above: "))
if choice == 1:
    #Calling user defined data type data entry function
    Score_Entry()
    #Menu Choices
    print("1) Bubble Sort")
    print("2) Insertion Sort")
    #Menu Choices Validated to integer only as python takes any value entered as a string
    choice_2 = int(input("Please choose an option from the list above: "))
    if choice_2 == 1:
        #Calling BubbleSort function
        BubbleSort(Students)
        for i in range(len(Students)):
            print("Student ID: ",Students[i].Student_ID)
            print("Student Name: ",Students[i].Student_Name)
            print("Student Score: ",Students[i].Student_Score)
        print("1) Linear Search")
        print("2) Binary Search")
        choice_3 = int(input("Please choose an option from the list above: "))
        if choice_3 == 1:
            Search_Value = input("Please enter a Student ID to search for: ")
            Linear_Search(Students, Search_Value)

    elif choice_2 == 2:
        InsertionSort(Students)
        for i in range(len(Students)):
            print("Student ID: ",Students[i].Student_ID)
            print("Student Name: ",Students[i].Student_Name)
            print("Student Score: ",Students[i].Student_Score)
        print("1) Linear Search")
        print("2) Binary Search")
        choice_3 = int(input("Please choose an option from the list above: "))
        if choice_3 == 1:
            Search_Value = input("Please enter a Student ID to search for: ")
            Linear_Search(Students, Search_Value)


elif choice == 2:
    print("Program Ended!")
    SystemExit




