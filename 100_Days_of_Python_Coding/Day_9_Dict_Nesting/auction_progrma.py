from auction_logo import logo

print(logo)
print("Welcome to Digital Auction!!!")
digital_auction = {}
while True:
    name = input("Please enter your name : ")
    bid = int(input("Enter your bid amount : $"))
    digital_auction[name] = bid
    user_resp = input("Do you want to add another bid?(yes/no): ")
    if user_resp != "yes":
        break

max_bid = 0
max_bidder = ""
for bidder in digital_auction:
    if digital_auction[bidder] > max_bid:
        max_bid = digital_auction[bidder]
        max_bidder = bidder

print(f"The heightest bidder is {max_bidder} with amount of {max_bid}")
