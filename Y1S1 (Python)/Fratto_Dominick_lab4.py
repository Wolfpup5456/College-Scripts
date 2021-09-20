# speed input, also speed is and integer
speed = input("input a number: ")
speed = int(speed)

# range check, 0 to 200
if (speed >= 0) and (speed <= 200):
    print("the number is valid")

# is the input outside of 200
if speed > 200:
    print("the number is not valid")
