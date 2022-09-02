def common(f,s):
    comlis=[]
    for i in f:
        if i in s:
            comlis.append(i)
    return comlis            
 
l1=[2,5,1,9,13,6]
l2=[4,8,15,34,13,2,6]   
print(common(l1,l2))             