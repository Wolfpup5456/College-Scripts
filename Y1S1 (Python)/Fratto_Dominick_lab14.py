def is_valid_email(email_address):
    if "@" in email_address and ".edu" in email_address:
        return True
    else:
        return False


print(is_valid_email("@volstate.edu"))
