## printing a sorted list of the input array of space separated numbers
in_text = input()
arr = map(int, in_text.split())
print(set(arr))
print(list(arr))
print(sorted(list(set(arr))))


##

