import re
names = input("Введите словосочетания:")
print(''.join(x[0] for x in names.split()))
