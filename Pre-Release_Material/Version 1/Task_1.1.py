i = 0
list = [5, 3, 4, 8, 9, 2]
search_value = int(input("Please input a search value "))
isFound = False

while i<len(list) and isFound == False:
    if list[i] == search_value:
        print("The index of search value: ", i)
        isFound = True
    else:
        i = i + 1
if isFound == False:
    print("The item is not found")