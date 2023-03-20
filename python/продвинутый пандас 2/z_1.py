import pandas as pd

data = pd.read_csv('ratings.csv')
maxx = data['userid'].max() # сколько пользователей
time [maxx]
for man in range(maxx): # идем по каждому пользователю
    
    ball=0
    
    sort = data.query("userid = ",man)      
    
    if sort.rows >= 100:
        min_time = sort[sort.userid == man and sort.timestamp == sort.timestamp.min()]
        max_time = sort[sort.userid == man and sort.timestamp == sort.timestamp.max()]
        time[man] = max_time - min_time
        
print ("средняя продолжительност ьжизни ", sum(time)/len(time))
        
    
        
