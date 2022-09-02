#method 1 
# n=number=int(input("ENTER A NUMBER BRO "))
# total=0

# while number>0:
#     total=number%10 +total
#     number=int(number/10)
# print(f"sum of digits of the number {n} is equal to {total}")


#method 2 
# n=number=input("ENTER A NUMBER BRO ")
# total=0
# i=0
# while i<len(number):
#     total=total +int(number[i])
#     i=i+1
# print(f"sum of digits of the number {n} is equal to {total}")


#method 3 
# n=number=input("ENTER A NUMBER BRO ")
# total=0
# for i in range(len(number)):
#     total=total +int(number[i])
# print(f"sum of digits of the number {n} is equal to {total}")



#method 4
# number=input("ENTER A NUMBER BRO ")
# total=0
# for i in number:
#     total+=int(i)
# print(total)