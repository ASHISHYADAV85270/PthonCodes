def power(num,*args):
    if args:
       return [i**num for i in args]
    else:
        return"pls give args bro"

numbers=[2,3,4,5,6]
print(power(3,*numbers))