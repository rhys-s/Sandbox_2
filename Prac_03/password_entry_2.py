MINIMUM_LENGTH = 4
MAX_LENGTH = 6
"""

def main():
    pw = input("Enter password length of at least {} and max of {}: ".format(MINIMUM_LENGTH,MAX_LENGTH))
    while len(pw) < MINIMUM_LENGTH  or len(pw) > MAX_LENGTH:
        pw = input("Please Re enter a password length of at least {} and max of {}: ".format(MINIMUM_LENGTH, MAX_LENGTH))
    print('*'*len(pw))
main()
"""


def main():
    """Obtain pword and print stars"""
    pw = get_password(MINIMUM_LENGTH, MAX_LENGTH)
    asterik_print(pw)


def get_password(min_length, max_length):
    """User enters pword, checks for length standards"""
    pw = input("Enter password length of at least {} and max of {}: ".format(MINIMUM_LENGTH, MAX_LENGTH))
    while len(pw) < min_length or len(pw) > max_length:
        print('Password is not an appropiate length')
        pw = input("Enter password length of at least {} and max of {}: ".format(MINIMUM_LENGTH, MAX_LENGTH))
    return pw


def asterik_print(string):
    """Prints same amount of asteriks as string length"""
    print('*' * len(string))


main()
