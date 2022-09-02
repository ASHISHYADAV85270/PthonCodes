class Person:
    count=0
    def __init__(self):
        Person.count+=1
        print(f"object number {Person.count} created")
p=Person()
z=Person()