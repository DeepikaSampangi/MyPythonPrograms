print("Welcome to the Rollercoster !!!")
ht: int = int(input("What is your height in cm ? "))

if ht > 120:
    print("You can ride with us")
    age: int = int(input("What is your age ? "))
    if age < 12:
        print("Your ticket is worth $5")
    elif age >= 12 and age <= 18:
        print("Your ticket is worth $7")
    else:
        print("Your ticket is worth $12")
else:
    print("Sorry, you have to grow taller before you ride.")
