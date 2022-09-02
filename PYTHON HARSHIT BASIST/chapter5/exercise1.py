def square_list(l):
    for i in l:
        l_new.append(i**2)
        
l=list(range(1,10)) 
print(l)   
l_new=[]
square_list(l)
print(l_new)
  