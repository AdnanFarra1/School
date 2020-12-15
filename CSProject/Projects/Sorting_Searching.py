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
            int(input("Please input Student ID: ")),
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
                Students[i].Student_Score, Students[i+1].Student_Score = Students[i+1].Student_Score, Students[i].Student_Score
    return Students



def InsertionSort():
    print("Inserty")

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
    elif choice_2 == 2:
        InsertionSort()

elif choice == 2:
    print("Program Ended!")
    SystemExit




