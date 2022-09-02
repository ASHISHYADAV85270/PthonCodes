# sets koo declare dict ki trh hi krte hai
# s={2,6,8,6}  #it will consider only one 6 
# print(s)
# # print(s[5])  #indexing not possible 

# # add element to set 
# s.add(9)
# print(s)

#remove element to set 
# s.remove(5) # if element not present it will give keyword error
# s.discard(10)  # if element not present it will not return or give any error
# print(s)


#copy 
# s2=s.copy()
# s.clear()


#union of sets
# s1={4,8,1,44}
# s2={6,9,3,57,44,8}
# union_of_sets= s1 | s2
# print(union_of_sets)


#Intersection of sets
# s1={4,8,1,44}
# s2={6,9,3,57,44,8}
# intersection_of_sets= s1 & s2
# print(intersection_of_sets)


#set to list vicecersa
#it is used to delete duplicate

# user=[2,7,4,7,4,7,4,4,8,9,1,4,6,3,9]
# print(user)
# s=set(user)
# print(s)
# user=list(s)
# print(user)


#sets comprehesion ....not in use major cases
# s={k**2 for k in range(1,11)}
# print(s)


# names={"harshit","mom","ashis","dad"}
# first_char_list={char[0] for char in names}
# print(first_char_list)