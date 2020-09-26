#Searching for multiple instaces
ItemDescription = [1,2,3,4,5,9,7,8,9,10]

search_value = int(input("Please input a search value: "))
for i in range(0,9):
   
    if ItemDescription[i] == search_value:
        print("The index of search value: ", i)




