# DO NOT REMOVE THIS:
def pause():
  input("Press enter to continue:")
  print()

# 1) Write a loop that prints the numbers from 3 to 9 in steps of 2.  Do it with a FOR loop.
# The output should be:
# 3 
# 5 
# 7 
# 9
print("Problem 1:") # DO NOT REMOVE THIS LINE
for v in range(3,10,2):
  print(v)
pause()             # DO NOT REMOVE THIS LINE

# 2) Write a loop that print the numbers from 9 t0 3 backwards in steps of 2.  Use a FOR loop.
# The output should be:
# 9
# 7
# 5
# 3 
print("Problem 2:") # DO NOT REMOVE THIS LINE
for t in range(9,2,-2):
  print(t)
pause()             # DO NOT REMOVE THIS LINE

# 3) Write a program that set the variable l to a list 
# containining the number 2, 4, 8, 16, and 32.  Then
# print the list in list form, them use a for loop to print
# the items in the list, one per line.
# The output should be:
# [2, 4, 8, 16, 32]
# 2
# 4
# 8
# 16
# 32
print("Problem 3:") # DO NOT REMOVE THIS LINE
l = list([2,4,8,16,32])
print(l) 
for x in range(len(l)):
  print(l[x])
pause()             # DO NOT REMOVE THIS LINE


# 4) Set a variable count to 0.  Write a WHILE loop that
# prints the value of count and then increments it by 1.
# The loop should stop when count reaches 10.  The output
# should be:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7 
# 8
# 9
print("Problem 4:") # DO NOT REMOVE THIS LINE
x = 0
while x < 10:
  print(x)
  x += 1
pause()             # DO NOT REMOVE THIS LINE


# 5) Finish the following function that takes a number and a list.
# it prints out all the values of the list multiplied by the number.
# Note that I have already added a call to the function: 
#   print_mult_vector(2, [2,4,6,8])
# The output should be:
# 4
# 8
# 12
# 16
print("Problem 5:") # DO NOT REMOVE THIS LINE
def print_mult_vector(num, vec):
  pass
  for num in range(1, 5, 1):
    print(len(vec) * num)

print_mult_vector(2, [2,4,6,8]) 

pause()             # DO NOT REMOVE THIS LINE

# 6) Write a function called mult_vector(num, vec)
# that returns a new list that is the list vec multiplied
# by num.  In other words, this function will be like
# the function in problem 5, but it will not print the
# list.  Then Call the function like so: print(mult_vector([2, [2,4,6,8])])

print("Problem 6:") # DO NOT REMOVE THIS LINE
def mult_vector(num, vec):
 my_list = vec
 multiplyfuntion = [i * num for i in my_list]
 return(multiplyfuntion)
print(mult_vector(2, [2,4,6,8]))
pause()             # DO NOT REMOVE THIS LINE

# 7) write a function that takes a string and return a list such that
# each character in the string is a character in the list, but it is the next
# character in the alphabet.
#
# For example, calling the function like so: print(make_list_enc("Hello, world"))
# prints the following:
# ['I', 'f', 'm', 'm', 'p', '-', '!', 'x', 'p', 's', 'm', 'e']
# Note that I have added a call to your function to show that it works.
#
# Note that you can use the function ord() to get the ordinal value
# (the ASCII code) of a character.  You can use the function chr() to turn an ordinal
# value back into a character.  So, for example, chr(ord('A') + 1) results in 'B',
# chr(ord('B') + 1) results in 'C', etc.

print("Problem 7:") # DO NOT REMOVE THIS LINE
def make_list_enc(phrase):
  A_list = list(phrase)
  for i in range(0,len(A_list)):
    A_list[i] = chr(ord(A_list[i]) + 1)
  return A_list
try:
  print(make_list_enc("Hello, world"))
except:
  pass
pause()                  # DO NOT REMOVE THIS LINE

# 8) Write another fuction called make make_string_dec(l) that takes a list
# and returns that list as a string. However, the string is made up of the
# previous character for each character in the list.  So, 
# print(make_list_dec(['I', 'f', 'm', 'm', 'p', '-', '!', 'x', 'p', 's', 'm', 'e']))
# results in:
# Hello,world
# Note that I have added a call to your function to show that it works.
print("Problem 8:") # DO NOT REMOVE THIS LINE
def make_string_dec(characters):
  A_list = list(characters)
  for i in range(0,len(A_list)):
    A_list[i] = chr((ord(A_list[i]) - 1))
  new_list = ""
  return new_list.join(A_list)
try:
  print(make_string_dec(['I', 'f', 'm', 'm', 'p', '-', '!', 'x', 'p', 's', 'm', 'e']))
except:
  pass