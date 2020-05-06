#Create Functions
#LineNum = 2
def ReadFileLine(FileName):
    with open(FileName, 'r') as file:
        f_contents = file.read()
        #print(file.readline(LineNum)
        #print(f_contents)
        print(file.readline(2))

ReadFileLine("testfile.txt")
