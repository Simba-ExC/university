stats = {'facebook': 55,
         'yandex': 115,
         'vk': 120,
         'google': 99,
         'email': 42,
         'ok': 98}
name = "clear"
sts = 0
for key in stats:
    if stats[key] > sts:
        sts = stats[key]
        name = key
print ('Максимальный объем продаж на рекламном канале:',name)
