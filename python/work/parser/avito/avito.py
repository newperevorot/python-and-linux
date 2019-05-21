#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
sys.setdefaultencoding('utf-8')

#План:
#1. Выяснить количество страниц
#2. Сформировать список урлов на страницы выдачи
#3. Собрать данные

def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    #print(len(ads))

    for ad in ads:
        #title, price, metro, url
        title = ad.find('div', class_='description').find('h3')
        print(title.decode('utf-8').encode('cp866'));



def main():
    url = 'https://www.avito.ru/vladimirskaya_oblast?p=1&q=htc'
    base_url = 'https://www.avito.ru/vladimirskaya_oblast?';
    page_part = 'p='
    query_part = '&q=htc'

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages + 1):
        url_gen = base_url + page_part + str(i) + query_part
        #print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)




if __name__ == '__main__':
    main()
