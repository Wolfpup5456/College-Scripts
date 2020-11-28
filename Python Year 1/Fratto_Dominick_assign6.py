# how many days / how many spots on the list will be filled, also the spots are integers
gem_days = int(input('How many days did you collect gems?: '))
# creates a list
gem_list = []

# loops how many days input, also adds input data to a list, input from user
for day in range(1, gem_days + 1):
    print('Enter the number of gems collected on day', day)
    gem_input = int(input())
    gem_list.append(gem_input)

# checks the length of the list created by user inputs, uses that later for the average
gem_list_length = len(gem_list)
# adds the list inputs together
gem_sum = sum(gem_list)

# prints the sum of the list
print("Total gems collected: ", gem_sum)

# does the average calculation and prints it
gem_average = gem_sum / gem_list_length
print("Average gems collected per day: ", gem_average)
