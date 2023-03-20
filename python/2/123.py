import pandas as pd
import numpy as np

data = pd.read_csv('Contacts_sample.csv', delimiter=';') # записываем из файла в DataFrame

data = data.drop(np.where(data['LInk'] == "www.enter.ru")[0])
print(data)
