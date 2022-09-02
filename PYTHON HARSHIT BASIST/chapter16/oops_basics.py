#we need to create a init function for class...just like constructor in c++
#class kai andr joo function hotaii hai unhai method boltai hai
# class Person:
    # def __init__(self,f_name,l_name,age): #it is instance function or dunder method or double underscore or magic method
    #     self.firstname=f_name
    #     self.lastname=l_name
#         self.age=age
#         #lhs are instance variable mtlb object kai parts
#         #here self is acting as object

# p1=Person("ashish","yadav",20) #bydefault init will be called
# print(p1.firstname) #lhs baale name use krna
# # if we want to print variable of a object
# print(p1.__dict__)



# OOP Instance Methods
#  ***********instance and object are same*********
# class Person:
#     def __init__(self,f_name,l_name,age):
#         self.firstname=f_name
#         self.lastname=l_name
#         self.age=age
    
#     def full_name(self):
#         self.fname=self.firstname + self.lastname
#         return self.fname

#     def is_not_teen(self):
#         return self.age>18    

# p1=Person("Ashish","Yadav",20)
# print(p1.is_not_teen())
# print(p1.full_name())
# Person.full_name(p1) same meaning
        

# l=[2,5,32,7]
# l.append(10)
# list.append(l,10)

# l.clear()
# list.clear(l)




# Class Variable

# class Circles:
#     pi=3.14  #it is class variable ...to use it we use classname.variblename
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return Circles.pi*self.radius*self.radius

# Circles.pi=5 #we can change frim here also



#class method  and static method
# decoder use hota hai phle define krne sai phle 

class Person:
    def __init__(self,f_name,l_name,age):
        self.firstname=f_name
        self.lastname=l_name
        self.age=age

    @classmethod
    def fullname(cls,str):     #cls is for class
        firstname,lastname,age=str.split(",")
        return cls(firstname,lastname,age)  

    @staticmethod    #without variable passing function 
    def rxxx():
        return "bina variable kai functions"
    

    @property
    def printdata(self):
        print("this is fuction is called without using brackets ()")





p1=Person("ashish","yadav",20)
print(p1.firstname) 
print(p1.printdata)

p2=Person.fullname("ashish,yadav,20")   #creating self defined constructor using class method  
print(p2.lastname)
print(p2.printdata)


print(Person.rxxx())



# _varname     for private variable but actuaaly they are not 
# __name__ dunder or magic  method 
# __name   name mangling   jiskaaa python name change krleta hai






