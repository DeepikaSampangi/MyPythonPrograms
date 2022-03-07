import math


def paint_calc(height: int, width: int, cover: int):
    no_of_cans = (height * width) / cover
    return math.ceil(no_of_cans)


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
can_count = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"You'll need {can_count} cans of paint.")
