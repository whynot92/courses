'''

Легкий рівень
Easy level

'''

# # 1. Реалізуйте клас "Rectangle", який має атрибути "width" та "height",
# # які відповідають за ширину та висоту прямокутника відповідно. Клас повинен 
# # також мати методи "area()" та "perimetr()", який повертає площу прямокутника
# # та периметр відповідно.
# #
# # 1. Implement a "Rectangle" class that has "width" and "height" attributes,
# # which are responsible for the width and height of the rectangle, respectively. The class must 
# # also have methods "area()" and "perimetr()" which returns the area of ​​a rectangle
# # and perimeter respectively.

# class Rectangle():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
#     def perimetr(self):
#         return (self.width + self.height) * 2
    

# rect1 = Rectangle(12, 6)

# print(rect1.area())
# print(rect1.perimetr())

# # 2. Реалізувати клас "Account", який має атрибути "balance" , що відповідають за баланс рахунку.
# # Клас повинен мати метод "add()", який додає вказану суму до балансу рахунку, та метод "minus()",
# # який знімає з рахунку вказану суму, якщо на рахунку достатньо коштів.
# #
# # 2. Implement the "Account" class, which has "balance" attributes responsible for the account balance.
# # The class must have an "add()" method, which adds the specified amount to the account balance, 
# # and a "minus()" method, which withdraws the specified amount from the account if there are enough 
# # funds in the account.

# class Account():
    
#     def __init__(self, balance=0):
#         self.balance = balance

#     def add(self, money):
#         self.balance += money

#     def minus(self, money):
#         if self.balance >= money:
#             self.balance -= money
#         else:
#             print("There are insufficient funds in the account")

# acc1 = Account(12)

# acc1.add(5)
# acc1.minus(12)
# print(acc1.balance)

# # 3. Створіть клас Фрукт з атрибутом назва. Створіть підклас Яблуко, який успадковує клас Фрукт та має 
# # додатковий атрибут сорт. Створіть об'єкти цих класів та виведіть їх атрибути.
# #
# # 3. Create a Fruit class with a name attribute. Create a subclass of Apple that inherits from the Fruit 
# # class and has additional attribute sort. Create objects of these classes and display their attributes.

# class Fruts():
    
#     name = ""

# class Apple(Fruts):

#     variety = ""

#     def introdus(self):
#         return f'{self.name}, {self.variety}'
    
# apple = Apple()
# apple.name = "Golden"
# apple.variety = "Yellow"

# print(apple.introdus())

# # 4. Створити клас "Пасажирський літак" з атрибутами "модель", "кількість місць" і "кількість пасажирів 
# # на борту". Додайте методи для додавання та видалення пасажирів.
# #
# # 4. Create a class "Passenger plane" with attributes "model", "number of seats" and "number of passengers 
# # on board". Add methods for adding and removing passengers.

# class Passenger_plane():

#     def __init__(self, model: str, number_of_searts: int, number_of_passengers: int):
#         self.model = model
#         self.number_of_searts = number_of_searts
#         self.number_of_passengers = number_of_passengers

#     def add_passengers(self, plus_people):
#         self.number_of_passengers += plus_people

#     def minus_passengers(self, minus_people):
#         self.number_of_passengers -= minus_people

#     def __str__(self):
#         return f'{self.number_of_passengers}'

# first_plain = Passenger_plane("boing", 250, 110)
# first_plain.add_passengers(15)
# first_plain.minus_passengers(5)

# print(first_plain)

# # 5. Створити клас "Студент" з атрибутами "ім'я", "вік" і "середній бал". Додайте метод для визначення 
# # ступеня відмінності студента.
# #
# # 5. Create a class "Student" with attributes "name", "age" and "average score". Add a method to define 
# # degree of distinction of the student.

# class Student():

#     def __init__(self, name: str, age: int, average_score: int):
#         self.name = name
#         self.age = age
#         self.avetage_score = average_score

#     def degree(self):
#         if self.avetage_score >= 90:
#             return "Excellent"
#         elif self.avetage_score >= 75:
#             return "Fine"
#         elif self.avetage_score >= 60:
#             return "Satisfactorily"
#         else:
#             return "Unsatisfactorily"
        
# first_student = Student("Vova", 21, 70)
# degree_first_student = first_student.degree()

# print(f"Degree of distinction of {first_student.name} = {degree_first_student}")

# # 7. Створіть базовий клас "Фрукт" з двома властивостями: "назва" і "колір". Напишіть метод для виведення 
# # інформації про фрукт, що включає назву і колір.
# #
# # Потім створіть клас "Яблуко", який успадковує клас "Фрукт" і має додаткову властивість "смак". 
# # Напишіть метод для виведення інформації про яблуко, що включає назву, колір та смак.
# #
# # Створіть об'єкт яблука і викличте метод для відображення інформації про нього.
# #
# # 7. Create a base class "Fruit" with two properties: "name" and "color". Write a method to output 
# # information about the fruit, including name and color.
# #
# # Then create an Apple class that inherits from the Fruit class and has an additional taste property. 
# # Write a method to output information about an apple, including its name, color, and flavor.
# #
# # Create an apple object and call a method to display information about it.

# class Fruit():
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def display_info(self):
#         return f"This fruit is called {self.name} and has a color {self.color}"
    
# class Apple(Fruit):

#     def __init__(self, name, color, taste):
#         super().__init__(name, color)
#         self.taste = taste

#     def display_info(self):
#         super().display_info()
#         print(f"Taste: {self.taste}, Name: {self.name}")

# fruie = Fruit("fruit", "green")
# print(fruie.display_info())

# apple = Apple("Golden", "Yellow", "Sweet")
# apple.display_info()

'''

Складний рівень
Difficult level

'''

# # 1. Створіть систему класів для представлення різних видів транспорту. В системі повинні бути наступні класи:
# #
# # Клас Транспорт:
# # Має атрибути: марка та рік випуску.
# # Має метод рухатися, який виводить повідомлення "Транспорт рухається".
# #
# # Клас Автомобіль:
# # Успадковує клас Транспорт.
# # Додає атрибут об'єм двигуна.
# # Має метод розгін, який виводить повідомлення "Автомобіль розганяється до 100 км/год за 10 секунд".
# #
# # Клас Мотоцикл:
# # Також успадковує клас Транспорт.
# # Додає атрибут кубатура двигуна.
# # Має метод каскад, який виводить повідомлення "Мотоцикл може виконувати каскади на мототрасі".
# #
# # 3. Create a class system to represent different modes of transportation. The system should have the following classes:
# #
# # Class Transport:
# # Has attributes: brand and year of manufacture.
# # Has a move method that outputs the message "Vehicle is moving".
# #
# # Class Car:
# # Inherits the Transport class.
# # Adds an engine volume attribute.
# # Has an acceleration method that displays the message "The car accelerates to 100 km/h in 10 seconds".
# #
# # Class Motorcycle:
# # Also inherits the Transport class.
# # Adds the engine cubic capacity attribute.
# # Has a cascade method that displays the message "Motorcycle can perform cascades on a motorcycle track".

# class Transport():
    
#     def __init__(self, brand="", year_manufacture=0):
#         self.brand = brand
#         self.year_manufacture = year_manufacture

#     def move_transport(self):
#         print("Vehicle is moving")

# class Car(Transport):

#     def __init__(self, brand, year_manufacture, engine_volume=0):
#         super().__init__(brand, year_manufacture)
#         self.engine_volume = engine_volume

#     def acceleration(self):
#         print("The car accelerates to 100 km/h in 10 seconds")

# class Motorcycle(Transport):

#     def __init__ (self, brand, year_manufacture, cubic_capacity):
#         super().__init__(brand, year_manufacture)
#         self.cubic_capacity = cubic_capacity

#     def cascad(self):
#         print("Motorcycle can perform cascades on a motorcycle track")

# 2. Створити базовий клас Гроші, який представляє грошову суму і має методи для додавання, 
# віднімання і зміни грошової суми. Потім створити похідні класи Долар і Євро, які успадковуються 
# від класу Гроші. Кожен з похідних класів повинен мати свою властивість, яка визначає валюту,
# та перевизначений метод str() для зручного виводу грошової суми у відповідній валюті.
#
# 2. Create a base class Money that represents an amount of money and has methods to add, 
# subtracting and changing the amount of money. Then create derived classes Dollar and Euro, which are 
# inherited from the Money class. Each of the derived classes must have its own property that defines 
# the currency, and an overridden str() method for convenient output of the monetary 
# amount in the appropriate currency.

class Money():
    pass