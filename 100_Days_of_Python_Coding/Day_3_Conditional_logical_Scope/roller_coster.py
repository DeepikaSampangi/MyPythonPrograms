print("Welcome to the Rollercoster !!!")
ht: int = int(input("What is your height in cm ? "))

if ht > 120:
    print("You can ride with us")
    age: int = int(input("What is your age ? "))
    if age < 12:
        amt = 5
    elif age >= 12 and age <= 18:
        amt = 7
    else:
        amt = 12
    photo = input("Do you want a photo?(yes/no): ")
    if photo == "yes":
        print(f"Total bill: {amt+3}")
    else:
        print(f"Total bill: {amt}")
else:
    print("Sorry, you have to grow taller before you ride.")
