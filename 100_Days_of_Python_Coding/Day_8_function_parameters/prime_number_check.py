def is_prime(num: int):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
            if count > 2:
                return False
    return True


n = int(input("Enter a number to check if it is prime: "))
if is_prime(n):
    print(f"{n} : It's a prime number.")
else:
    print(f"{n} : It's not a prime number.")
