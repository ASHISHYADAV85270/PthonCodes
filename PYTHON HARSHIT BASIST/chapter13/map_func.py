# map function...esse hi filter function hota hai...but we use list com more
# map(func, *iterables) --> map object
# Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted

def squr(a):
    return a**2

num=[1,6,2,8]


#by using map function
num_new=list(map(squr,num)) #y khud hi loop chla dega 
print(num_new)

#by list comprehension
num_new=[i**2 for i in num]
print(num_new)

#by  normal method 
num_new=[]
for i in num:
    num_new.append(squr(i))

print(num_new)


#example2
names=["ashish","viaks ","anukalp"]
#calculate lenght of each string
lengths=list(map(len,names))
print(lengths)


#we use map when we use predefined fuc in  major cases