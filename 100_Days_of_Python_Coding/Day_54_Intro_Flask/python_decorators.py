def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# First-class Obj, can be passed around as arguments


def calculate(cal_func, n1, n2):
    return cal_func(n1, n2)


result = calculate(multiply, 2, 3)
print(result)


# Nested funtions
def outer_func():
    print("I'm Outer")

    def nested_func():
        print("I'm Inner")

    nested_func()

outer_func()