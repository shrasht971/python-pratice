# Write the program  accept numbers till user enters 0 and display the total of all the numbers entered.
total = 0
while True:
    num = float(input("Enter a number (enter 0 to finish): "))
    if num == 0:
        break
    total += num

print("The total of all the numbers entered is:", total)
