#Imports
import sys

print("                                 ABC Company\n\n")

#MenuInterface Function
def MenuInterface():
    #Menu Display
    print("Please choose an item from the menu\n")
    print("1. Add a new product in the file\n")
    print("2. Search for a product using either product code, description or price\n")
    print("3. Display all products stored in the file\n")
    print("4. End the program\n")
    #User Input
    MenuChoice = input("Please enter one of the numbers in the menu above\n")
    while MenuChoice.isdigit() == False:
        print("You did not enter an integer, please enter an integer between 1 and 4\n")
        MenuChoice = input("Please enter one of the numbers in the menu above\n")
    else:
        #Conversion from string to integer in order to use comparison operators
        MenuChoice = int(MenuChoice)

        while MenuChoice > 4:
                print("\nSorry! Number {} is not in the menu, please choose a number between 1 and 4\n".format(MenuChoice))
                MenuChoice = int(input("Please enter one of the numbers in the menu above "))

            #Variable check
                '''print("You chose option number: ", MenuChoice)'''
        #Validation
        if MenuChoice == 1:
            MenuChoice1()
        elif MenuChoice == 2:
            MenuChoice2()
        elif MenuChoice == 3:
            MenuChoice3()
        elif MenuChoice == 4:
                print("Program terminated")
                sys.exit()

def MenuChoice1():
    #Data Collection and file appending

    #ProductCode
    productCode = input("Please enter a 4 digit product code\n")
    #Validation for productCode data type
    while productCode.isdigit() == False:
        print("You did not enter an integer, please enter a 4 digit integer")
        productCode = input("Please enter a 4 digit product code\n")
    else:
        CodeLen = len(str(productCode))
        while CodeLen != 4:
            print("\nYou entered {} digits, please enter 4 digits".format(CodeLen))
            productCode = int(input("Please enter a 4 digit product code\n"))
            CodeLen = len(str(productCode))
        #CodeLen Check
        '''print("CodeLen is: ", CodeLen)'''

        #ProductDescription
        productDescription = input("Please enter the product description (20 Characters Max)\n")
        while productDescription.isalnum() == False:
            print("You did not enter a string, please enter a string of 20 characters max")
            productDescription = input("Please enter the product description (20 Characters Max)\n")
        DescLen = len(productDescription)
        while DescLen > 20:
            print("\nDescription is {} characters, please enter max 20 characters".format(DescLen))
            productDescription = str(input("Please enter the product description (20 Characters Max)\n"))
            DescLen = len(productDescription)

        #ProductPrice
        productPrice = input("Please enter the product price\n")
        try:
            productPrice = float(productPrice)
        except:
            print("You did not enter an integer or a float, please enter an integer or a float")
            productPrice = input("Please enter the product price\n")
            productPrice = float(productPrice)
        product = "{} {} {}".format(productCode,productDescription,productPrice)
        #productDetails check
        '''print("The product code you entered was: ",productCode)'''
        '''print("The product description you entered was: ", productDescription)'''
        '''print("The product price you entered was: ", productPrice)'''
        '''print("The product you entered was: ", product)'''


        appendFile = open("productFile.txt", "a")
        appendFile.write("\n")
        appendFile.write(product)

        print("Product successfully added to file!")


def MenuChoice2():
    searchfile = open("productFile.txt", "r")
    searchphrase = input("Please enter your search phrase\n")
    #Search Algorithm
    for line in searchfile:
        if searchphrase in line: print("\n",line)

    searchfile.close()

def MenuChoice3():
    print("\nThis is the list of products stored\n")
    print("Code  Description  Price")
    ProductData = open("productFile.txt", "r").read()
    print(ProductData)





MenuInterface()
