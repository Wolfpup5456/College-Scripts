# what file should be opened
print("what file would you like to open? (exclude .txt, that will be added in. so if your file is named numbers.txt, just input numbers): ")
file_read_input = input("") + ".txt"
# input list comes from file input
input_list = []
# Target List is valid numbers
target_list = []
# Bad Numbers are invalid numbers
bad_numbers = []
# spacer
print("")



# opens .txt file and converts to a python list
file_read = open(file_read_input, "r")
line = file_read.readline().rstrip()
while line != "":
    input_list.append(line)
    line = file_read.readline().rstrip()
    # print("list written to")

# using map function to convert from strings to integers, then sorts, least to most
input_list = list(map(int, input_list))
input_list.sort()
# print("list converted")

# gets length of list, used later
list_len = len(input_list)
# print(list_len)
# print(input_list)

# this whole loop is pretty much a copy from my assignment 11 program

# this loop adds numbers to the bad numbers and target numbers lists
while True:
    last = min(input_list, default=0)

# when input list hits 0, this loop is finished
    if list_len == 0:
        # print("empty list")
        break

# 0 gets thrown out
    elif last == 0:
        input_list.remove(last)
        list_len = len(input_list)
        # print("hit 0")
        continue

# is the number between 25 and 75, if so added to target list, then removed from input list
    elif last >= 25 and last <= 75:
        target_list.append(last)
        input_list.remove(last)
        list_len = len(input_list)
        # print("valid number l 48")
        continue

# if below 25, added to bad numbers
    elif last < 25:
        bad_numbers.append(last)
        input_list.remove(last)
        list_len = len(input_list)
        # print("valid")
        continue

# if above 75, added to bad numbers
    elif last > 75:
        bad_numbers.append(last)
        input_list.remove(last)
        list_len = len(input_list)
        # print("invalid number l 62")

# results
print("target List:", target_list)
print("bad Numbers:", bad_numbers)
