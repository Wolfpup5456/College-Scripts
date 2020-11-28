# feet to inches
def convert_in_ft():
    num_input = int(input("enter the number of feet: "))
    sol = (num_input*12)
    print("")
    print("there are", sol, "inches in", num_input, "feet")

# feet to yards
def convert_ft_yd():
    num_input = int(input("enter the number of feet: "))
    sol = (num_input // 3)
    print("")
    print("there are", sol, "yards in", num_input, "feet")

# miles to yards
def convert_mi_yd():
    num_input = int(input("enter the number of miles: "))
    sol = (num_input * 1760)
    print("")
    print("there are", sol, "yards in", num_input, "miles")

# miles to feet
def convert_mi_ft():
    num_input = int(input("enter the number of miles: "))
    sol = (num_input * 5280)
    print("")
    print("there are", sol, "feet in", num_input, "miles")

# whole menu
print("""Conversion Menu:

1. Convert feet to inches
2. Convert yards to feet
3. Convert miles to yards
4. Convert miles to feet
5. Exit
""")

# menu item input
menu_selection = int(input("Please choose a menu option: "))

# menu items results
if menu_selection == 1:
    convert_in_ft()
    print("")
    print("goodbye")

elif menu_selection == 2:
    convert_ft_yd()
    print("")
    print("goodbye")

elif menu_selection == 3:
    convert_mi_yd()
    print("")
    print("goodbye")

elif menu_selection == 4:
    convert_mi_ft()
    print("")
    print("goodbye")

elif menu_selection == 5:
    print("goodbye")
