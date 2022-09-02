l=["abc","xyz","pqr"]
# r=["cba","zyx","rqp"]  we want this 

#simple method
# r=[]
# for i in l:
#     r.append(i[::-1])

# print(r)

#list comprehension method----> kya append krna hai ...fir uska way
# r=[i[::-1] for i in l]
# print(r)
sum_of_squares = sum(num ^ 2 for num in range(3) if num>0)
print(sum_of_squares)
