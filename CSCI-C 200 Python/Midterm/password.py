import string

def password(pw):
    specialChars = "!@#$"
    numChars = "0123456789"
    if len(pw) < 8:
        print("Password should contain at least 8 characters")
        return False
    lowCount = 0
    upCount = 0
    specCharCount = 0
    numCharCount = 0
    for i in pw:
        if i in specialChars:
            specCharCount += 1
        elif i in numChars:
            numCharCount += 1
        elif i.lower() != i:
            upCount += 1
        else:
            lowCount += 1
    if lowCount < 3:
        print("Password should contain at least 2 lowercase characters")
        return False
    if upCount < 1:
        print("Password should contain at least 1 uppercase character")
        return False
    if numCharCount < 2:
        print("Password should contain at least 2 numbers")
        return False
    if specCharCount < 1:
        print("Password should contain at least 1 of these: {}".format(specialChars))
        return False
    return True

def main():
    goodPass = False
    
    while goodPass == False:
        user_password = input("Please enter a password: ")
        if password(user_password) == True:
            print("Password {} is a valid password".format(user_password))
            goodPass = True
    pass

if __name__ == '__main__':
    print("Running `password.py` ")
    main()