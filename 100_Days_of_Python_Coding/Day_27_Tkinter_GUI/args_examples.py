def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))


def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)


calculate(2, add=2, mul=4)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
