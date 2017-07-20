
import csv

data = list()

file_name = "/Users/Warren/documents/crudrepository/data/products.csv"

def read_data(file_name):
    with open(file_name,"r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            data.append(row)
            print(row["id"], row["name"])


with open(file_name,"r") as csv_file:
    reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    for row in reader:
        data.append(row)

other_file = "/Users/Warren/documents/crudrepository/data/writing_stuff.csv"

#to write to your same file, just change the other_file below to file_name
#example_new_product = {"id": 100, "name": "New Item"} #must be before writing, and after reading
#data.append(example_new_product)

#with open(other_file, "w") as csv_file2:
#    writer = csv.DictWriter(csv_file2, fieldnames=["id", "name", "aisle", "department","price"])
#    writer.writeheader() # uses fieldnames set above
#    for product in data:
#        writer.writerow(product)


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

#print("You chose the " + function + " function! Great choice!")



#Three quotes will give the ability to type a multi-line string into python directly (avoiding having to type all the pring and \n above) done with """

def list_products():
    read_data(file_name)

def show_product():
      print("You chose the " + function + " function! Great choice!")
def create_product():
      print("You chose the " + function + " function! Great choice!")
def update_product():
      print("You chose the " + function + " function! Great choice!")
def destroy_product():
      print("You chose the " + function + " function! Great choice!")

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
    print("YOU HAVE CHOSEN AN Unrecognized Operation. Please choose one of: 'List', 'Show', 'Create', 'Update', or 'Destroy'.")


print("\n")








#print(len(p))
