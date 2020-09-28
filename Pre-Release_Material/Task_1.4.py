ItemDescription = ["Cornflakes", "Milk", "Coffee", "USB", "Stapler", "Calculator"]
ItemCode= [1488, 5878, 4973, 3967, 2758, 6893]
Item_Price = ["$7", "$3", "$4", "$10", "$5", "$20"]
NumberInStock = [27, 94, 120, 12, 7, 3]


Stock_Level = int(input("Please input minimum stock level "))
for i in range(0,6):

    if  NumberInStock[i] < Stock_Level:
        print("This item is below the stock level")
        print("The item code is:", ItemCode[i])
        print("The item price is:", Item_Price[i])
        print("The number in stock is:", NumberInStock[i])
        print("The item description is:", ItemDescription[i])

