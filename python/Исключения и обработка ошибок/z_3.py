from datetime import datetime

def datediff(start_date, end_date):
        try:
                        difference=datetime.strptime(end_date,'%Y-%m-%d')-datetime.strptime(start_date,'%Y-%m-%d')
                        return f'{difference.days} дней между датами "{start_date}" и "{end_date}": {list(range(1,difference.days+1))}'
                datediff(start_date='2020-02-01', end_date='2020-02-10')

start_date = input("Введите начальную дату:")
end_date = input("Введите конечную дату:")
print(datediff(start_date, end_date))
