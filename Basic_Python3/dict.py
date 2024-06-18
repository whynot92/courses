
'''

Легкий рівень

'''

# 1. Знайдіть суму квадратів елементів цього словника.
# #
# # 1. Find the sum of the squares of the elements of this dictionary.
# # dct = { 'x': '1', 'y': '2', 'z': '3' }

# dct = { 'x': '1', 'y': '2', 'z': '3' }

# answer = 0

# for i in dct.values():
#     answer += int(i) ** 2

# print(answer)

# # 2. Складіть значення кожного словника. Потім від першої суми відніміть другу.
# #
# # 2. Make up the meaning of each dictionary. Then subtract the second from the first amount.
# # dct1 = { '1': 12, '2': 24, '3': 36 }
# # dct2 = { 'a': '3', 'b': '6', 'c': '9' }

# dct1 = { '1': 12, '2': 24, '3': 36 }
# dct2 = { 'a': '3', 'b': '6', 'c': '9' }

# sum_dct1= 0
# sum_dct2 = 0

# for i in dct1.values():
#     sum_dct1 += int(i)

# for i in dct2.values():
#     sum_dct2 += int(i)

# print(sum_dct1 + sum_dct2)

# # 3. Перетворіть усі його значення на рядки.
# #
# # 3. Convert all its values ​​to strings.
# # dct = { 1: '4', 2: '5', 3: '6' }

# dct = { 1: '4', 2: '5', 3: '6' }

# new_dct = dict()

# for key, value in dct.items():
#     new_dct[key] = str(value)

# print(new_dct)

# # 4. Напишіть код, щоб отримати наступний результат:
# # Код:
# #
# # 4. Write the code to get the following output:
# # Code:
# # dct = { 'x': '1', 'y': '2', 'z': '3' }
# # Вихідний код:
# #
# # Source code:
# # ['11', '222', '3333']

# dct = { 'x': '1', 'y': '2', 'z': '3' }

# new_list = [i * int(i) + i for i in dct.values()]
# print(new_list)

# # 5. Напишіть код, щоб отримати наступний результат:Напишіть код, щоб отримати наступний результат:
# # Код:
# #
# # 5. Write the code to get the following output:Write the code to get the following output:
# # Code:
# # dct = { 'x': '1', 'y': '2', 'z': '3' }
# # Вихідний код:
# #
# # Source code:
# # ['x', 'yy', 'zzz']

# dct = { 'x': '1', 'y': '2', 'z': '3' }

# new_list = [key * int(value) for key, value in dct.items()]
# print(new_list)

# # 6. Складіть елементи цього словника як рядки:
# # Код:
# #
# # 6. Put the elements of this dictionary as strings:
# # Code:
# # dct = { 'x': 1, 'y': 2, 'z': 3 }
# # Вихідний код:
# #
# # Source code:
# # '123'

# dct = { 'x': 1, 'y': 2, 'z': 3 }

# str_answer = ""

# for i in dct.values():
#     str_answer += str(i)

# print(str_answer)

# # 7. Складіть елементи цього словника як рядки:
# # Код:
# #
# # 7. Put the elements of this dictionary as strings:
# # Code:
# # dct = { 'a': 7, 'b': 6, 'c': 5 }
# # Вихідний код:
# #
# # Source code:
# # '5/6/7'

# dct = { 'a': 7, 'b': 6, 'c': 5 }


# value_list = [str(i) for i in dct.values()]
# value_list.reverse()

# print("/".join(value_list))

# # 8. Складіть елементи цього словника у вигляді наступної дати:
# # Код:
# #
# # 8. Put the elements of this dictionary in the form of the following date:
# # Code:
# # dct = { 'y': 2025, 'm': 12, 'd': 31 }
# # Вихідний код:
# #
# # Source code:
# # '2025-12-31'

# dct = { 'y': 2025, 'm': 12, 'd': 31 }


# value_list = [str(i) for i in dct.values()]

# print("-".join(value_list))

# # 9. Дано словник, який містить «Прізвище»-«оцінка». На його основі створити новий словник,
# # який буде містити лише учнів, які навчаються на 4 та 5
# #
# # 9. A dictionary containing "Surname"-"rating" is given. Create a new dictionary based on it,
# # which will contain only students studying in 4th and 5th
# # students = {"Петров": 3, "Іванов": 4, "Сидоров": 5, "Смирнов": 2, "Козлов": 4}

# students = {"Ivan": 5, "Vadym": 3, "Sergio": 1, "Vika": 4, "Marshal": 5}
# favorite = dict()

# for key, value in students.items():
#     if value >= 4:
#         favorite[key] = value

# print(favorite)

# # 10. Погода. У словнику збережено інформацію про температурі у різних містах: ключами є назви
# # міст, значеннями – температура. Розрахуйте середню температуру за цими містами
# #
# # 10. Weather. The dictionary stores information about the temperature in different cities:
# # the keys are the names bridge, values ​​- temperature. Calculate the average temperature for these
# # cities
# #
# # temperatures = {
# #     'Київ': 25,
# #     'Львів': 20,
# #     'Одеса': 28,
# #     'Харків': 22,
# #     'Дніпро': 24
# # }

# temperatures = {
#     'Київ': 25,
#     'Львів': 20,
#     'Одеса': 28,
#     'Харків': 22,
#     'Дніпро': 24
# }

# len_temperatures = len(temperatures)
# sum_temperatures = 0

# for i in temperatures.values():
#     sum_temperatures += int(i)

# print(f'Average temperature for these cities: {sum_temperatures / len_temperatures}')



# # 11.Користувач має логін та пароль. Користувач має ввести свій логін та пароль, перевірити дані і
# # написати чи вхід здійснено чи н.і
# #
# # 11. The user has a login and password. The user must enter his login and password, check
# # the data and write whether the entry is made or n.i
# # users = {
# #     'john': 'password123',
# #     'alice': 'alice2022',
# #     'bob': 'bobiscool',
# #     'emma': 'emma1234',
# #     'david': 'davidPassword'
# # }

# users = {
#     'john': 'password123',
#     'alice': 'alice2022',
#     'bob': 'bobiscool',
#     'emma': 'emma1234',
#     'david': 'davidPassword'
# }
# nick_user = input("Write here your nickname: ")
# password_user = input("Write here your password: ")

# if nick_user in users:
#     if password_user == users[nick_user]:
#         print("Login is correct.")
# else:
#     print("Login or password isn't correct.")

'''

Складний рівень

'''

# 1. Напишіть програму, яка приймає два словники і повертає словник з ключами як з першого
# словника, так і з другого словника, а значення якого складаються з значень обох словників.
#
# 1. Write a program that takes two dictionaries and returns a dictionary with the same keys as
# the first of the dictionary, as well as from the second dictionary, and the values ​​of which
# consist of the values ​​of both dictionaries.
