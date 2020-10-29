def bubble(list):
    indexing_length = len(list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range (0, indexing_length):
            if list[i] > list[i+1]:
                sorted = False
                Temp = list[i]
                list[i] = list[i+1]
                list[i+1] = Temp
    return list
print(bubble([5,8,3,12,74,1,2,7]))