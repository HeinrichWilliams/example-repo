
from tabulate import tabulate         


#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)
    
    
    def get_cost(self):
       
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost 


    def get_quantity(self):
        
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity 

    def __str__(self):
        
        '''
        Add a code to returns a string representation of a class.
        '''
        return (f"Country: {self.country}, "
                f"Code: {self.code}, "
                f"Product: {self.product}, "
                f"Cost: {self.cost}, "
                f"Quantity: {self.quantity}")
    


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
# Initialize an empty list to hold Shoe objects
shoe_list = []


#==========Functions outside the class==============
# These functions will be used to manage the shoe inventory
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        with open("inventory.txt", "r", encoding="utf-8") as file:
            # Skip header
             file.readline()
             # Read each line in the file
             for line in file:
                if line.strip():  # skip empty lines
                    try: # Split the line into components
                        # Assuming the format is: Country,Code,Product,Cost,Quantity
                        country, code, product, cost, quantity = line.strip().split(',') # Split by comma
                        shoe = Shoe(country, code, product, cost, quantity) # Create a Shoe object
                        shoe_list.append(shoe) # Append to the shoe list
                    except ValueError as e:
                        print(f"Error processing line: {line.strip()}. Error: {e}")
    except FileNotFoundError:
         print("The file inventory.txt was not found.")
    except Exception as e:
          print(f"An error occurred: {e}")


def capture_shoes():
    
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # Prompt user for shoe details
    try:
        country = input("Enter the country: ")
        code = input("Enter the shoe code: ")
        product = input("Enter the product name: ")
        cost = float(input("Enter the cost of the shoe: "))
        quantity = int(input("Enter the quantity of shoes: "))
        # Create a Shoe object and append it to the shoe list
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        print("Shoe added successfully!")
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter valid data.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all():
    
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    if not shoe_list:
        print("No shoes available.")
        return
    table = []
    # Create a table with headers
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    for shoe in shoe_list:
        # Append each shoe's details to the table
        table.append([
            shoe.country, 
            shoe.code, 
            shoe.product, 
            shoe.cost, 
            shoe.quantity
        ])
    # Print the table using tabulate
    print(tabulate(table, headers=headers, tablefmt="grid"))

def re_stock():
   
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    if not shoe_list:
        print("No shoes in inventory.")
        return

    # Step 1: Find the shoe with the lowest quantity
    lowest_shoe = min(shoe_list, key=lambda s: s.quantity)
    print("\nShoe with the lowest stock:")
    print(lowest_shoe) 

    # Step 2: Ask user if they want to restock
    try:
        choice = input("Do you want to restock this shoe? (yes/no): ").strip().lower()
        if choice == 'yes':
            add_qty = int(input("Enter quantity to add: "))
            lowest_shoe.quantity += add_qty
            print(f"Updated quantity: {lowest_shoe.quantity}")
            
            # Step 3: Update inventory.txt
            with open("c:/Users/heinrich Williams/Dropbox/private/Hyperiondev/Level 1 - Python for Data Science/M03T07 – OOP – Synthesis/inventory.txt", "w", encoding="utf-8") as file:
                # Rewriting the file, including updated quantities
                file.write("Country,Code,Product,Cost,Quantity\n")
                for shoe in shoe_list:
                    # Write each shoe's details to the file
                    file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
            print("Inventory file updated.")
        # If user does not want to restock
        else:
            print("No changes made.")
    except ValueError:
        print("Invalid input. Quantity must be a number.")
    except Exception as e:
        print(f"An error occurred: {e}")


def search_shoe():
    
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    code_to_find = input("Enter the shoe code to search for: ").strip()
    
    for shoe in shoe_list:
        if shoe.code.lower() == code_to_find.lower():
            print("Shoe found:")
            print(shoe)
            return shoe
        
    print("Shoe with that code was not found.")
    return None


def value_per_item():
   
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    print("\nTotal value per item:\n")
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} ({shoe.code}) - Value: R{value:.2f}")


def highest_qty():
   
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # Check for the maximum quantity shoes
    highest_shoe = max(shoe_list, key=lambda s: s.quantity)

    print("\nProduct for Sale:")
    print(highest_shoe)
    print("⚡ This item is now on SALE due to high stock!")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

def main_menu():
    while True: # Loop until user chooses to exit
        print("\n=== SHOE INVENTORY SYSTEM ===")
        print("1. Read shoe data from file")
        print("2. Capture a new shoe")
        print("3. View all shoes")
        print("4. Re-stock lowest quantity item")
        print("5. Search for a shoe by code")
        print("6. Show value per item")
        print("7. Show item with highest quantity (for sale)")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()
        # Process the user's choice
        if choice == '1':
            read_shoes_data()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            view_all()
        elif choice == '4':
            re_stock()
        elif choice == '5':
            search_shoe()
        elif choice == '6':
            value_per_item()
        elif choice == '7':
            highest_qty()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")
#========End of the main menu===========
# This is the entry point of the program
# It will call the main menu function to start the program
if __name__ == "__main__":
    main_menu()

