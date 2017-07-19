
import csv

print("\n")
print("Welcome the product app (insert username here)!!!")
print("\n")
print("There are X products in the database! Please select an operation:")
print("\n")
print("Operation | Description")
print("----------  -----------")
print("'List'    | Display a list of product identifiers and names.")
print("'Show'    | Show information about a product.")
print("'Create'  | Add a new product.")
print("'Update'  | Edit an existing product.")
print("'Destroy' | Delete an existing product.")
print("\n")
function = input("Please input your chosen operation:  ")
print("\n")
print("You chose the " + function + " function! Great choice!")

#Three quotes will give the ability to type a multi-line string into python directly (avoiding having to type all the pring and \n above) done with """
