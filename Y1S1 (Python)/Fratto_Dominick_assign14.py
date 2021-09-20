def silly_encrypter(input):
    # check to make sure that the input is uppercase, converted to upper at the output with make_upper
    input_check = input.isupper()
    if input_check == False:
        print("English input: ", input)
        print("This input is not all uppercase! The encryptor will now make your input uppercase.")
        print("")

    encrypt_split = input.split()
    done = ""

    # will keep going through list and encrypting until first list is empty
    while encrypt_split != []:
        pos = encrypt_split[0]
        first_letter = pos[0]
        replace = pos.replace(first_letter, "", 1)
        replace += first_letter
        replace += "IE"
        done += replace
        done += " "
        encrypt_split.remove(pos)

        if encrypt_split == []:
            is_upper = done.isupper()
            if is_upper == False:
                make_upper = done.upper()
                return print("Silly Encrypter output:", make_upper)
            else:
                return print("Silly Encrypter output:", done)

def Silly_decrypter(input):
    print("Silly Encryptor input: ", input)

    decrypt_split = input.split()
    done = ""

    while decrypt_split != []:
        pos = decrypt_split[0]
        remove_IE = pos.replace("IE", "", 1)
        letter_count = len(remove_IE)
        letter_count -= 1
        last_letter = remove_IE[letter_count]
        remove_LastLetter = remove_IE.replace(last_letter, "", 1)
        add_to_front = last_letter + remove_LastLetter

        done += add_to_front
        done += " "
        decrypt_split.remove(pos)
        if decrypt_split == []:
            return print("English Output:", done)

# assignment asks for an input of a uppercase string, the encryptor will convert strings to uppercase, the decrypter will not however.
print(silly_encrypter("mod3numlist is a test string!"))

print(Silly_decrypter("HISTIE SIIE AIE ESTTIE TRING!SIE"))
