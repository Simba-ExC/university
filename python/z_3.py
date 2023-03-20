import pandas as pd
import numpy as np



# Пандемия_COVID-19
tables = pd.read_html(
    'https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BD%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F_COVID-19',
    match='стран')

df = tables[1]

df.drop(('Страны и территории', 'Всего 000000000000000'), axis=1, inplace=True)

df.columns = df.columns.droplevel(-1)

df.rename(columns={'.mw-parser-output .ts-comment-commentedText{border-bottom:1px dotted;cursor:help}@media(hover:none){.mw-parser-output .ts-comment-commentedText:not(.rt-commentedText){border-bottom:0;cursor:auto}}Летал.': 'Летал.'}, inplace=True)

df.replace({'\[[0-9]+\]': ''}, regex=True, inplace=True)

print (df.head())
