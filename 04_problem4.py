class Complex :
    def __init__(self, r ,i):
        self.r = r
        self.i = i

        def __sum__(self, c2):
            return Complex(self.r + c2.r, self.i + c2.i)
        
c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1 + c2)        


    