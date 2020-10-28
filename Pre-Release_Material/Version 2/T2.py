# e.g. "description", description, "Price:", Itemprice, 


ItemDescription = input("Please enter an Item Description ")
ItemCode = input("Please enter Item Code ")
Item_Price = input("Please enter Item Price ")
NumberInStock = input("Please enter number in stock ")

print("ID", ItemDescription)
print("IC", ItemCode)
print("IP", Item_Price)
print("NIS", NumberInStock) 

line = "Item Description: " + ItemDescription + " Item Code: " + ItemCode + " Item Price: " + Item_Price + " Number in Stock: " + NumberInStock
print(line)


#Writing to the text file

FileHandle = open("Items.txt", "a")
FileHandle.write(line)
FileHandle.close()
