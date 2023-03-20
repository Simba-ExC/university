import pandas as pd

data = pd.read_csv('ratings.csv')
maxx = data['movieId'].max() # сколько у нас фильмов 

max_id =0
max_film = 0
max_movi = 0

sort_move = data.query("rating==5.0") # исключаем ненужные строки 

for movi in range(maxx): # ищем каждый фильм

    sort = data.query("movieId == @movi")
    max_id = sort.shape[0]   #сколько строк с данным фильмом и рейтингом 5.0
    if max_id > max_film:
        max_film = max_id
        max_movi = movi
        
print ("фильм с максимальным рейтингом с id",max_movi)
        
    
        
