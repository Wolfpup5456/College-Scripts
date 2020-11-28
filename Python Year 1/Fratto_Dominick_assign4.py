# monster input 1st, monster is an integer 2nd
monster = input("please input a number between 0 and 36: ")
monster = int(monster)

# is the number with in the range of 0 to 36, not needed
# if (monster >= 0) and (monster <= 36):
#     print("test")

# error handler above 36, prints impossible if exceed
if monster > 36:
    print("outside the range 0 to 36")

# 0 is purple
if monster == 0:
    print("purple")

# between range 1 - 10, even black, odd blue
if (monster >= 1) and (monster <= 10):
    if (monster % 2) == 0:
        print('black')
    else:
        print('blue')

# between range 11 - 18, even blue, odd black
if (monster >= 11) and (monster <= 18):
    if (monster % 2) == 0:
        print('blue')
    else:
        print('black')

# between range 19 - 28, even black, odd blue
if (monster >= 19) and (monster <= 28):
    if (monster % 2) == 0:
        print('black')
    else:
        print('blue')

# between range 19 - 36, even blue, odd black
if (monster >= 29) and (monster <= 36):
    if (monster % 2) == 0:
        print('blue')
    else:
        print('black')

