maximum = int(input("Enter the value for the maximum number: "))
num_list = []

print("Enter a number between 1 and ", maximum, "to add")
list_append = int(input(""))
list_len = len(num_list)

if list_len < maximum and list_len >= 0:
    num_list.append(list_append)
    print(num_list)

else:
    print("invalid")
