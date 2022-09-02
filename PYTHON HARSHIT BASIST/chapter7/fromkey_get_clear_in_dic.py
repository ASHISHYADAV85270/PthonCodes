# user_info={
#     "fname":"unknown",
#     "lname":"unknown",
#     "contact":"unknown",
# }

# agr saari keys mai same values deni hai too 
user_info=dict.fromkeys(["fname","lname","contact"] , "unknown")
# user_info=dict.fromkeys(("fname","lname","contact") , "unknown")
# for i,j in user_info.items():
#     print(f"key is {i} and value is {j}")





# get method
name_info={
    "fname":"ashish",
    "lname":"yadav",
}
# print(name_info["fnames"])  # it will give error 
# print(name_info.get("fnames"))  # it will give none but not error ..so it is better
# print(name_info.get("fname"))
# print(name_info.get("fnames")) #it will return none 
# print(name_info.get("fnames","not founded!!!")) #"it will return not founded!!!"










#clear
# name_info.clear()  # it will delete all data from dic
# print(name_info)

#copy 
d={
    "language":["java","python"],
    "editor":"vscode"
}

# case:1
# d1=d # it means d1 and d are same ... soo if we doo changes in d1 then it will be refected in d also
# print(d1==d)  # it will true because they are same values
# print(d1 is d) # it will also give true because they will have same value and adress


# case:1
# d1=d.copy() #if we doo changes in d1 then it will not be refected in d ..
# print(d1==d)  # it will true because they are same values
# print(d1 is d) 
# it will give false bec it also compare memory adress of dic too