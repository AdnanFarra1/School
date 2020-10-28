#Searching for multiple instaces
ItemDescription = [1,2,3,4,5,9,7,8,9,10]
is_found = False

search_value = int(input("Please input a search value: "))
for i in range(0,9):
   
    if ItemDescription[i] == search_value:
        print("The index of search value: ", i)
        is_found = True
    elif i == 9 & is_found == False:
        print("The item is not found")


    




