'''1) define 3 functions "add()","modify()" and "delete()" with just a print message.
now accept input from user as a number. if the number entered is 1, call "add()"
if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]'''
def add():
    print("Adding item...")

def modify():
    print("Modifying item...")

def delete():
    print("Deleting item...")

# Accept input from the user
user_input = int(input("Enter a number (1 for add, 2 for modify, 3 for delete): "))

# Call functions based on user input using match...case
match user_input:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
    case _:
        print("Invalid input. Please enter 1, 2, or 3.")
