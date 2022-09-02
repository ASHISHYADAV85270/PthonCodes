#list comprehension sai code bhoot jada choota hojata hai..aur y python mai hii hota hai



# example1
# squares=[1,4,9,16,25,36,49,64,81,100,121]
#simple method 
# square=[]
# for i in range(1,12):
#     square.append(i**2)
# print(square)
#list comprehension method----> kya append krna hai ...fir uska way
# square=[i**2 for i in range(1,12)]
# print(square)



#example2
# names=["ashihs","uma","rann"]
# first_char=["a","u","r"]  #this we want
#simpe method
# first_char=[]
# for name in names:
#     first_char.append(name[0])
# print(first_char)

#list comprehension method----> kya append krna hai ...fir uska way
# first_char=[name[0] for name in names]
# print(first_char)





#if lc
# num=list(range(1,11))
# even_num=[i for i in num if i%2==0]
# odd_num=[i for i in num if i%2!=0]
# print(even_num)
# print(odd_num)



#if else in lc


num=[1,4,3,6,8,9,13,5]
#jhaa even uski 2 sai multiply aur jhaa odd bhaa -1
# num_new=[-1,16,-3,36,64,-9,-13,-5]

#simple 
# num_new=[]
# for i in num:
#     if i%2==0:
#         num_new.append(i**2)
#     else:
#         num_new.append(-i)
# print(num_new)


#lc method 
# num_new=[i**2 if i%2==0 else -i for i in num]
# print(num_new)



#nested list comp
# output=[[1,2,3],[1,2,3],[1,2,3]]

#simple
# new_list=[]
# for j in range(3):
#     new_list.append([1,2,3])
# print(new_list)

#lc
# new_list=[[i for i in range(1,4)] for j in range(0,3)]
# print(new_list)