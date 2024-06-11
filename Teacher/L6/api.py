import requests

responce = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')

if responce.status_code != 200:
    print(f'Error: {responce.status_code}')
    exit(0)

print(responce.json()[0]["buy"])
print(responce.json()[1]["buy"])