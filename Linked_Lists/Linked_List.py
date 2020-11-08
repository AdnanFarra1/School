#Constants
NullPointer = 0
#Arrays
Nodes_Array = []
class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

def InitialiseList():
    StartPointer = NullPointer
    FreeListPointer = 1
    for i in range(1,7):
        Nodes_Array[i].pointer = i + 1
    Nodes_Array[7].pointer = NullPointer
