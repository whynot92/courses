import requests
from bs4 import BeautifulSoup

bot_token = "7310573884:AAHqe2f5ED23UCGS6GCcDywzHBciZaHE7yI"
group_id = "-4201133737"

url = 'https://www.olx.ua/uk/elektronika/telefony-i-aksesuary/?currency=UAH&search%5Border%5D=created_at%3Adesc'

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'lxml')

title = soup.find('h6', class_='css-16v5mdi')
price = soup.find('p', class_='css-tyui9s')
photo = soup.find('img', class_='css-8wsg1m')["src"].replace(';s=200x0;q=50', '')
print(photo)

text = f"{title.text}\n\n{price.text}"

url = f"https://api.telegram.org/bot{bot_token}/sendPhoto?chat_id={group_id}&caption={text}&photo={photo}"

# send_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message_text}&disable_web_page_preview=true'

response = requests.get(url)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit(0)
else:
    print("send message")