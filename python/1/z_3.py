spisok = input ("введите номерные знаки \n")
spisok.lower()
spisok.strip()
my_list = spisok.split(" ")
is_repeatable = len(my_list) != len(set(my_list))
#если длина списка не равна длине множества, значит есть повторы
print("Имеются повторяющиеся элементы" if is_repeatable else "Все элементы уникальны")
for i in range(len(my_list)):
   if  my_list.count(my_list[i])>= 2:
       print (my_list[i],"повторяется больше двух раз")
       break
