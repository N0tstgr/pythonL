class TwoDVector:
    def __init__(self, i, j):
       self.i = i
       self.j = j


class ThreeDVector:
    def __init__(self, i, j, k):
      super().__init__(i, j)
      self.k = k
    

o = TwoDVector(3, 7) 
p = ThreeDVector(3, 7, 9)   

