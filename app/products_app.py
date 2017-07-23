
import csv

data = []

file_name = "/Users/Warren/documents/crudrepository/data/products.csv"

headers = ["id", "name", "aisle", "department", "price"]
user_input_headers = [header for header in headers if header != "id"]

#def get_product_id(product): return int(product["id"])

#def auto_incremented_id():
#    product_ids = map(get_product_id, data)
#    return max(product_ids) + 1

#def read_data(file_name):
#    with open(file_name,"r") as csv_file:
#        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
#        for row in reader:
#            data.append(row)
#            print(row["id"], row["name"])

with open(file_name,"r") as csv_file:
    reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    for row in reader:
        data.append(dict(row))

other_file = "/Users/Warren/documents/crudrepository/data/writing_stuff.csv"

#to write to your same file, just change the other_file below to file_name
#example_new_product = {"id": 100, "name": "New Item"} #must be before writing, and after reading
#data.append(example_new_product)

print("\n")

row_count = len(data)

print("\n")
print("Welcome the product app (insert username here)!!!")
print("\n")
print("There are " + str(row_count) + " products in the database! Please select an operation from the following menu:")
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
function = function.title()
print("\n")

#Three quotes will give the ability to type a multi-line string into python directly (avoiding having to type all the pring and \n above) done with """

def list_products():
    print("You chose the " + function + " function! Great choice!" + "\n")
    print("THERE ARE " + str(row_count) + " PRODUCTS:")
    for p in data:
        print("+",p)
    #for row in data:
    #    print("+ {'id': '" + row["id"] + "', " + "'name': " + "'" + row["name"] + "',"+ "'aisle': " + "'" + row["aisle"] + "',"+ "'department': " + "'" + row["department"] + "'," + "'price': " + "'" + row["price"] + "'}")
        #formatting to print as example in screenshot
def show_product():
    print("You chose the " + function + " function! Great choice!" + "\n")
    product_id = input("Ok! Please specify the product's identifier:  ")
    try:
        product = [p for p in data if p["id"] == product_id][0]
    except IndexError: #Handling issue of item # entered and not recognized.
        print("ERROR: Could not find a product with the identifier", product_id + ".", "Please start over.")
        import sys
        sys.exit() #Closes the script
    print("Here you go!", "\n", product)

def create_product():
    print("You chose the " + function + " function! Great choice!" + "\n")
    print("Please specify the product's information:")
    product_name = input("    What do you want to name the new product?")
    product_aisle = input("    What aisle is the new product in?")
    product_department = input("    What department is the new product in??")
    product_price = input("    What price is the new product?")
    "CREATING YOUR NEW PRODUCT!"
    new_product = {
    "id": len(data) + 1,
    "name": product_name,
    "aisle": product_aisle,
    "department": product_department,
    "price": product_price,
    }

    print("New product is", new_product)
    data.append(new_product)

def update_product():
    print("You chose the " + function + " function! Great choice!" + "\n")
    product_id = input("Ok. What is the product's ID? ")
    try:
        product = [p for p in data if p["id"] == product_id][0]
    except IndexError: #Handling issue of item # entered and not recognized.
        print("ERROR: Could not find a product with the identifier", product_id + ".", "Please start over.")
        import sys
        sys.exit() #Closes the script
    print("Ok. Please provide the product's information...")
    for header in user_input_headers:
        product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
    print("Updating Product To:", product)


def destroy_product():
    print("You chose the " + function + " function! Great choice!" + "\n")
    product_id = input("Ok. What is the product's ID? ")
    try:
        product = [p for p in data if p["id"] == product_id][0]
    except IndexError: #Handling issue of item # entered and not recognized.
        print("ERROR: Could not find a product with the identifier", product_id + ".", "Please start over.")
        import sys
        sys.exit() #Closes the script
    print("DESTROYING the product: ", product)
    del data[data.index(product)]


if function == "List": #using title function in case someone inputs 'list'
    list_products()
elif function == "Show":
    show_product()
elif function == "Create":
    create_product()
elif function == "Update":
    update_product()
elif function == "Destroy":
    destroy_product()
else:
    print("YOU HAVE CHOSEN AN UNRECOGNIZED OPERATION. Please choose one of: 'List', 'Show', 'Create', 'Update', or 'Destroy'.")


print("\n")

#OVERWRITING INVENTORY CSV FILE
with open(file_name, "w") as csv_file2:#NEED TO UPDATE FILE NAME TO ORIGINAL FILE FOR CREATE TO WORK
    writer = csv.DictWriter(csv_file2, fieldnames=["id", "name", "aisle", "department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in data:
        writer.writerow(product)





#print(len(p))
