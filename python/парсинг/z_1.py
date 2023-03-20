import requests
import pandas as pd
from bs4 import BeautifulSoup
URL = 'http://habr.com/ru/all'
KEYWORDS = ['python', 'парсинг']
res = requests.get(URL, KEYWORDS)
soup = BeautifulSoup(res.text, 'html.parser')
# добираемся до блоков с новостями
news_blocks = soup.find_all('div', class_='search_results_item')
# добираемся до текста со ссылкой
articles_intro = list(map(lambda x: x.find('div', class_='article_intro'), news_blocks))
# добираемся до ссылок
a_list = list(map(lambda x: x.find('a').get('href'), articles_intro))
# формируем полноценные ссылки
all_refs = list(map(lambda x: 'https://www.kommersant.ru/' + x, a_list))
#все новости
def get_all_links(url, query, pages):
    all_refs = []
    params = {
        'search_query': query
    }
    for i in range(pages):
        params['page'] = i + 1
        res = requests.get(URL, params)
        time.sleep(0.3)
        soup = BeautifulSoup(res.text, 'html.parser')
        news_blocks = soup.find_all('div', class_='search_results_item')
        articles_intro = list(map(lambda x: x.find('div', class_='article_intro'), news_blocks))
        a_list = list(map(lambda x: x.find('a').get('href'), articles_intro))
        all_refs += list(map(lambda x: 'https://www.kommersant.ru/' + x, a_list))
    return all_refs
all_links = get_all_links(URL, 'python', 3)
# собираем даты, заголовки и тексты новостей
for link in all_links:
    soup = BeautifulSoup(requests.get(link).text, 'html.parser')
    if soup.find('div', class_='b-article__publish_date'):
        date = pd.to_datetime(soup.find('div', class_='b-article__publish_date').find('time').get('datetime'), dayfirst=True).date()
    elif soup.find('time', class_='title__cake'):
        date = pd.to_datetime(soup.find('time', class_='title__cake').get('datetime'), dayfirst=True).date()
    print(date)
    if soup.find('h2', class_='article_name'): 
        title = soup.find('h2', class_='article_name').text
    else: 
        title = soup.find('h1', class_='article_name').text    
    print(title)
    text = soup.find('div', class_='article_text_wrapper').text
    print(text)
# запишем данные в датафрейм
hab_news = pd.DataFrame()
for link in all_links:
    soup = BeautifulSoup(requests.get(link).text, 'html.parser')
    time.sleep(0.3)
    if soup.find('div', class_='b-article__publish_date'):
        date = pd.to_datetime(soup.find('div', class_='b-article__publish_date').find('time').get('datetime'), dayfirst=True).date()
    elif soup.find('time', class_='title__cake'):
        date = pd.to_datetime(soup.find('time', class_='title__cake').get('datetime'), dayfirst=True).date()
    if soup.find('h2', class_='article_name'): 
        title = soup.find('h2', class_='article_name').text
    else: 
        title = soup.find('h1', class_='article_name').text    
    text = soup.find('div', class_='article_text_wrapper').text
    row = {'date': date, 'title': title, 'text': text}
    hab_news = pd.concat([hab_news, pd.DataFrame([row])])  
hab_news = get_hab_news(all_links)
print(hab_news)
