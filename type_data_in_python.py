# 1. Створити дві змінні типу string і помістити туди ім’я та прізвище. Вивести привітання, враховуючи персональні дані:
# 1, Create two string variables and put the first and last name there. Display greetings, taking into account personal
# data:

first_name: str = 'Vadym'
second_name: str = 'Sokolov'

print(f'Hello {first_name} {second_name}!!!')

# 2. Ввести з клавіатури 2 числа, знайти різницю, суму, добуток та остачу першого числа від другого:
# 2. Enter 2 numbers from the keyboard, find the difference, sum, product and remainder of the first number
# from the second:

first_input_user: int = int(input('Write here your first number: '))
second_input_user: int = int(input('Write here your second number: '))
answer: int = 0

if first_input_user > second_input_user:
    answer = first_input_user - second_input_user
    print(answer)
elif first_input_user < second_input_user:
    second_input_user, first_input_user = first_input_user, second_input_user
    answer = first_input_user - second_input_user
    print(answer)

print(first_input_user + second_input_user)
print(first_input_user / second_input_user)
print(first_input_user ** second_input_user)
print(first_input_user % second_input_user)

# 3. Знайдіть результат операції:
# 3. Find the result of the operation:

print(f'10 + 10 // 2 = {10 + 10 // 2}')    # 15
print(f'18 / 3 ** 2 = {18 / 3 ** 2}')    # 2.0
print(f'14 % 4 = {14 % 4}')    # 2
print(f'10 * 10 + 5 = {10 * 10 + 5}')    # 105
print(f'5 ** 2 - 10 = {5 ** 2 - 10}')    # 15
print(f'20 * 5 // 4 = {20 * 5 // 4}')    # 25
print(f'20 + 2 * 4 = {20 + 2 * 4}')    # 28
print(f'25 - 10 % 5 = {25 - 10 % 5}')    # 25
print(f'16 // 4 ** 2 = {16 // 4 ** 2}')    # 1
print(f'30 - 15 * 2 = {30 - 15 * 2}')    # 0

# 4. Знайдіть результат операції:
# 4. Find the result of the operation:

print(f'7 * 3 <= 25 - {7 * 3 <= 25}')   # True
print(f'12 % 5 >= 2 - {12 % 5 >= 2}')   # True
print(f'4 + 5 > 6 - {4 + 5 > 6}')   # True
print(f'10 - 2 * 3 == 4 - {10 - 2 * 3 == 4}')   # True
print(f'2 * 4 + 1 >= 9 - {2 * 4 + 1 >= 9}')    # True
print(f'16 / 4 + 2 > 6 - {16 / 4 + 2 > 6}')    # False
print(f'3 * 4 - 5 <= 7 - {3 * 4 - 5 <= 7}')    # True
print(f'6 / 3 + 1 < 4 - {6 / 3 + 1 < 4}')    # True
print(f'11 - 3 == 9 + 2 - {11 - 3 == 9 + 2}')    # False
print(f'5 * 3 > 14 - {5 * 3 > 14}')    # True
print(f'(5 + 2) * 3 > 15 - {(5 + 2) * 3 > 15}')    # True
print(f'10 - (6 + 2) == 2 - {10 - (6 + 2) == 2}')    # True
print(f'(9 / 3) + (5 * 2) <= 20 - {(9 / 3) + (5 * 2) <= 20}')    # True
print(f'(7 % 3) * (2 + 3) >= 10 - {(7 % 3) * (2 + 3) >= 10}')    # False
print(f'(10 / 2) + (8 - 4) > 9 - {(10 / 2) + (8 - 4) > 9}')    # False

# 5. Напишіть програму, яка за даним N від 1 до 9 виводить на екран N пінгвінів. Зображення одного пінгвіна має розмір
# 5×9 символів, між двома сусідніми пінгвінами також є порожній (з прогалин) стовпець.
# 5. Write a program that, given N from 1 to 9, displays N penguins on the screen. The image of one penguin has the size
# 5×9 symbols, there is also an empty (from spaces) column between two adjacent penguins.

# number: int = int(input("Write your number from 1 - 9: "))
#
# penguin = r'''
#     _~_
#    (o o)
#   /  V  \
#  /(  _  )\
#    ^^ ^^'''
#
# print(penguin * number)

# 6. N школярів ділять K яблук порівну, залишок, що не ділиться, залишається в кошику. Скільки яблук дістанеться
# кожному школяру?
# 6. N schoolchildren divide K apples equally, the remainder that is not divided remains in the basket.
# How many apples will you get? to every student?

number_of_students: int = int(input("Write number of students here: "))
number_of_apples: int = int(input("Write number of apples here: "))

print(f'Each student receives {number_of_apples // number_of_students}')

# 7.N школярів поділили K яблук порівну, залишок, що не ділиться, залишився в кошику. Скільки яблук залишилось у кошику?
# 7. N schoolchildren divided K apples equally, the undivided remainder remained in the basket.
# How many apples are left in the basket?

number_of_students_one: int = int(input("Write number of students here: "))
number_of_apples_one: int = int(input("Write number of apples here: "))

print(f'Left in the cart {number_of_apples_one % number_of_students_one}')

# 8. Оголосити змінну - довжину сторони квадрату. Обчислити площу квадрату і вивести її на екран.
# 8. Declare a variable - the length of the side of the square. Calculate the area of the square and
# display it on the screen.

side_of_a_square: int = 15

print(f'The area of the square is {side_of_a_square ** 2}')

# 9. Дано натуральне число. Виведіть останню цифру.
# 9. A natural number is given. Print the last digit.

value_number: str = input("Write your number here: ")

gen_list = [el for el in value_number if el.isdigit()]
print(gen_list[-1])


# 10. Дано позитивне двозначне число. Знайдіть число десятків у ньому.
# 10. A positive two-digit number is given. Find the number of tens in it.

two_digit_number: int = int(input("Write a positive two-digit number here: "))

answer = two_digit_number // 10

print(f'The number has {answer} tens')

# 11. Запишіть літеру 'A' (латинську, велику) 100 разів поспіль.
# 11. Write the letter 'A' (Latin, capital) 100 times in a row.

print('A' * 100)

# 12. Дано ціле число N. Виведіть наступне за ним парне число.
# 12. Given an integer N. Print the next even number after it.

N: int = int(input("Enter an integer: "))

if N % 2 == 0:
    next_even = N + 2
else:
    next_even = N + 1

print(f"Next for, {N}, even number:, {next_even}")

# 13. Задане число N записали 100 разів поспіль і потім піднести до квадрату. Що вийшло?
# 13. The specified number N was written down 100 times in a row and then squared. What happened?

N: str = input("Write your number here: ")

print(f'Your answer = {int((N * 100)) ** 2}')


# 14. Довжина Київської кільцевої автомобільної дороги – 107 кілометрів. Байкер Вася стартує з нульового кілометра цієї
# дороги та їде зі швидкістю v кілометрів на годину. На якій відмітці він зупиниться через годину?
# 14. The length of the Kyiv ring road is 107 kilometers. Biker Vasya starts from the zero kilometer of this one
# of the road and travels at a speed of v kilometers per hour. At what mark will it stop after an hour?

speed_bike: int = int(input("Write here your speed: "))
start: int = 0
print(f'The biker will stop at a distance of {start + speed_bike} km in one hour.')

# 15. За день машина проїжджає N км. Скільки днів потрібно, щоби проїхати маршрут довжиною M кілометрів?
# 15. A car travels N km per day. How many days does it take to drive a route M kilometers long?

N: int = int(input("Enter the number of kilometers the car drives per day: "))
M: int = int(input("Enter the total length of the route in kilometers: "))

print(f"Number of days required to travel the route = {M // N+1}")
