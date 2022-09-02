import pdb #import pdb module
#it is used for debugging


#why debugging
# 1 our program is not running and causing unexpected error
# 2 our program is running but not working the same way

#steps for debugging
# 1 set trace 
# 2  execute code line by line
pdb.set_trace() # hm iski position bhi set krsktai hai
user=input("enter your name")
age=input("enter your age")
print(f"hello {user} your age is {age}")
age_new=age+5
print(f"hello {user} your age after 5 year will be {age}")



#l  to know the point of debugger 
#n to pass that line for debugging
#c  it will allow full code to debug
# q for quiting debugger



