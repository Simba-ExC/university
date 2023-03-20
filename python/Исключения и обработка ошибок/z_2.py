from datetime import datetime

stream = ['2018-04-02', '2018-02-29', '2018-19-02']

def check_date(some_date):
    try:
        datetime.strptime(some_date, '%Y-%m-%d')
        return print('дата "{}" корректна: {}'.format(some_date, True))
    except ValueError:
        return print('дата "{}" некорректна: {}'.format(some_date, False))
    
for day in stream:
    check_date(day)
