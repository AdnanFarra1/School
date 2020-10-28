def New_Item():
    ItemDescription = input("Please enter an Item Description ")
    ItemCode = input("Please enter Item Code ")
    Item_Price = input("Please enter Item Price ")
    NumberInStock = input("Please enter number in stock ")

    print("ID", ItemDescription)
    print("IC", ItemCode)
    print("IP", Item_Price)
    print("NIS", NumberInStock) 
    #Concatenating String
    line = "Item Description: " + ItemDescription + " Item Code: " + ItemCode + " Item Price: " + Item_Price + " Number in Stock: " + NumberInStock
    print(line)


    #Writing to the text file

    FileHandle = open("Items.txt", "a")
    FileHandle.write(line)
    FileHandle.close()

def Search_Code():
    i = 0
    Size = 6
    ItemDescription = ["Cornflakes", "Milk", "Coffee", "USB", "Stapler", "Calculator"]
    ItemCode= [1488, 5878, 4973, 3967, 2758, 6893]
    Item_Price = ["$7", "$3", "$4", "$10", "$5", "$20"]
    NumberInStock = [27, 94, 120, 12, 7, 3]
    search_value = int(input("Please input a search value "))
    isFound = False

    while i<Size and isFound == False:
        if ItemCode[i] == search_value:
            print("The Index of search value:", i)
            print("The Item Code is:", ItemCode[i])
            print("The Item Price is:", Item_Price[i])
            print("The Number In Stock is:", NumberInStock[i])
            isFound = True
        else:
            i = i + 1
    if isFound == False:
        print("The item is not found")

def Output_HigherPrices():
    Given_Price = int(input("Please enter a price: "))
    ItemDescription = ["Cornflakes", "Milk", "Coffee", "USB", "Stapler", "Calculator"]
    ItemCode= [1488, 5878, 4973, 3967, 2758, 6893]
    Item_Price = [7, 3, 4, 10, 5, 20]
    NumberInStock = [27, 94, 120, 12, 7, 3]
    for i in range(6):
        if Item_Price[i] > Given_Price:
            print("Item Description: ", ItemDescription[i])
            print(" Item Code: ", ItemCode[i])
            print("Item Price: ", Item_Price)
            print(" Number in Stock: ", NumberInStock)
            
def Search_Description():
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







# Menu Interface
print("A. Add a new stock item to the text file")
print("B. Search for a stock item with a speicifc item code")
print("C. Search for all stock items with a specific description")
choice = input("Please choose a letter from the menu ")

if choice == "A":
    New_Item()
elif choice == "B":
    Search_Code()
elif choice == "C":
    Search_Description()
elif choice == "D":
    Output_HigherPrices()
   


