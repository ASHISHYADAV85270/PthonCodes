def greatest(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    elif b>a and b>c and b>d:
        return b
    elif c>a and c>b and c>d:
        return c
    else:
        return d

def sop(nums):
    return sum(x**2 if x>0 for x in nums)

print(greatest(2,6,45,3))