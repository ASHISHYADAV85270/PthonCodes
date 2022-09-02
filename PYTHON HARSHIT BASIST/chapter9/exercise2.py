l=[True,3.0,False,None,44,[2,5,3,5],33.8]
# output=["3.0","44","33.8"]

output=[str(i) for i in l if type(i)==int or type(i)==float ]
print(output)