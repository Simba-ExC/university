name=[]
bal_att=[]
bal_inst=[]
for i in range(3):
    spisok = input ("введите имя абитуриента, средний балл аттестата исредний балл, полученный при поступлении в институт \n")
    aud = spisok.split(" ")
    name.append(aud[0])
    bal_att.append(aud[1]) 
    bal_inst.append(aud[2])
print ("\nТекущие абитуриенты: \n Имя            |",name,"\n средний балл аттестата  |",bal_att ,"\n Средний балл, полученный при поступлении в институт     |",bal_inst)

print ("\nАбитуриентов, у которых разница средних баллов более 0,5\n")
for i in range(len(bal_att)):
    sr =float(abs(float(bal_att[i])- float(bal_inst[i])))
    if sr >= 0.5:
        print ("у",name[i],"разница средних баллов %.2f" % sr)
    

print ("\nАбитуриентов, у которых разница средних баллов более 1\n")
for i in range(len(bal_att)):
    sr =float(abs(float(bal_att[i])- float(bal_inst[i])))
    if sr >= 1:
        print ("у",name[i],"разница средних баллов %.2f" % sr)

print ("\nАбитуриентов, у которых разница средних баллов более 2\n")
for i in range(len(bal_att)):
    sr =float(abs(float(bal_att[i])- float(bal_inst[i])))
    if sr >= 2:
        print ("у",name[i],"разница средних баллов %.2f" % sr)
