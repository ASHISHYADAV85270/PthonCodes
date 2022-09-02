#######method 1
# #to count number of time a character occured in a string and repeat no allowed
# name=input("ENTER YOUR NAME BRO ")
# # count=0
# while name:
#     # count=name.count(name[0])
#     # print(f"{name[0]}= {count}")
#     print(f"{name[0]}= {name.count(name[0])}")
#     name=name.replace(name[0],"")
    
#######method 2
# name=input("ENTER YOUR NAME BRO ")
# i=0    
# temp_var=""
# while i<len(name):
#     if name[i] not in temp_var:
#         temp_var+=name[i]
#         print(f"{name[i]} :  {name.count(name[i])}")
#     i+=1    

#######method 3
# name=input("ENTER YOUR NAME BRO ")    
# temp_var=""
# for i in range(len(name)):
#     if name[i] not in temp_var:
#         temp_var+=name[i]
#         print(f"{name[i]} :  {name.count(name[i])}")
  

###method 4 by dictionary method ...you will learn it in chapter 7
def coun_char(s):
    count_dictionary={}
    for char in s:
        count_dictionary[char]=s.count(char)
    return count_dictionary

name=input("ENTER YOUR NAME BRO ")
print(coun_char(name))
