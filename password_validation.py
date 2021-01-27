import re


def validate(passwd):
    if len(passwd) < 8:
        return("The password is not accepted")
    elif re.search('[0-9]', passwd) is None:
        return("The password is not accepted")
    elif re.search('[a-z]', passwd) is None:
        return("The password is not accepted")
    else:
        return("The password is accepted")



if __name__ == '__main__':
    passwd = input("Enter a password: ")
    validate(passwd)
