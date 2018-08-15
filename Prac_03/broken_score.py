def main():
    """Gets score , evaluates through other fnctn"""
    mark = float(input('Please input your total mark out of 100'))
    print(evaluate_mark(mark))


def evaluate_mark(mark):
    """ Evaluates the score given """
    if mark > 100 or mark < 0:
        return 'Please enter a valid score'
    elif mark >= 85:
        return 'Thats a hd my boi'
    elif mark >= 75:
        return 'Living that distinction life'
    elif mark >= 65:
        return 'A credit will do'
    elif mark >= 50:
        return "p's get degrees"
    else:
        return ' You have failed unluggy'


main()
