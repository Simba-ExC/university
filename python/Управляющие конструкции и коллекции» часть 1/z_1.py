ent_Str = input("Введите слово: ")
 
fst_Str = len(ent_Str)
good_Str = fst_Str / 2
if fst_Str % 2 == 0:
    print(ent_Str[int(good_Str)-1:int(good_Str)])
elif fst_Str % 2 !=0:
    print(ent_Str[int(good_Str)])
