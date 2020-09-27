i = 0
ItemDescription = ["Cornflakes", "Milk", "Coffee", "USB", "Stapler", "Calculator"]
ItemCode= [1488, 5878, 4973, 3967, 2758, 6893]
Item_Price = ["$7", "$3", "$4", "$10", "$5", "$20"]
NumberInStock = [27, 94, 120, 12, 7, 3]
search_value = input("Please input a search value ")
isFound = False

while i<len(ItemDescription) and isFound == False:
    if ItemDescription[i] == search_value:
        print("The Index of search value:", i)
        print("The Item Code is:", ItemCode[i])
        print("The Item Price is:", Item_Price[i])
        print("The Number In Stock is:", NumberInStock[i])
        isFound = True
    else:
        i = i + 1
if isFound == False:
    print("The item is not found")