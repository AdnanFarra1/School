Size = 10
ItemDescription = ["a", "b", "c", "a"]
SearchValue = input("Please enter a search value")
for i in range(3):
    if SearchValue == ItemDescription[i]:
        print("Item index: ", i)

