
class getTheName():
    def getName(self):
        return self.__class__.__name__

c = getTheName()
print(c.getName())