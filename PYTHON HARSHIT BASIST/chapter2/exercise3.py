# name,char=input("enter your name and pls shi name btana and also enter a character ").split(",")
# print(f"lenght of your name is = {len(name)}")
# l_char= char.lower()
# occurence= name.count(l_char)
# u_char= char.upper()
# occurence= name.count(u_char)+occurence  #method one 
# occurence=name.count(char.upper())+ name.count(char.lower()) #method two 

# occurence=name.lower().count(char.lower()) #method three 

# #now best version is there fore
# occurance=name.strip().lower().count(char.strip().lower())

# print(f"number of times the character occured is = {occurance}")



#now notice in this problem we are passing a problem that  at the time of input if after , we give space then it does not give a correct result  soo too overcome it we require a method to remove the spaces 





# name,character=input("enter the name and  character to be searched ").split(",")
# print(len(name))
# print(f"the character you inserted {character} is present {name.lower().count(character.strip().lower())} times")