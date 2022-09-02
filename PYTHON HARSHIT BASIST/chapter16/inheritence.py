class Person:
    def __init__(self,f_name,l_name,age):
        self.firstname=f_name
        self.lastname=l_name
        self.age=age
    def person_detail(self):
        return f"{self.firstname} {self.lastname} and age : {self.age} "
    def full_data(self):
        print(f"{self.firstname} {self.lastname} and age : {self.age} ")
    
class Contact(Person):
    def __init__(self,f_name,l_name,age,phone_number,email):
        ###super method mai hmlogo kooo object pass nhu krnaa hota but in case of calling by name we require object as an argument too
        Person. __init__(self,f_name,l_name,age)
        # super(). __init__(f_name,l_name,age)
        self.phone_number=phone_number
        self.email=email
    def contact_detail(self):
        return f" phone :{self.phone_number} email: {self.email} "
    def full_data(self):
        print(f"{self.firstname} {self.lastname} and age : {self.age} phone :{self.phone_number} email: {self.email} ")

class Address(Contact):
    def __init__(self, f_name, l_name, age, phone_number, email,street,city,state):
        super().__init__(f_name, l_name, age, phone_number, email)
        self.street=street
        self.city=city
        self.state=state
    def Address_detail(self):
        return f" street:{self.street}  city:{self.city}  state:{self.state}"
    def full_data(self):
        print(f"{self.firstname} {self.lastname} and age : {self.age} phone :{self.phone_number} email: {self.email} street:{self.street}  city:{self.city}  state:{self.state} ")

p=Person("ashish","yadav",20)
# print(p.person_detail())

c=Contact("ashish","yadav",20,8954123868,"bt20ece065@gmail.com")
# print(c.contact_detail())



a=Address("ashish","yadav",20,8954123868,"bt20ece065@gmail.com","mansarover","MBD","UP")
# print(a.Address_detail())
# a.full_data()


 #y btaiga   ki kiss order mai compliler check kregaa....jhaa function milaa uskai baad it will not check 
# print(help(Address)) 
# print(Address.mro())
# print(Address.__mro__)

# Person->Contact->Address order of class inherited 
# a is a object of address,contact,person 
# c is a object of contact,person 
# p is a object of person 
# mtlb agr subclass kaa object ...parent kaa bhi object hoga


# it check that........ki object is class ka hai y nhi..it will return a boolean value 
# print(isinstance(c,Address))    
# print(isinstance(c,Contact))    

# Python issubclass() is built-in function used to check if a class is a subclass of another class or not. This function returns True if the given class is the subclass of given class else it returns False.
# Person  it is a parent class of contact and aadress....means contact and addrsss are subclass of person
# contact   it is a parent class of  aadress....means  addrsss is subclass of contact

# issubclass(subclass,parent)  #thn it will give answer true
print(issubclass(Person,Address))
print(issubclass(Contact,Address))
