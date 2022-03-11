a: list = ["key1", "key2", "key3"]

b: list = ["value1", "value2", "value3"]

z = zip(a, b)

print(f"Zip of two lists {zip(*z)}")
