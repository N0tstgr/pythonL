class Vector :
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result


    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"   

##testing the implementation
v1 = Vector(4,5,6)
v2 = Vector(9,8,7)
v3 = Vector(11,12,13) #same dimension vector

print(v1 + v2)  #output Vector(13, 13, 13)
print(v1 * v2) ## output 118

print(v1 + v3) #output  Vector(15, 17, 19)
print(v1 * v3) ##output 182



     
        