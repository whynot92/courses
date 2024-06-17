import customtkinter as tk
import requests
from bs4 import BeautifulSoup

def generate():
    name_file = entry_user.get()
    page_number = 1
    number_pages = list()

    url = f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page_number}'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')

    action = soup.find_all('a', class_='title')
    price = soup.find_all('h4', class_='price float-end card-title pull-right')
    pages = soup.find('ul', class_='pagination')

    for i in pages.text.split('\n'):
        if i.isalnum():
            number_pages.append(i)
    with open(f'homework_OLX\\{name_file}.txt', 'w', encoding='utf-16') as file:
        while page_number < int(number_pages[-1]) + 1:
            file.write('\n')
            file.write('-' * 40)
            file.write(f'Страница № {page_number}')
            file.write('-' * 40)
            for a, p in zip(action, price):
                links = a.get('href')
                file.write('\n')
                file.write(f'Ноутбук: {a.text} \n')
                file.write(f'Цена: {p.text} \n')
                file.write(f'https://webscraper.io/{links} \n')
            page_number += 1
    
        else:
            file.write('-' * 40)
            file.write('End price')
            file.write('-' * 40)

    print('Данные успешно сохранены в файл price.txt')
 

tk.set_appearance_mode('System')

window = tk.CTk()
window.title('Scraper site')
window.iconbitmap('homework_OLX\\seo_marketing_finance_management_business_icon_263053.ico')
window.geometry('200x200')


bg = tk.CTkLabel(window, text='Write here name your file:')
bg.pack()

entry_user = tk.CTkEntry(window)
entry_user.pack()

bt_generate = tk.CTkButton(window, text='Generat prices', command=generate)
bt_generate.place(x=30, y=80)

window.mainloop()