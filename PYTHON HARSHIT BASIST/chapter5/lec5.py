#list---->collection of items of different or similar type
#list are mutable 
#string are immunatble
uname=input("enter you first name and last name separated by comma").split(",")
print(uname)
# numbers=[1,2,3,4,5]
# print(numbers)
# print(numbers[3])


# word=[1,"two","three",'four',5,7]
# print(word)
# print(word[1])
# word[3]='akkk' #********it is not possible in the case of simple string
# print(word)
# print(word[0:4:2]) #slicing also possible

#it will throw error
# user="ashisjd"
# user[2]="m"
# print(user)



# tray=[1,5,9,2,6,"tro",'signme']
# # tray[1:5]="two"  #ek character ek place koo diya jaiga 
# tray[1:3]=["hello","ashihs"]
# print(tray)


# #****compare two list 
# num1=[1,2,3,4]
# num2=[1,2,3,4]
# num3=[7,2,3,4]

# is operator also compare the adrees in the case of list 
# print(num1 is num2)  # it will give false bec it also compare memory adress of object too
# print(num1 == num2)
# print(num1 == num3)





#useful functions used for a list 
# list=[1,2,3,4,5,"mango",5,"grapes"]
# 1 count 
# print(list.count(5))  #similar as used i string

# 2 clear
# list.clear() #it will empty our list
# print(list)

# 3 sort method
# names=["ashi","palak","tany","manu","shask"]
# names.sort()   # y actual mai alphabatical order mai sort krdega
# print(names)

# 4 sorted function   ...... y actual mai change nhi krega list koo
# print(sorted(names))

# 5 copy method
# name_copy=names.copy()
# print(name_copy)

#6 reverse   ... it return none but it reverse the list actually
# names.reverse()
# print(names)


#7 how to add data to the list    append,insert,extend 
# cars=["santro","alto","maruti"]
# # cars.append("bullet") # it will add it to the end only
# cars.insert(1,"hello") #specific position pai add krle kai liye
# print(cars)


#8 how to add two merge 
# num1=["one ","two","3"]
# num2=["four","5","six"]
# num=num1+num2
# print(num)

#9 how to add within a list 
# num1.extend(num2)  ##normally ismai chla jaiga
# num1.append(num2)  #list inside another list   mtlb as a single element of type list add hoga y
# print(num1) 


#10 how to delete data from list      pop,del,remove
# numbers=[1,2,3,4,5,"mango","grapes"]
 #pop method
 # numbers.pop()
# numbers.pop(2)


#del operator
# del numbers[4]


#remove method
# numbers.remove("mango")  # agr y list mai multiple huai too sbsai phle bala delete hoga bs....aur agr hua hi nhi too error aayga
# print(numbers)


# 11 convert string to list
# name="ashish  yadav".split()
# name2="manu,yadav".split(",")
# print(name)
# print(name2)

# 11 convert list to string  
# user=["hello","beta"]
# print(",".join(user))

##12 min and max function
# num=[2,3,9,4,2,6,3,29,12]
# print(min(num))
# print(max(num))

# #****2D list
# list=[[1,2,3],[4,5,6,],[7,8,9]]
# for sub in list:
#     for i in sub:
#         print(i,end =" ")


 