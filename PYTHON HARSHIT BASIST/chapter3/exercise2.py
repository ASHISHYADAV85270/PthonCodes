name,age=input("ENTER YOUR NAME AND AGE").split(",")
age=int(age)
# if name.lower()[0]=="a" and age>=10:
#     print("you can watch the movie bro")
# else:
#     print("you need permision bro")



if  age>=10 and (name[0]=='a' or name[0]=='A'):
    print("you can watch the movie bro")
else:
    print("you need permision bro") 