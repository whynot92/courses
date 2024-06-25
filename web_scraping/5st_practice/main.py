import time
import schedule
import requests
from datetime import datetime
from bs4 import BeautifulSoup

message_sent = False

def get_all_tr(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    all_tr = soup.find_all('tr')
    return all_tr

def get_all_td(all_tr):
    list_td = []
    for i in all_tr:
        row_list =[]
        all_td = i.find_all('td')
        for a in all_td:
            row_list.append(a.text.strip())
        list_td.append(row_list)
    return list_td

def get_dict(list_td):
    new_list = []
    for i in list_td:
        dict_one = dict()
        if len(i) >= 4:
            dict_one['Date'] = i[0].strip()
            dict_one['Total Occupied(KM)'] = i[1].rstrip(' km&sup2')
            dict_one['Total Occupied(%)'] = i[2].strip()
            dict_one['Change'] = ''.join(i[3:6]).rstrip(' km&sup2')
            new_list.append(dict_one)
    return new_list

def time_comparisons(finish_info):
    today = datetime.today().strftime('%Y.%m.%d')
    for i in finish_info:
        if i['Date'] == today:
            answer = f'''
Дата: {i['Date']}
Всего занято в км²: {i['Total Occupied(KM)']} км²
Всего занято в %: {i['Total Occupied(%)']}
Изменение в км²: {i['Change']} км²
'''
            return answer
    return None

def message_in_telegram():
    global message_sent
    url = 'https://deepstat.xyz/areas.php'
    all_tr = get_all_tr(url)
    all_td = get_all_td(all_tr)
    finish_info = get_dict(all_td)
    comparisons = time_comparisons(finish_info)
    print(comparisons)
    if comparisons is not None and not message_sent:
        bot_token = "7310573884:AAHqe2f5ED23UCGS6GCcDywzHBciZaHE7yI"
        group_id = "-4201133737"
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={group_id}&text={comparisons}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Ошибка при отправке сообщения: {response.status_code}")
        else:
            print("Сообщение успешно отправлено в Telegram")
            message_sent = True
    else:
        print("На сегодня нет данных или сообщение уже отправлено, сообщение не отправлено")

def main():
    schedule.every(5).seconds.do(message_in_telegram)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()