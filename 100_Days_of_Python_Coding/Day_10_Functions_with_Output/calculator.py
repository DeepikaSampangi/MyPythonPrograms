from calculator_art import logo

print(logo)


def add(n1: int, n2: int) -> int:
    return n1 + n2


def subtract(n1: int, n2: int) -> int:
    return n1 - n2


def multiply(n1: int, n2: int) -> int:
    return n1 * n2


def divide(n1: int, n2: int) -> float:
    return n1 / n2


cal_ops = {"+": add, "-": subtract, "*": multiply, "/": divide}

num1 = int(input("What's the first number?: "))
while True:
    print("Select the operation to be performed")
    for key in cal_ops:
        print(key)
    ops = input("Operation to be performed: ")
    cal_func = cal_ops[ops]
    next_num = int(input("What's the next number?: "))

    ans = cal_func(num1, next_num)
    print(f"{num1} {ops} {next_num} = {ans}")
    resp = input("Type 'y' to continue calculating with the prev, type 'n' to exit: ")
    if resp != "y":
        break
    else:
        num1 = ans
