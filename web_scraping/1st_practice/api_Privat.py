import requests
#1
respons = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')

usd = respons.json()[1]['buy']
eur = respons.json()[0]['buy']

input_user = int(input("Write your value: "))
input_money = input("Write here USD or EUR: ")

if input_money == 'USD':
    print(f'your courses = {input_user * float(usd)}')
else:
    print(f'your courses = {input_user * float(eur)}')
