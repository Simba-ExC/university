import numpy as np
import pandas as pd
data = pd.read_csv('power.csv')

data.query('quantity > "1" & country == "Latvian" | country == "Lithuania" | country == "Estonia" & year > "2005" & year < "2010"  ')

print(data)
