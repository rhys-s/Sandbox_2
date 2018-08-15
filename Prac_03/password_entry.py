"""Rhys Selwyn"""
pw = str(input('Please put word'))
if len(pw) >= 6 or len(pw) <= 3:
    print('Wrong passowrd')
    pw = str(input('Please put word'))
elif len(pw) < 6 and len(pw) > 3:
    for i in range (len(pw)):
        print('*',end='')