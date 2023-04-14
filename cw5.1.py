class Fruit:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
class Apple(Fruit):
    def isFresh(self):
        if self.color == "red" or self.color == "green":
            return True
        else:
            return False
class Banana(Fruit):
    def isFresh(self):
        if self.color == "orange":
            return True
        else:
            return False
class Orange(Fruit):
    def isFresh(self):
        if self.color == "orange":
            return True
        else:
            return False
jablko=Apple("blue" , "0.7")
print("isFresh? "+ str(jablko.isFresh()))