# didn't have to define this whole statement, was trying something more complicated that didn't work out, decided to keep it. works perfectly fine
def name_input():
    name = input("Enter a username that has only alphabetical characters and is between 5 and 10 characters: ")
    name_len = len(name)
    name_bool = name.isalpha()

    # test code
    # print(name.isalpha())
    # print(name_len)

    # does the name length field have a number, it should because of name_len
    while name_len >= 0:

        # names like "Jacob" will go through, prints accepted, range 5 to 10
        if 5 <= name_len <= 10 and name_bool == True:
            print("Username accepted.")
            break

        # if the username is not within the range of 5 to 10, or does not have letters in the "name" field, will run this loop (reruns the first half of the code)
        elif name_len <= 4 or name_len > 10 or name_bool == False:
            print("Invalid username! Please try again.")
            print("")
            name = input("Enter a username that has only alphabetical characters and is between 5 and 10 characters: ")
            name_len = len(name)
            name_bool = name.isalpha()
            if 5 <= name_len <= 10 and name_bool == True:
                print("Username accepted.")
                break
            else:
                continue


# runs the whole stack defined above
name_input()
