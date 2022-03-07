from calculator_art import logo


def add(n1: int, n2: int) -> int:
    return n1 + n2


def subtract(n1: int, n2: int) -> int:
    return n1 - n2


def multiply(n1: int, n2: int) -> int:
    return n1 * n2


def divide(n1: int, n2: int) -> float:
    return n1 / n2


def calculator():
    cal_ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
    print(logo)
    num1 = float(input("What's the first number?: "))
    while True:
        print("Select the operation to be performed")
        for key in cal_ops:
            print(key)
        ops = input("Operation to be performed: ")
        cal_func = cal_ops[ops]
        next_num = float(input("What's the next number?: "))

        ans = cal_func(num1, next_num)
        print(f"{num1} {ops} {next_num} = {ans}")
        resp = input(
            "Type 'y' to continue calculating with the prev, type 'n' to start new, type exit: "
        )
        if resp == "y":
            num1 = ans
        elif resp == "n":
            calculator()
        else:
            break


calculator()
