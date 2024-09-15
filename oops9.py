class TwoDvectors :
    def __init__ (self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"Given vectors are {self.i}i and {self.j}j ") 

class ThreeDvectors(TwoDvectors) :   #(inheritance)
    def __init__ (self, i, j, k):
        super().__init__(i,j)   #i aur j ki value parent class se leli
        self.k = k 
    def show(self):
        print(f"Given vectors are {self.i}i and {self.j}j and {self.k}k ") 


x = int(input("Value of x : "))
y = int(input("Value of y : "))
z = int(input("Value of z : "))

a = TwoDvectors(x, y)  #parethesis me jo daloge vo self me jayega
b = ThreeDvectors(x, y, z)

a.show()
b.show()