
#example 1
# square={
# 251:1,
# 2:4,
# 3:9,
# 4:16,
# }
# square={num:num**2  for num in range(1,11)}
# square={f"square of {num} is ":num**2  for num in range(1,11)}
# print(square)



#example 2
name="ashpdjasasvislg"

#simple method
# count={}
# for subchar in name:
#     count[subchar]=name.count(subchar)
# print(count)


#dc method
# count={subchar:name.count(subchar) for subchar in name}

# print(count)
# for i,j in count.items():
#     print(f"{i} : {j}")


#if else in dc 
# d={
#     1:"odd",
#     2:"odd",
#     3:"odd",
#     4:"even"
# }
d={i:("even" if i%2==0  else "odd") for i in range(1,11)}
print(d)
