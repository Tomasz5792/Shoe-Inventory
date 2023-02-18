#=============Shoe list===========
#The list will be used to store a list of objects of shoes.
shoe_list = []


#========The beginning of the class==========
class shoe():

    def __init__(self, country, code, product, cost, quantity):
        #In this function, you must initialise the following attributes:
            #● country,
            #● code,
            #● product,
            #● cost, and
            #● quantity.
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost_pound(self):
        #Add the code to return the cost of the shoe in this method.
        return self.cost/100
        
    def get_quantity(self):
        #Add the code to return the quantity of the shoes.
        return self.quantity
        
    def __str__(self):
        #Add a code to returns a string representation of a class.
        return f"""{self.country:<20}{self.code:<15}{self.product:<25}{self.cost/100:<15.2f}{self.quantity:<15}"""
   

#==========Functions outside the class==============
def read_shoes_data(shoe_list):                 #reads data into shoe_list

    #This function will open the file inventory.txt and read the data from this file, then create a shoes object with this data
    #and append this object into the shoes list. One line in this file represents data to create one object of shoes. 
    #You must use the try-except in this function for error handling. 
    #Remember to skip the first line using your code.
    try:
        with open("inventory.txt", "r") as inventory_text:
            for line in inventory_text:
                line = line.strip("\n")
                line = line.split(",")
                #print(line)
                try:
                    shoe_list.append(shoe(line[0], line[1], line[2], float(line[3]), int(line[4])))       #Using float & int() and try: to remove first line and any other errors
                except:
                    pass

        #print(shoe_list)
        return shoe_list
    except:
        print("Error, cant find text file.")
    

def capture_shoes(shoe_list):                   #adds shoe object to shoe list
    #This function will allow a user to capture data about a shoe and use this data to create a shoe object and append this object inside the shoe list.
    
    #Variables
    country = ""
    code = ""
    product = ""
    cost = 0
    quantity = 0

    print("""------------------------------------------------------------------------------------------
Add Shoe
------------------------------------------------------------------------------------------""")
    country = input("Please enter Country: ")
    code = input("Please enter Code: ")
    product = input("Please enter Product: ")
    while True:
        try:
            cost = float(input("Please enter cost in £: "))*100
            break
        except:
            print("Input not recognised.")
    while True:
        try:
            quantity = int(input("Please enter quantity: "))
            break
        except:
            print("Input not recognised.")

    try:
        shoe_list.append(shoe(country, code, product, cost, quantity))              #Using float & int() and try: to remove first line and any other errors
        
        with open("inventory.txt", "a") as inventory_text:                          #Appending to text file
            inventory_text.write(f"\n{country},{code},{product},{cost},{quantity}")

    except:
        print("Failed to add shoe object to shoe list.")

    return shoe_list


def view_all(shoe_list):                        #prints table of shoes
    #his function will iterate over the shoes list and print the details of the shoes returned from the __str__ function. 
    #Optional: you can organise your data in a table format by using Python’s tabulate module.  Country,Code,Product,Cost,Quantity
    print(f"""------------------------------------------------------------------------------------------
View Data
------------------------------------------------------------------------------------------
{"Country":<20}{"Code":<15}{"Product":<25}{"Cost (£)":<15}{"Quantity (No.)":<15}
------------------------------------------------------------------------------------------""")

    for object in shoe_list:
        print(object)


def save_text_file(shoe_list):                  #function to rewrite text file with shoe_list

    with open("inventory.txt", "w") as inventory_text:
        
        inventory_text.write(f"Country,Code,Product,Cost,Quantity")

        for object in shoe_list:
            inventory_text.write(f"\n{object.country},{object.code},{object.product},{object.cost},{object.quantity}")


def re_stock(shoe_list):                        #function to find shoe with lowest quantity and add quantity
    #This function will find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked. 
    #Ask the user if they want to add this quantity of shoes and then update it.  This quantity should be updated on the file for this shoe.
    
    #Variables
    position = 0
    position_list = []
    lowest_quantity = 99999999999999999999

    print(f"""------------------------------------------------------------------------------------------
View Lowest Quantity
------------------------------------------------------------------------------------------""")


    for object in shoe_list:
        #print(f"{position}: {object.quantity}")        #for testing

        if object.quantity < lowest_quantity:
            lowest_quantity = object.quantity
            position_list = []
            position_list.append(position)
            
        elif object.quantity == lowest_quantity:
            position_list.append(position)

        position = position + 1

    #print(position_list)        #for testing

    for item in position_list:
        while True:
            try:
                number_to_add = int(input(f"Item {shoe_list[item].product}, {shoe_list[item].code} has a quantity of {shoe_list[item].quantity}.  Enter a number of shoes to add to the stock, enter 0 to skip: "))
                #print(number_to_add)        #for testing
                shoe_list[item].quantity = shoe_list[item].quantity + number_to_add
                break
            except:
                print("An integer must be added")

        print("------------------------------------------------------------------------------------------")

    save_text_file(shoe_list)                   #update text file

    return shoe_list


def seach_shoe(shoe_list):                      #searches for a shoe with sku
    #This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.
    
    #Variables
    code_search = ""
    position = 0
    position_list = []    
    
    code_search = input("""
------------------------------------------------------------------------------------------
Shoe search by code
------------------------------------------------------------------------------------------
Please enter a code to search for shoe.

Code: """).upper()

    for object in shoe_list:
    
        if object.code == code_search:
            position_list.append(position)

        #print(f"{position}: {code_search} {object.code}")       #for testing

        position = position + 1    
    
    #print(position_list)       #for testing

    print("------------------------------------------------------------------------------------------")

    for item in position_list:
        
        print(f"Item {shoe_list[item].product}, {shoe_list[item].code} has a price of {shoe_list[item].cost} and a quantity of {shoe_list[item].quantity}")
        print("------------------------------------------------------------------------------------------")


def value_per_item(shoe_list):                  #prints cost * quantity in table
    #This function will calculate the total value for each item.  Please keep the formula for value in mind: value = cost * quantity.  Print this information on the console for all the shoes.
    print(f"""------------------------------------------------------------------------------------------
View Data
------------------------------------------------------------------------------------------
{"Product":<25}{"Code":<15}{"Cost (£)":<15}{"Quantity (No.)":<15}{"Total Value (£)":<15}
------------------------------------------------------------------------------------------""")

    for object in shoe_list:
        print(f"""{object.product:<25}{object.code:<15}{object.cost/100:<15.2f}{object.quantity:<15}{object.cost*object.quantity/100:<15.2f}""")


def highest_qty(shoe_list):                              #find highest quantity and print sale
    #Write code to determine the product with the highest quantity and print this shoe as being for sale.
    #Variables
    position = 0
    position_list = []
    highest_quantity = 0

    print(f"""------------------------------------------------------------------------------------------
View Highest Quantity
------------------------------------------------------------------------------------------""")


    for object in shoe_list:
        #print(f"{position}: {object.quantity}")        #for testing

        if object.quantity > highest_quantity:
            highest_quantity = object.quantity
            position_list = []
            position_list.append(position)
            
        elif object.quantity == highest_quantity:
            position_list.append(position)

        position = position + 1

    #print(position_list)        #for testing

    for item in position_list:

        print(f"Item {shoe_list[item].product}, {shoe_list[item].code} has a quantity of {shoe_list[item].quantity}.  Please put on sale.")
        print("------------------------------------------------------------------------------------------")


#==========Main Menu=============
#Create a menu that executes each function above.
#This menu should be inside the while loop. Be creative!

shoe_list = read_shoes_data(shoe_list)      #reads data into shoe_list

#Variable
menu_choice = ""

while menu_choice != "q":

    menu_choice = input("""
------------------------------------------------------------------------------------------
Main Menu
------------------------------------------------------------------------------------------
What would you like to do?
View Data       -   d   Add Shoe        -   a   Find lowest     -   l       
Search by Code  -   s   Value per item  -   v   Find highest    -   h

Input: """).lower()

    print("")

    if menu_choice == "d":
        view_all(shoe_list)                         #makes shoe_list into a table

    elif menu_choice == "a":
        shoe_list = capture_shoes(shoe_list)        #adds a new shoe item to shoe_list

    elif menu_choice == "l":
        shoe_list = re_stock(shoe_list)             #finds lowest quantity


    elif menu_choice == "s":                        #searches shoe
        seach_shoe(shoe_list)

    elif menu_choice == "v":                        #searches shoe
        value_per_item(shoe_list)  

    elif menu_choice == "h":                        #finds highest quantity and prints sale
        highest_qty(shoe_list)      

    elif menu_choice == "q":
        print("------------------------------------------------------------------------------------------")
        print("Good bye")
        print("------------------------------------------------------------------------------------------")  

    else:
        print("Input not recodnised.")


    



