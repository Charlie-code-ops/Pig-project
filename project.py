knights_number = 0 

print("Lets create a knight!")
name = input("What is the knights nanme?: ")

while knights_number < 1:

    print("Their name is: " + name)
    knights_number += 1 

print("--- What would you like to update? ---")
print("1: knights name: " + name)

try:

    selection = int(input("Select your option: "))

    if selection == 1:
        name = str(input("What is their new name?: "))
        print("Your knight's new name is: " + name)
    else:
        print("--- Please select a valid option ---")    

except:
    print(" --- Try Again! --- ") 

print("Goodbye Sir " + name)    