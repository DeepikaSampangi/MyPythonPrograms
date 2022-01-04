def greet():
    print("Hello Universe")
    print("How is it going?")


greet()


def greet_with_name(name: str):
    print(f"Hello {name}")
    print("How is it going?")


greet_with_name(name="Universe")
greet_with_name(name="milkyway")
