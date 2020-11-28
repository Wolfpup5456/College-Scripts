numbers = [83, 21, 103, 16, -8, 71, 82, 119, -35, 28]
valid_numbers = []

# helped in the testing process, didn't hurt to leave in, also leaves the valid_numbers list sorted at the end of the program
numbers.sort()

list_len = len(numbers)

# test code, in fact most comments are test code in this program
# print(numbers)


while True:
    last = min(numbers, default=0)
    if list_len == 0:
        # print("empty list")
        break

    elif last == 0:
        # if you would like to exclude 0 from the valid_numbers list, delete or comment out line 21
        valid_numbers.append(last)
        numbers.remove(last)
        continue

    elif last > 0 and last < 100:
        valid_numbers.append(last)
        numbers.remove(last)

        # print("valid number")

        list_len = len(numbers)

        # print(list_len)
        # print(numbers)
        continue

    elif last < 0:
        numbers.remove(last)

        # print("not valid number")
        # print(list_len)
        # print(numbers)

        list_len = len(numbers)
        continue

    elif last > 100:
        numbers.remove(last)

        # print("not valid number")
        # print(list_len)
        # print(numbers)

        list_len = len(numbers)

print(valid_numbers)

valid_numbers_len = len(valid_numbers)

total = sum(valid_numbers)
print("Total:", total)

valid_numbers_average = total / valid_numbers_len
print("Average:", valid_numbers_average)
