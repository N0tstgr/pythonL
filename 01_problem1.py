class TwoDVector:
    def __init__(self, x, y):
        self.u = x
        self.v = y
    def show(self):
        print(f"The vector is {self.u}i + {self.v}j")







class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super ().__init__(x, y)
        self.w = z
    def show(self):
        print(f"The vector is {self.u}i + {self.v}j + {self.w}k")

l = TwoDVector(2, 5)        
m = ThreeDVector(2, 5, 9)
l.show()
m.show()