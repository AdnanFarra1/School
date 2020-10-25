# DECLARE ItemDescription : ARRAY[0:3] OF str
#DECLARE Size : int
#DECLARE isFound : bool
#DECLARE Searchvalue : str
#DECLARE i : int

#Main Program Starts Here
Size = 4
i = 0
isFound = False
ItemDescription = ["a","b","c","d"]
#print("List Print",ItemDescription)
Searchvalue = input("Please enter a search value ")
#print("SV", Searchvalue)
while isFound == False and i<Size:
    if Searchvalue == ItemDescription[i]:
        print("The index of the search value", i)
        isFound = True
    else: 
        i += 1
if isFound == False:
    print("The item is not found")