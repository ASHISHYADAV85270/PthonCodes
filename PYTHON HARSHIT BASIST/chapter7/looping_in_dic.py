user_info={
    "fname":"ashish",
    "lname":"yadav",
    "contact":8527086883,
    "age":21,
    "fav_person":["virat","MSD"]
}


#check if key is present  in dictionary
# if "fname" in user_info:
#     print("present ")
# else:
#     print("NOT present ")


#check if value is present  in dictionary---->values method
# if "ashish" in user_info.values():
#     print("present ")
# else:
#     print("NOT present ")



#values method ****************
# new_dic_values=user_info.values()
# print(new_dic_values)
# print(type(new_dic_values))   #its type is  <class 'dict_values'>
#ek tuple mai saari values ki list aajaigi




#keys method ***************
# new_dic_keys=user_info.keys()
# print(new_dic_keys)
# print(type(new_dic_keys))   #its type is  <class 'dict_keys'>
#ek tuple mai saari keys ki list aajaigi



#items method ...it is the best method
# new_dic_items=user_info.items()
# print(new_dic_items)
# print(type(new_dic_items))
   #its type is  <class 'dict_items'>
# ek tuple mai saari (keys,values) i.e tuple ki form mai ki list aajaigi 
# ((key,value),(key,value),(key,value),(key,value))
# dict_items([('fname', 'ashish'), ('lname', 'yadav'), ('contact', 8527086883), ('age', 21), ('fav_person', ['virat', 'MSD'])])


#why it is best????
# for i,j in user_info.items():   #its like tuple unpacking
#     print(f"key is {i} and value is {j}")


# for i in user_info.items():
#     print(i)






#loops in dictionary 
#type 1
# for i in user_info:
#     print(i)   # it will print all the key only

#type2
# for i in user_info.values():
#     print(i)   # it will print all the values only  

# for i in user_info:
#     print(user_info[i])   # it will print all the values only  

