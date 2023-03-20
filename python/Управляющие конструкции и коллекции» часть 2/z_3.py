results = {
'vk': {'revenue': 103, 'cost': 98},
'yandex': {'revenue': 179, 'cost': 153},
'facebook': {'revenue': 103, 'cost': 110},
'adwords': {'revenue': 35, 'cost': 34},
'twitter': {'revenue': 11, 'cost': 24},
}

for key in results:
    ROI = (results[key]['revenue']/results[key]['cost'])*100
    results[key]['ROI'] = "%.2f" % ROI

for key in results:
    print(key,end = ":")
    print(results[key])

    
