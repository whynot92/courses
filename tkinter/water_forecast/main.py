import requests
from tkinter import *
import tkinter
from tkinter import ttk

API = 'bc5907b4ae2d0c49283107d768dd3f4d'
temp = ''
humidity = ''
fell_like = ''
wind = ''
weather = ''

def get_weather():
    global temp, humidity, fell_like, wind, icon, weather
    name_city = ent.get()
    responce = requests.get(f'http://api.openweathermap.org/data/2.5/find?q={name_city}&type=like&APPID={API}')
    date = responce.json()
    try:
        name_city = date['list'][0]['name']
        temp = int(date['list'][0]['main']['temp'] - 273.15)
        humidity = date['list'][0]['main']['humidity']
        fell_like = int(date['list'][0]['main']['feels_like'] - 273.15)
        wind = date['list'][0]['wind']['speed']

        lb3['text'] = name_city
        lb5['text'] = f'Temperature: {temp} \u00b0C'
        lb8['text'] = f'Air humidity: {humidity} %'
        lb6['text'] = f'Feels like: {fell_like} \u00b0C'
        lb7['text'] = f'Wind speed: {wind} m/s '
    except IndexError:
        lb3['text'] = 'Name error'


window = Tk()
window.title('Weather Forecast in your city')
window.geometry('250x250')

img = tkinter.PhotoImage(file="tkinter\\water_forecast\\free-icon-kraken-2534513.png", width='32', height='32')
lb1 = Label(master=window, image=img)
lb2 = Label(text='Kraken weather forecast', font='Kraken 12')

lb1.place(x='8', y='5')
lb2.place(x='45', y='12', )

lb3 = Label(text='Your city', font='Kraken 30')
lb3.place(x='5', y='45')

lb5 = Label(text=f'Temperature: {str(temp)}')
lb5.place(x='5', y='100')
lb6 = Label(text=f'Feels like: {str(fell_like)}')
lb6.place(x='5', y='120')
lb7 = Label(text=f'Wind speed: {wind}')
lb7.place(x='5', y='140')
lb8 = Label(text=f'Air humidity: {humidity}')
lb8.place(x='5', y='160')

separator = ttk.Separator(window, orient='horizontal')
separator.place(x=0, y=192, relwidth=1)

ent = Entry(width='25')
ent.place(x='15', y='210')
bt = Button(text='Кнопка', command=get_weather)
bt.place(x='180', y='205')
window.mainloop()