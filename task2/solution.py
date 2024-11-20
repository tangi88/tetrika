from collections import Counter
import requests
from bs4 import BeautifulSoup
import csv


ADDR = 'https://ru.wikipedia.org'

def get_wiki():
    lst_url = [f'{ADDR}/wiki/Категория:Животные_по_алфавиту']
    data = []

    while lst_url:
        url = lst_url.pop()
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        div_pages = soup.find('div', id='mw-pages')
        all_pages = div_pages.findAll('a')
        next_page = all_pages[-1]
        if next_page.text == 'Следующая страница':
            lst_url.append(f'{ADDR}{next_page.attrs['href']}')

        div_category = soup.find('div', class_='mw-category mw-category-columns')
        all_category = div_category.findAll('a')

        for category in all_category:
            name_category = category.text
            data.append(name_category[0])

    counter = Counter(data)

    with open('beasts.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(dict(counter).items())

    return len(data)


if __name__ == '__main__':
    get_wiki()

