class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()
print(nemo.num_eyes)
nemo.breathe()
