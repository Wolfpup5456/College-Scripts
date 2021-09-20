def findAverage():
    user_input = int(input("please input a number, -1 will end the list: "))
    average_list = []
    while True:
        if user_input == -1:
            break
        elif user_input != -1:
            average_list.append(user_input)
            # print(average_list)
            user_input = int(input("please input a number, -1 will end the list: "))
            if user_input == -1:
                list_len = len(average_list)
                # print(list_len)
                sum_list = sum(average_list)
                # print(sum_list)
                average = sum_list / list_len
                return average
            else:
                continue

print(findAverage())


# Write a function called findAverage that asks the user to enter a number. The function keeps asking the user to enter a number until the user enters -1. After the user enters -1, the function returns the average of the numbers entered.

# Do NOT print from mod3numlist function. The function must return the average.

# Do NOT call the function main. Name the funciton findAverage.

# You should paste the code from your Python editor into the blank below to retain the spacing and indention.
