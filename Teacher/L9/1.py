import math
import requests
from bs4 import BeautifulSoup as bs

# Шукаємо кол-во сторінок
def count_all_pages(url):
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    find_all_ads = soup.find('span', class_='css-7ddzao')
    all_ads = find_all_ads.text.split()[2]
    return math.ceil(int(all_ads) / 35)

def get_data_ads(find_ads_first_page):
    list_ads = list()
    
    for i in find_ads_first_page:
        card_data = {}
        if 'ТОП' not in i.text:
            card_data["title"]= i.find('h6', class_='css-16v5mdi er34gjf0').text
            card_data["location"]= i.find('p', class_='css-1a4brun er34gjf0').text
            card_data["price"]= i.find('p', class_='css-tyui9s er34gjf0').text
            card_data["link"]= i.find('a', class_='css-z3gu2d').get('href')

            response_ad = requests.get(f'https://olx.ua{card_data["link"]}')
            soup_ad = bs(response_ad.text, 'lxml')

            card_data["description"] = soup_ad.find('div', class_='css-1t507yq er34gjf0').text,
            card_data["price_usd"] = soup_ad.find('h3', class_='css-12vqlj3').text
            
            text = f"""
{card_data["title"]}\n
{card_data["price"]} або {card_data["price"]}\n
Опис:\n{card_data["description"]}\n
https://olx.ua{card_data["link"]}\n\n
{card_data["location"]}\n
            """
            list_ads.append(text)
    return list_ads

# Анализуємо пропозиції та витягуємо данні
def get_ads_on_first_page(url, page):
    url = f'https://www.olx.ua/uk/nedvizhimost/kvartiry/prodazha-kvartir/dnepr/?currency=UAH&page={page}&search%5Bdistrict_id%5D=111&search%5Bfilter_enum_number_of_rooms_string%5D%5B0%5D=odnokomnatnye'
    
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    find_ads_first_page = soup.find_all('div', class_='css-qfzx1y')
    return get_data_ads(find_ads_first_page)

# Проходимо по всім сторінкам і записуємо у файл
def ads_on_all_pages(url):
    pages = count_all_pages(url)
    
    for page in range(1):
        print(f'Аналізую {page} сторінку')
        list_ads_urls = get_ads_on_first_page(url, page)
        for i in list_ads_urls:
            with open('OLX.txt', 'a', encoding='utf-8') as file:
                file.write(f'******************\n')
                file.write(i)
        print(f'Парсинг сторінки {page} завершено!')
    print(f'Парсинг завершенно!')
            
def main():
    url = f'https://www.olx.ua/uk/nedvizhimost/kvartiry/prodazha-kvartir/dnepr/?currency=UAH&search%5Bdistrict_id%5D=111&search%5Bfilter_enum_number_of_rooms_string%5D%5B0%5D=odnokomnatnye'
    ads_on_all_pages(url)
    

if __name__ == '__main__':
    main()