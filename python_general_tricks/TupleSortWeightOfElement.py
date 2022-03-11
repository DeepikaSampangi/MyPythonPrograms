import time

start_time = time.time()


def sort_tuple(input_tuple):
    tuple_len: int = len(input_tuple)
    for i in range(0, tuple_len):
        for j in range(0, tuple_len - i - 1):
            if input_tuple[j][1] > input_tuple[j + 1][1]:
                temp = input_tuple[j]
                input_tuple[j] = input_tuple[j + 1]
                input_tuple[j + 1] = temp
    return input_tuple


input_tuple: list = [("b", 2), ("e", 5), ("d", 4), ("a", 1), ("c", 3)]
end_time = time.time()

print(sort_tuple(input_tuple))
print("Time taken", end_time - start_time)
