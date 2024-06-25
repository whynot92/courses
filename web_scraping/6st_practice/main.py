import requests
from bs4 import BeautifulSoup

def get_all_actions(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')

    all_actions = soup.find_all('div', class_='actions-list__item')
    return all_actions

def get_images_promo(all_action):
    list_info_actions = []

    for i in all_action:
        data_content = {}
        data_content['img_url'] = i.find('a', class_='actions-list__img').get('src')
        data_content['name_action'] = i.find('h4', class_='actions-list__title').text
        # data_content['get_end_days'] = i.find('div', class_='timer__days timer-item').text
        # data_content['get_end_hour'] = i.find('div', class_='timer__hours timer-item').text
        # data_content['get_and_minutes'] = i.find('div', class_='timer__minutes timer-item').text
        data_content['get_url'] = i.find('a', class_='actions-list__img').get('href')
        print(data_content)
        list_info_actions.append(data_content)
    return list_info_actions




def main():
    url_all_actions = 'https://www.atbmarket.com/promo/all'
    # get_all_action = get_all_actions(url_all_actions)
    # a = get_images_promo(get_all_action)
    a = get_all_actions(url_all_actions)
    print(a)

if __name__ == '__main__':
    main()