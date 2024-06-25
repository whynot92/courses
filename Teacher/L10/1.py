import requests 
from bs4 import BeautifulSoup
import time

token_bot = "7110634657:AAFm0ioKParELSmHurMIEaLyyZ0jGe_Kvr0"
group_id = "-1002024774792"
last_text = []

def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    last_tr = soup.select('tr')[1]
    last_th = soup.select('th')[1]
    date = last_tr.select('td')[0].text
    area = last_tr.select('td')[1].text
    area_km2 = last_tr.select('td')[2].text.replace('&sup2', '^2 ')
    change = last_tr.select('td')[3].text.replace('&sup2', '^2 ')
    change_mounth = last_tr.select('th')[0].text.replace('&sup2', '^2 ')

    return {
        'date': date,
        'area_occup_percent': area,
        'area_occup_km2': area_km2,
        'change_day': change,
        'change_mounth': change_mounth,
    }

def generate_msg(data):
    msg = ""
    msg += f'Окуповано:\n*{data["area_occup_percent"]}* '
    msg += f'(*{data["area_occup_km2"]}*)\n\n'
    change_day = data["change_day"].replace("\n", "")
    msg += f'Зміна:\n*{change_day}*'

    msg += "🟢\n\n" if data["change_day"].find('-') == -1 else "🔴\n\n"

    change_mounth = data["change_mounth"].replace("\n", "")
    msg += f'Зміна за місяць:\n*{change_mounth}*'
    
    msg += "🟢\n\n" if data["change_mounth"].find('-') == -1 else "🔴\n\n"

    msg += f'Оновлено: {data["date"]}\n'
    msg += f'➡️[ПІДПИСАТИСЯ](https://t.me/Occupied_area)\n'
    return msg

def send_bot(msg):
    url = f'https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={group_id}&text={msg}&parse_mode=Markdown'
    response = requests.get(url)

while True:
    data = get_data('http://kuna.pw/deepstate/areas.php')
    msg = generate_msg(data)
    if msg not in last_text:
        send_bot(msg)
        last_text.append(msg)
    time.sleep(1700)