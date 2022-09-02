#we use enumerate function with for loop to track position of our items in iterration


#how can we do this without enumerate function
name=["Asd","vikas","lsif"]
# 0----> asd 
#1 ----> vikas 
#2---> lsif

# pos=0
# for i in name:
#     print(f"{pos}---->{i}")
#     pos+=1



#enumerate function
for pos,subname in enumerate(name):
    print(f"{pos}---->{subname}")



