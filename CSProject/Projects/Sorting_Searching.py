class Student:

    def __init__(self, Student_ID, Student_Name, Student_Score):
        self.Student_ID = Student_ID
        self.Student_Name = Student_Name
        self.Student_Score = Student_Score

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
    for i in range(No_Scores):
        Students.append(Student.from_input())
    print(Students[0].Student_ID)
    print(Students[0].Student_Name)
    print(Students[0].Student_Score, "M")
    #print("Student ID entered is: ",Stodent.Student_ID)
    #print("Student Name entered is: ",Stodent.Student_Name)
    #print("Student Score entered is: ",Stodent.Student_Score, "M")
def BubbleSort(Students):
    indexing_length = len(Students) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if Students[i].Student_Score > Students[i+1].Student_Score:
                sorted = False
                Students[i].Student_Score, Students[i+1].Student_Score = Students[i+1].Student_Score, Students[i].Student_Score
    return Students



def InsertionSort():
    print("Inserty")

print("1) Enter Student Scores")
print("2) End the program")
choice = int(input("Please choose an option from the list above: "))
if choice == 1:
    Score_Entry()
    print("1) Bubble Sort")
    print("2) Insertion Sort")
    choice_2 = int(input("Please choose an option from the list above: "))
    if choice_2 == 1:
        BubbleSort(Students)
        for i in range(len(Students)):
            print("Student ID: ",Students[i].Student_ID)
            print("Student Name: ",Students[i].Student_Name)
            print("Student Score: ",(Students[i].Student_Score))



    elif choice_2 == 2:
        InsertionSort()

elif choice == 2:
    print("Program Ended!")
    SystemExit




