
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
print ()
boys.sort()
girls.sort()
i=0
print ('Идеальные пары:' )
while i < len(girls):
    print (boys[i],'и',girls[i])
    i+=1
