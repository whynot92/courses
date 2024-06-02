'''

Легкий рівень
Easy Level

'''

# # 1. Надрукувати числа від 1 до 7. Результатом виконання цієї програми буде стовпчик чисел: 1,2,
# # 3, 4, 5, 6, 7
# #
# # 1. Print numbers from 1 to 7. The result of this program will be a column of numbers: 1,2,
# # 3, 4, 5, 6, 7

# for i in range(1, 7):
#     print(i)

# # 2. Надрукувати числа від 1 до 20 у рядок. Результатом виконання цієї програми буде рядок чисел:
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# #
# # 2. Print numbers from 1 to 20 in a line. The result of executing this program will be a string
# # of numbers: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# for i in range(1, 21):
#     print(i ,end=" ")

# # 3. Виведіть повідомлення Hello, Python! на екран n разів (n - ціле число, яке вводить користувач).
# # Вхідні дані: 3
# # Вихідні дані:
# # Hello, Python!
# # Hello, Python!
# # Hello, Python!
# #
# # 3. Print Hello, Python! on the screen n times (n is an integer entered by the user).
# # Input data: 3
# # Output data:
# # Hello, Python!
# # Hello, Python!
# # Hello, Python!

# user_input = int(input("Write here your number: "))

# for i in range(user_input):
#     print("Hello, Python!")

# # 4. З клавіатури вводиться число n. Знайти добуток чисел від 1 до цього числа. 1*2*3*…*n.
# # Для початкового значення добутку змінній надаємо значення один. Вхідні дані: 5.
# # Вихідні дані: 120
# #
# # 4. The number n is entered from the keyboard. Find the product of numbers from 1 to this number.
# # 1*2*3*...*n. For the initial value of the product, we assign the value one to the variable.
# # Input data: 5.
# # Output: 120

# number = 5
# multiplication = 1

# for i in range(1, number+1):
#     multiplication = multiplication * i

# print(multiplication)

# # 5. Скласти програму, яка виведе на екран квадрати всіх цифр у порядку зростання.
# #
# # 5. Write a program that will display the squares of all numbers in ascending order.
# # 0
# # 1
# # 4
# # 9
# # 16
# # 25
# # 36
# # 49
# # 64
# # 81

# for i in range(10):
#     print(i * i)

# # 6. Напишіть програму-таймер зворотного відліку, яка запитує у користувача кількість секунд n,
# # з якої слід починати відлік. Вхідні дані: 5
# # Вихідні дані:
# #
# # 6. Write a countdown timer program that prompts the user for n seconds,
# # from which the countdown should start. Input data: 5
# # Output data:
# # 5
# # 4
# # 3
# # 2
# # 1
# # Start!

# n = int(input("Write here number: "))

# while n > 0:
#     print(n)
#     n -= 1

# print("Start!")

# # 7. Надрукувати у рядку m разів число n. Числа m і n - цілі числа, які вводить користувач у
# # порядку n, m. Вхідні дані:
# # 10
# # 5
# # Вихідні дані:
# # 10 10 10 10 10
# #
# # 7. Print the number n in a line m times. The numbers m and n are integers entered by the user
# # of order n, m. Incoming data:
# # 10
# # 5
# # Output data:
# # 10 10 10 10 10

# m = int(input("Write here M number: "))
# n = int(input("Write here N number: "))

# for i in range(n):
#     print(m, end=" ")

# # 8. Надрукувати всі двоцифрові числа, у яких остання цифра дорівнює n - ціле число, яке вводить
# # користувач. Вхідні дані: 3
# # Вихідні дані: 13 23 33 43 53 63 73 83 93
# #
# # 8. Print all two-digit numbers in which the last digit is n - an integer that enters
# # user. Input data: 3
# # Output data: 13 23 33 43 53 63 73 83 93

# number = int(input("Write here your number: "))

# for i in range(10, 100):
#     if i % 10 == number:
#         print(i, end=" ")

# # 9. За цим цілим числом N роздрукуйте всі квадрати натуральних чисел, що не перевищують N,
# # у порядку зростання. Вхідні дані: 50
# # Вихідні дані:
# # 1 4 9 16 25 36 49
# #
# # 9. Given this integer N, print all squares of natural numbers not exceeding N,
# # in ascending order. Input data: 50
# # Output data:
# # 1 4 9 16 25 36 49

# number = 50
# number_one = 1

# for i in range(1, number):
#     if number - 1 > number_one:
#         number_one = i * i
#         print(number_one, end=" ")
#     else:
#         break

# # 10. Визначте суму всіх елементів послідовності, що завершується числом 0.
# #
# # 10. Determine the sum of all elements of the sequence ending with the number 0.

# sequence = [10, 12, 2, 40, 45, 100, 99, 70]
# total = 0

# for i in sequence:
#     if str("0") in str(i):
#         total += i

# print(total)

'''

Складний рівень
Difficult level

'''
# # 1. Яблука лежать на прилавку у вигляді піраміди: 1 ряд одне яблуко, другий ряд  - два і т.д.
# # Скільки яблук на прилавку? Вхідні дані: 150
# # Вихідні дані: 11325
# #
# # 1. Apples lie on the counter in the form of a pyramid: one apple in the first row, two apples
# # in the second row, etc. How many apples are on the counter? Input data: 150
# # Output: 11325

# number = 150
# sum = 0

# for i in range(1, number + 1):
#     sum += i

# print(sum)

# # 2. Одноклітинна амеба ділиться навпіл кожні 3 години. Визначити скільки буде амеб через 3,6,9,12,
# #  ... , 24 години
# #
# # 2. A single-celled amoeba divides in half every 3 hours. Determine how many amoeba there
# # will be after 3,6,9,12, ... , 24 hours

# ameba = 2

# for i in range(3, 25, 3):
#     print(f"In {i} hours there will be {ameba} amoeba. ")
#     ameba *= 2

# # 3. Надрукувати вигляд прилавку:
# #
# # 3. Print the view of the counter:
# #
# # 3.1:
# # @
# # @ @
# # @ @ @
# # @ @ @ @
# # @ @ @ @ @

# icon = "@ "

# for i in range(1, 6):
#     print(icon)
#     icon += "@ "

# # 3.2:
# #         @
# #       @ @
# #     @ @ @
# #   @ @ @ @
# # @ @ @ @ @

# icon = " @"

# for i in range(1, 6):
#     print("{:>10}".format(icon))
#     icon += " @"

# # 3.3:
# #     @
# #    @ @
# #   @ @ @
# #  @ @ @ @
# # @ @ @ @ @

# icon = " @"

# for i in range(1, 6):
#     print("{:^10}".format(icon))
#     icon += " @"

# #          *
# #         * *
# #        * * *
# #       * * * *
# #      * * * * *
# #     * * * * * *
# #    * * * * * * *
# #   * * * * * * * *
# #  * * * * * * * * *

# icon = " *"

# for i in range(1, 10):
#     print("{:^18}".format(icon))
#     icon += " *"

# # 3.4:
# # * * * * * * * * * *
# #   * * * * * * * * *
# #     * * * * * * * *
# #       * * * * * * *
# #         * * * * * *
# #           * * * * *
# #             * * * *
# #               * * *
# #                 * *
# #                   *
# counter = 10
# icon = " *" * counter


# for i in range(1, 11):
#     print("{:>20}".format(icon))
#     counter -= 1
#     icon = " *" * counter

# # 3.5:
# # * * * * * * * * * *
# # * * * * * * * * *
# # * * * * * * * *
# # * * * * * * *
# # * * * * * *
# # * * * * *
# # * * * *
# # * * *
# # * *
# # *

# counter = 10
# icon = "* " * counter


# for i in range(1, 11):
#     print("{:20}".format(icon))
#     counter -= 1
#     icon = "* " * counter

# # 3.6:

# icon = "**"

# for i in range(1, 10):
#     print("{:^18}".format(icon))
#     icon += "**"

# # 4. Напишіть програму, яка друкує цілі числа від 1 до n (1 < n ≤ 1000) з такою умовою: для чисел
# #кратних 3 виводить *3* замість числа, для чисел кратних 5 друкує *5*, а для чисел,
# # які кратні 3 і 5 одночасно, повідомлення буде *35*. Вхідні дані: 16
# # Вихідні дані:
# #
# # # 4. Write a program that prints integers from 1 to n (1 < n ≤ 1000) with the following
# # condition: for numbers multiples of 3 prints *3* instead of a number, for numbers that are
# # multiples of 5 it prints *5*, and for numbers, which are multiples of 3 and 5 at the same time,
# # the message will be *35*. Input data: 16
# # Output data:
# # 1
# # 2
# # *3*
# # 4
# # *5*
# # *3*
# # 7
# # 8
# # *3*
# # *5*
# # 11
# # *3*
# # 13
# # 14
# # *35*
# # 16

# number = int(input("Write here your number: "))

# for i in range(1, number + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("*35*")
#     elif i % 3 == 0:
#         print("*3*")
#     elif i % 5 == 0:
#         print("*5*")
#     else:
#         print(i)

# # 5.1 Напишіть програму для обчислення виразу 1/2 + 2/3 + 3/4 + …​ + n/(n + 1) із заданим n,
# # яке вводить користувач (n > 0). Вхідні дані: 3. Вихідні дані: 1.9166666666666665
# #
# # 5.1 Write a program to calculate the expression 1/2 + 2/3 + 3/4 + …​ + n/(n + 1) given n,
# # which is entered by the user (n > 0). Input data: 3. Output data: 1.9166666666666665

# number = int(input("Write here your number > 0: "))

# answer = 0

# for i in range(1, number + 1):
#     answer += i / (i + 1)

# print(answer)

# # 5.2 При заданому користувачем значенні цілого числа n ≥ 2 обчислити вираз
# # 1 × 2 + 2 × 3 + …​ + (n - 1) × n. Вхідні дані: 3. Вихідні дані: 8
# #
# # 5.2 Calculate the expression given by the user for the value of an integer n ≥ 2
# # 1 × 2 + 2 × 3 + … + (n - 1) × n. Input data: 3. Output data: 8

# answer = 0

# for i in range(1, number):
#     answer += i * (i + 1)

# print(answer)

# # 6. Напишіть програму для побудови шаблону як у вихідних даних за введеним значенням n.
# # Вхідні дані:8.
# # Вихідні дані:
# #
# # 6. Write a program to build a pattern as in the input data for the input value of n.
# # Input data: 8.
# # Output data:
# # 1
# # 22
# # 333
# # 4444
# # 55555
# # 666666
# # 7777777
# # 88888888

# num = int(input("Write here your number: "))

# for i in range(1, num + 1):
#     print(str(i) * i)

# # 7. Надрукувати таблицю відповідності між масою у фунтах і масою в кілограмах для значень n
# # фунтів (1 фунт = 453 г) у вигляді таблиці. Вхідні дані: 5
# # Вихідні дані:
# #
# # 7. Print a table of correspondence between mass in pounds and mass in kilograms for values ​​of n
# # pounds (1 pound = 453 g) in tabular form. Input data: 5
# # Output data:
# # 1   0.453
# # 2   0.906
# # 3   1.359
# # 4   1.812
# # 5   2.265

# num = int(input("Write here number of pounds: "))

# pounds_to_kg = 0.453

# for i in range(1, num + 1):
#     kg = i * pounds_to_kg
#     print(f"{i}\t{kg}")


# # 8. Першого дня спортсмен пробіг X кілометрів, а потім він щодня збільшував пробіг на 10%
# # від попереднього значення (для вирішення завдання дозволяється використовувати числа з комою,
# # які в Пітоні пишуться через точку). За даним числом X визначте номер дня, який пробіг
# # спортсмена становитиме щонайменше Y кілометрів.
# #
# # 8. On the first day, the athlete ran X kilometers, and then he increased the mileage by 10%
# # every day from the previous value (to solve the problem, it is allowed to use numbers
# # with a comma, which in Python are written through a dot). From the given number X, determine
# # the number of the day that has passed of the athlete will be at least Y kilometers.

# X = float(input("Write here km in first day: "))
# days = 1
# distance = X

# Y = float(input("Write here finish km.: "))

# while distance < Y:
#     days += 1
#     distance += distance * 10 / 100

# print(f"The sportsman will reach a distance of at least", {Y}, "kilometers on day", {days})

# # 9. Послідовність складається з цілих чисел і завершується числом 0. Визначте значення
# # найбільшого елемента послідовності.
# # Вхідні дані:
# #
# # 9. The sequence consists of integers and ends with the number 0. Determine the value
# # of the largest element of the sequence.
# # Incoming data:
# # 1
# # 7
# # 9
# # 0
# # Виведення програми:
# #
# # Program output:
# # 9


# max_number = 0

# while True:
#     num = int(input("Enter a number (0 to stop): "))

#     if num == 0:
#         break

#     if num > max_number:
#         max_number = num

# print("The maximum number is:", max_number)

'''

Модульні задачі
Modular tasks

'''

# # 1. Гра, вгадай число
# # Користувач запускає програму, компютер загадує число від 1 - 100, користувач має вгадати число.
# # Також вивести відповідне повідомлення, чи число менше чи більше загаданого, якщо користувач
# # вгадав число, то привітати його.
# # Додатково:
# # надати користувачеві лише 7 спроб, якщо він за 7 спроб не вгадає число написати що він програв.
# #
# # 1. Guess the number game
# # The user starts the program, the computer guesses a number from 1 - 100, the user must guess
# # the number. Also display a corresponding message, whether the number is less or more than
# # the guessed one, if the user guessed the number, then congratulate him.
# # Additionally:
# # give the user only 7 attempts, if he does not guess the number in 7 attempts, write that he lost.

# import random

# counter = 7
# number_sicret = random.randint(1, 101)

# print("#" * 57)
# print("\n")
# print(f"You have {counter } attempts to guess the number")
# print("\n")
# print("#" * 57)

# while counter > 0:
#     user_number = int(input("Write here your number from 0 to 100: "))
#     if user_number > number_sicret:
#         print("Your number is more than the computer guessed")
#         counter -= 1
#         print(f"You have {counter} attempts left")
#         print("#" * 57)
#     elif user_number < number_sicret:
#         print("Your number is less than the computer guessed")
#         counter -= 1
#         print(f"You have {counter} attempts left")
#         print("#" * 57)
#     else:
#         print("You win!!!!")
#         print(f"You have used {7 - counter} attempts")
#         break
# else:
#     print("\n")
#     print("Sorry you loos in this game! Maybe later!")
#     print("\n")

# 2. Гра, вгадай слово
# Задано список слів, потрібно вгадати загадане рандомне слово, якщо користувач вводить букву і
# вона є в слові то вивести повідомлення що ця буква є в слові, якщо користувач вводить повторну
# ту саму буква то вивести повідомлення що ви вже вводили цю букву, якщо всі букви вгадано,
# вивести повідомлення що ви відгадали слово.
#
# 2. Guess the word game
# Given a list of words, you need to guess the guessed random word if the user enters the letter i
# it is in the word, then display a message that this letter is in the word, if the user enters
# a repeated one the same letter, then display a message that you have already entered this
# letter, if all the letters have been guessed, display a message that you guessed the word.
import random

secret_words = ["laptop", "watch", "clock", "apple"]
random_word = random.choice(secret_words)

word_template = "_ " * len(random_word)
list_secret = word_template.split(" ")
list_secret.remove("")

# print(random_word)

while True:
    print("#" * 40)
    print(f"\n")
    input_user = input("Write the letter of the word, and I will say whether it is or not:")
    print(f"\n")
    if input_user in random_word:
        print("#" * 40)
        print(f"\n")
        print(f"There are {random_word.count(input_user)} letters '{input_user.upper()}' in the word.")
        for index, value in enumerate(random_word):
            if input_user == value:
                list_secret[index] = value
        print(f"\n")
        print(" ".join(list_secret))
        print(f"\n")
    else:
        print("#" * 40)
        print(f"\n")
        print(f"The letter '{input_user.upper()}' is not in this word")
        print("")
        print(" ".join(list_secret))
        print(f"\n")
    if "".join(list_secret) == random_word:
        print("#" * 40)
        print(f"\n")
        print("Finish")
        print(f"\n")
        print("#" * 40)
        break

# 3. Гра кімнати
# Потрібно придумати власну гру в кімнати
# Наприклад:
# Є 5 кімнат, в кожній кімнаті по 3 дверей, в одній з дверей вогонь, інші безпечні,
# треба пройти всі кімнати.

# 4. Написати програму яка дозволяє додавати, видаляти товар, переглядати товар,
# очищувати весь список, та виходити з програми. Також щоб в низу в таблиці була сума
# вартості всіх товарів.
# ----------------------------------------------------------------------------------------------
# |  №  | Товар                                     |        кількість  |            вартість  |
# ----------------------------------------------------------------------------------------------
# |  1  | Апельсин                                  |                 6 |                 150  |
# |  2  | Лимон                                     |                 8 |                  90  |
# |  3  | Картопля                                  |               123 |                 445  |
# ----------------------------------------------------------------------------------------------
# | Продано всього                                                      |                 685  |
# ----------------------------------------------------------------------------------------------
