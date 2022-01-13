## Class Creation
class User:
    pass


user_1 = User()


## Class creation with init
class User:
    def __init__(self, seats):
        # initialize the attributes
        self.seats = seats
        print(self.seats)


user_1 = User(seats=10)

## Class Creation with methods accessing init variables
class User:
    def __init__(self, seats):
        # initialize the attributes
        print("init")

    def access(self):
        print(self.seats)  # AttributeError 'User' object has no attribute 'seats'
        # print(seats) Error no such variable defined in method


user_1 = User(seats=10)
# user_1.access()  ## Thorws an AttributeError

## Class method tries to access var from another method
class User:
    def __init__(self, seats):
        # initialize the attributes
        self.seats = seats

    def access(self):
        print(self.seats)
        self.new_var = 10
        another_var = 4

    def access_new_var(self):
        self.access()
        print(self.new_var)
        # print(self.another_var) Throws Attribute Error'User' object has no attribute 'another_var'


user_1 = User(seats=10)
user_1.access_new_var()
