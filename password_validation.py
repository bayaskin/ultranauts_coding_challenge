import re


def validate(passwd, role):
    if role == 'regular':

        if len(passwd) < 8:
            return("The password is not accepted, it is not long enough")

        elif re.search('[0-9]', passwd) is None:
            return("The password is not accepted, it must have at least one number")

        elif re.search('[a-z]', passwd) is None:
            return("The password is not accepted, it must have at least one letter")

        else:
            return("The password is accepted")
    else:
        if len(passwd) < 13:
            return("The password is not accepted, it is not long enough")

        elif re.search('[0-9]', passwd) is None:
            return("The password is not accepted, it must have at least one number")

        elif re.search('[a-z]', passwd) is None:
            return("The password is not accepted, it must have at least one letter")

        elif re.search('[!@#$%^&*]', passwd) is None:
            return("The password is not accepted, it must have at least one special symbol: '!', '@', '#', '$', '%', '^', '&', or '*'")

        else:
            return("The password is accepted")




if __name__ == '__main__':
    role = input("Enter your role (regular, admin): ")
    passwd = input("Enter a password: ")
    print(validate(passwd, role))
