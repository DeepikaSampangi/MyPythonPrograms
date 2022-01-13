class User:
    def __init__(self, seats):
        # initialize the attributes
        # self.seats = seats
        print("Init")

    def access(self):
        print(self.seats)


user_1 = User(seats=10)
user_1.access()
# user_1.id = "001"
# user_1.username = "Deepika"

# print(user_1.username)
