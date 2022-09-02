def printer(l,**kwargs):
    if True in kwargs.values():
        return[name[::-1].title() for name in l] 
    else:
        return[name.title() for name in l] 
     
print(printer(["ashui","sifufgfgd"],reverse_str=True))        



