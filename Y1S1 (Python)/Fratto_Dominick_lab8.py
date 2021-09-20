# initial input
word_input = input("please input a word: ")

# tells the user what they input
print ("you input: ", str(word_input))

# puts the input into a list, then splits it into letters
split = list(word_input)
list_add = str(split)
# test code, outputs the list
# print(list_add)

# outputs a,e,i,o,u totals
a = list_add.count("a")
e = list_add.count("e")
i = list_add.count("i")
o = list_add.count("o")
u = list_add.count("u")

# prints the totals
print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)
