# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
small = 15
medium = 20
large = 25
small_pepperoni = 2
med_large_pepperoni = 3
cheese = 1
total_amt = 0
if size == "S":
    total_amt += small
elif size == "M":
    total_amt += medium
elif size == "L":
    total_amt += large

if add_pepperoni == "Y":
    if size == "S":
        total_amt += small_pepperoni
    else:
        total_amt += med_large_pepperoni

if extra_cheese == "Y":
    total_amt += cheese

print(f"Your final bill is : ${total_amt}")
