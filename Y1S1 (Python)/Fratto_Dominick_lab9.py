def is_equal(num_1, num_2):
    global x
    if num_1 == num_2:
        x = True
    else:
        x = False

is_equal(1, 1)

if x == True:
    print("equal")

else:
    print("not equal")
