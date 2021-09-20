color_list = ["Blue", "Green", "Orange",]

def list_writer(color_list):
    while color_list != []:
        first_item = color_list[0]
        file_write = open("colors.txt", "a")
        file_write.write(first_item + "\n")
        color_list.remove(first_item)

list_writer(color_list)


# Make a list with at least three of your favorite colors.
# Write a function called list_writer that accepts a list as a parameter.
# Inside the list_writer function, read the list item by item.
# Inside the list_writer function, save each item in the list to a text file called colors.txt (put one color per line in the text file).
# When you call your function, pass the list into the function as a parameter/argument.