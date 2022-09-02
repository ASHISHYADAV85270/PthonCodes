class Laptop:
    def __init__(self,name,brand,price):
        self.lname=name
        self.brand=brand
        self.price=price
    def discount(self,dis):
        return self.price*(100-dis)/100

l=Laptop("hp","legion",40000)
print(l.discount(40))