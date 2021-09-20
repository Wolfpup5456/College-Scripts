# Write python code that asks the user to "Enter a number between 1 and 10." If the
# number is less than 1 or the number is greater than 10, tell the user "Invalid number".
# If the user enters a valid number, convert the number to a decimal number, and print
# the decimal number to the screen. (Example: if 3 were entered, 3.0 would be
# printed).

# range input, also range is a number
range = input("Enter a number between 1 and 10: ")
range = int(range)

# if the number is out of the 1 - 10 range, invalid
if (range < 1) or (range > 10):
    print('invalid number')

# print float if number is within 1 - 10
elif (range >= 1) and (range <= 10):
    print(float(range))
