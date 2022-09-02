def printdata(d):
    for i,j in d.items():
        print(f"number is = {i} and value of cube is {j}")



def cuber(num):
    data={}
    for i in range(1,num+1):
        y=i**3
        data[i]=y
    printdata(data)

cuber(13)       

