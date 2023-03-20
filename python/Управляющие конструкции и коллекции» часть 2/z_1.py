ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]}

print("Результат",end = " : { ")
for key in ids:
    user = ids [key]
    set_res_1 = set(user)
    list_res_1 = (list(set_res_1))
    for item_1 in list_res_1:
        print(item_1,end = ", ")
print(end = "}")

