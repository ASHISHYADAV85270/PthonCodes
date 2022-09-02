def insertdata(d):
    for key in d:
        val=input(f"ENTER THE VALUE IN THE {key}")
        d[key]=val
    return d    

user_info={
    "fname":"unknown",
    "lname":"unknown",
    "contact":"unknown",
    "fav_movie":["none","none"]
}
user_info=insertdata(user_info)
for i in user_info.items():
    print(i)