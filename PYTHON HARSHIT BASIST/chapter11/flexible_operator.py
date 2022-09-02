#star   * operator
# *args
#$$$$$$$$$$$args mai value as a tuple jaigi 
# def add(a,b):
#     total=a+b
#     return total
# print(add(5,7))
# print(add(5,7,12,4)) # y error dega too iss conditions sai bchnai kai liye *operator use hot hai
#TypeError: add() takes 2 positional arguments but 4 were given 

# def add(*args):
#     total=0
#     for num in args:
#         total+=num
#     return total

# print(add(5,7,12,4))    
# print(add(5,7,12,4,7,4,6,3,6))    



# args and normal para
# def mul(num,*args):
#     print(num)
#     print(args)

# def mul(*args,num):  #it is wrong format 
    # print(num)
    # print(args)


# mul(2,4,6,34,3)  #2 num kaa aur bcha hua args kaa




# args as a argument 
# def hel(*args):
#     print(args)

# num=[1,4,6,7,8]
# hel(*num)  # use operator for both tuple as well as list ..it unpack them







#kwargs (keyword argument )
#kwargs (double star operator )
#it take input as dict

# def dat(**kwargs):
#     for i,j in kwargs.items():
#         print(f"{i} : {j}")

# dat( names ='ashihs', age=20) 


# user_info={
#     "fname":"ashish",
#     "lname":"yadav",
#     "contact":8527086883,
#     "age":21,
#     "fav_person":["virat","MSD"]
# }
# #dict unpacking
# dat(**user_info)



#if all functions are used to gether then we use PADK order
#parameter 
#args
#default parameters
#kwargs
# def data(name,*args,lname="yadav",**kwargs):
#     print(name)
#     print(args)
#     print(lname)
#     print(kwargs)

# data("ashish",1,2,3,mother="savita ",father="vijay")