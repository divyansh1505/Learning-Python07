# class Class:
#     a=1 
#     def show(self):
#         print(f"Class attribute is {self.a}")

# e = Class()
# e.a = 45    #(agar yaha e.Class likhta to bhi 45 aata)

# e.show()
        #    - obviously this will print 45 and not 1

class Class:
    a=1 
    @classmethod   #class decorator
    def show(cls):
        print(f"Class attribute is {cls.a}")

e = Class()
e.a = 45 
e.show()