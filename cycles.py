'''

Легкий рівень
Easy Level

'''

# 1. Надрукувати числа від 1 до 7. Результатом виконання цієї програми буде стовпчик чисел: 1,2,
# 3, 4, 5, 6, 7
#
# 1. Print numbers from 1 to 7. The result of this program will be a column of numbers: 1,2,
# 3, 4, 5, 6, 7

for i in range(1, 7):
    print(i)

# 2. Надрукувати числа від 1 до 20 у рядок. Результатом виконання цієї програми буде рядок чисел:
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#
# 2. Print numbers from 1 to 20 in a line. The result of executing this program will be a string
# of numbers: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

for i in range(1, 21):
    print(i ,end=" ")

# 3. Виведіть повідомлення Hello, Python! на екран n разів (n - ціле число, яке вводить користувач).
# Вхідні дані: 3
# Вихідні дані:
# Hello, Python!
# Hello, Python!
# Hello, Python!
#
# 3. Print Hello, Python! on the screen n times (n is an integer entered by the user).
# Input data: 3
# Output data:
# Hello, Python!
# Hello, Python!
# Hello, Python!

user_input = int(input("Write here your number: "))

for i in range(user_input):
    print("Hello, Python!")

# 4. З клавіатури вводиться число n. Знайти добуток чисел від 1 до цього числа. 1*2*3*…*n.
# Для початкового значення добутку змінній надаємо значення один. Вхідні дані: 5.
# Вихідні дані: 120
#
# 4. The number n is entered from the keyboard. Find the product of numbers from 1 to this number. 1*2*3*...*n.
# For the initial value of the product, we assign the value one to the variable. Input data: 5.
# Output: 120

number = 5
multiplication = 1

for i in range(1, number+1):
    multiplication = multiplication * i

print(multiplication)

# 5. Скласти програму, яка виведе на екран квадрати всіх цифр у порядку зростання.
#
# 5. Write a program that will display the squares of all numbers in ascending order.
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81

for i in range(10):
    print(i * i)

# 6. Напишіть програму-таймер зворотного відліку, яка запитує у користувача кількість секунд n,
# з якої слід починати відлік. Вхідні дані: 5
# Вихідні дані:
#
# 6. Write a countdown timer program that prompts the user for n seconds,
# from which the countdown should start. Input data: 5
# Output data:
# 5
# 4
# 3
# 2
# 1
# Start!

n = int(input("Write here number: "))

while n > 0:
    print(n)
    n -= 1

print("Start!")

# 7. Надрукувати у рядку m разів число n. Числа m і n - цілі числа, які вводить користувач у
# порядку n, m. Вхідні дані:
# 10
# 5
# Вихідні дані:
# 10 10 10 10 10
#
# 7. Print the number n in a line m times. The numbers m and n are integers entered by the user
# of order n, m. Incoming data:
# 10
# 5
# Output data:
# 10 10 10 10 10

m = int(input("Write here M number: "))
n = int(input("Write here N number: "))

for i in range(n):
    print(m, end=" ")

# 8. Надрукувати всі двоцифрові числа, у яких остання цифра дорівнює n - ціле число, яке вводить
# користувач. Вхідні дані: 3
# Вихідні дані: 13 23 33 43 53 63 73 83 93
#
# 8. Print all two-digit numbers in which the last digit is n - an integer that enters
# user. Input data: 3
# Output data: 13 23 33 43 53 63 73 83 93

number = int(input("Write here your number: "))

for i in range(10, 100):
    if i % 10 == number:
        print(i, end=" ")

# 9. За цим цілим числом N роздрукуйте всі квадрати натуральних чисел, що не перевищують N,
# у порядку зростання. Вхідні дані: 50
# Вихідні дані:
# 1 4 9 16 25 36 49
#
# 9. Given this integer N, print all squares of natural numbers not exceeding N,
# in ascending order. Input data: 50
# Output data:
# 1 4 9 16 25 36 49

number = 50
number_one = 1

for i in range(1, number):
    if number - 1 > number_one:
        number_one = i * i
        print(number_one, end=" ")
    else:
        break

# 10. Визначте суму всіх елементів послідовності, що завершується числом 0.
#
# 10. Determine the sum of all elements of the sequence ending with the number 0.

sequence = [10, 12, 2, 40, 45, 100, 99, 70]
total = 0

for i in sequence:
    if str("0") in str(i):
        total += i

print(total)

'''

Складний рівень
Difficult level

'''
