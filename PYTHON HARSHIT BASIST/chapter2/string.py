# name ="ashish"
# age = 21
# print("name is = " +name + "age is equal to =" +str(age))
# #it is very ugly method ....so we require short cut

# print("name is = {} agr is equal tp = {}".format(name,age))# python 3


# print(f"name is = {name} agr is equal tp = {age}") #python 3.6


#string indexing 
  #language="pyhton"
# p=0,-6
# y=1,-5
# t=2,-4
# h=3,-3
# o=4,-2
# n=5,-1
# print(language[0])
# print(language[-1])


#string slicing//selecting sub sequence 
#syntax -   [start agrdument : stop argument:stepargument]
#stop agrument mtlb joo last character print hoga usai net bala
#step baala mtlb kitna jump krna hai ....y reverse bhi print krba skta hai 
# word="ashish"
# print(word[2:4])


# word="abcdefgh"
# print(word[0:5:2])
# print(word[:5:2])
# print(word[-1:3:-1])


#string method and fuctions
#method mai hmlog . use krte hai  aur method kai changes final string pai naa jaate 
#string are immutable
# name="AsHish yaDaV"
#1 len()---> it aslo counts number of spaces also 
# print(f"length= {len(name)}")

#2 lower()   ---> convert to lower
# print(f"lower= {name.lower()}")


#3 upper()   ---> convert to upper
# print(f"upper= {name.upper()}")

#4 title()  ----> convert first character capital
# print(f"TITLE= {name.title()}")

#5 count()  --> count specific character in a string and it is case sensitive also
# print(f"count of a is = {name.count('a')}")
#yhaa pai upar notice kroo hmnai single kai andr double qoutes use ki hai

#6 replace(kiskoreplacekrna , kischiz sai, kitnai tk)  ---> 
# name= "shivani is   very   beautiful   girl  and is very selfish girl in the world and she refused happy offer"
# print(name.replace(" ","-"))
# print(name.replace("is","was",1))


#7 find("to find ", from which pos you want to find)
# user="she is a good person is wnated is"
# print(user.find("is"))
# #now if we want to find  pos of second is then this is the method
# pos1=user.find("is")
# print(f"position of first is ={pos1}")

# pos2=user.find("is",pos1 + 1)
# print(f"position of second is ={pos2}")

#8 strip method 
# user="       ashish        "
# dots="..........................."
# print(user+dots)
# print(user.lstrip() +dots)
# print(user.rstrip() +dots)
# print(user.strip() +dots)

#9 center(lenght+some value , " to be added only one character")----> word koo bich mai lekar right left dono jgh likh loo
username="ashish"
print(username.center(8,"*"))
print(username.center(10,"*"))

