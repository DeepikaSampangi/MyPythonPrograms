def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)


input_num = int(input("Enter a number"))
print(f"Factorial of {input_num} is {factorial(input_num)}")
