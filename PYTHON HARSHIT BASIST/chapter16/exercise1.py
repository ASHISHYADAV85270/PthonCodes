class Laptop:
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
        self.laptopspecs=name +brand

l=Laptop("hp","legion",96000)
print(l.laptopspecs)
