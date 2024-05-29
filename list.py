'''

Легкий рівень
Easy level

'''

# 1. Створіть порожній список і додайте до нього 10 різних значень.
#
# 1. Create an empty list and add 10 different values ​​to it.

new_list: list = []
new_list = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]

print(new_list)

# 2. Створіть список з 5 чисел і виведіть на екран суму цих чисел.
#
# 2. Create a list of 5 numbers and display the sum of these numbers on the screen.

number_list: list = [1, 2, 3, 4, 5]
sum_math: int = 0

for i in number_list:
    sum_math += i

print(sum_math)

# 3. Створіть список з 6 різних слів і виведіть на екран останнє слово в цьому списку.
#
# 3. Create a list of 6 different words and display the last word in the list.

new_list: list = ["vadym", "Kharkiv", "Dnipro", "Sasha", "Ivan"]

print(new_list[-1])

# 4. Створіть список з 5 чисел і замініть другий елемент на нове значення.
#
# 4. Create a list of 5 numbers and replace the second element with the new value.

num_list: list = [1, 2, 3, 4, 5]
num_list.insert(2, 6)

print(num_list)

# 5. Створіть список з 6 слів і виведіть на екран всі слова, що мають довжину більше 5 символів.
#
# 5. Create a list of 6 words and display all words longer than 5 characters.

name_list: list = ["Ivan4ik", "Petro", "Lida", "Serg", "Dimax", "Max"]

new_list: list = [el for el in name_list if len(el) >= 5]
print(new_list)


# 6. Створіть список з 6 чисел і виведіть на екран всі числа, що більше за середнє
# значення цього списку.
#
# 6. Create a list of 6 numbers and display all numbers greater than the average
# the value of this list.

num_list: list = [12, 9, 35, 1, 45, 19]

average_value: int = sum(num_list) / len(num_list)

new_list: list = [i for i in num_list if i >= average_value]
print(new_list)



# 7. Створіть список з 8 рядків і виведіть на екран всі рядки, що мають довжину менше
# за 10 символів.
#
# 7. Create a list of 8 lines and display all lines less than that
# for 10 characters.

words: list = [
    "Sky",
    "Quiet night",
    "Stars shine bright",
    "Moon's soft light",
    "Gentle",
    "Leaves fall down",
    "shore",
    "Heart's true beat",
    ]

answer_list: list = [el for el in words if len(el) < 10]
print(answer_list)


# 8. Створіть список з 6 чисел і виведіть на екран суму перших трьох чисел в цьому списку.
#
# 8. Create a list of 6 numbers and display the sum of the first three numbers in this list.

num_list: list = [1, 2, 3, 4, 5, 6]
math_answer: int = 0

for index, value in enumerate(num_list):
    if index <= 2:
        math_answer += value

print(math_answer)

print(num_list[0] + num_list[1] + num_list[2])

# 9. Створіть список з 4 рядків і виведіть на екран всі рядки в зворотному порядку.
#
# 9. Create a list of 4 lines and display all the lines in reverse order.

sentences: list = [
    "Sky so blue",
    "Quiet night",
    "Stars shine bright",
    "Moon's soft light",
]

sentences.reverse()

print(sentences)

# 10. Створіть список з 9 чисел і виведіть на екран перше число, яке більше за 5.
#
# 10. Create a list of 9 numbers and display the first number greater than 5.

num_list: list = [12, 2, 1, 45, 3, 15, 9, 4, 5]
new_list: list = []

for i in num_list:
    if i > 5:
        new_list.append(i)
        break

print(new_list)


# 11. Створіть список з 5 рядків і виведіть на екран всі рядки, що мають першу літеру "A".

# 11. Create a list of 5 strings and display all the strings that have the first letter "A"
# on the screen.

senstences: list = [
    "Sky so blue",
    "AQuiet night",
    "Stars shine bright",
    "Moon's soft light",
    "AGentle breeze",
]

for i in senstences:
    if i[0] == "A":
        print(i)


# 12. Створіть список з 6 чисел і виведіть на екран максимальне значення в цьому списку.
#
# 12. Create a list of 6 numbers and display the maximum value in this list.

num_list: list = [1, 2, 3, 4, 5, 6]

print(max(num_list))

# 13. Створіть список з 7 рядків і виведіть на екран всі рядки, що мають останню літеру "s".
#
# 13. Create a list of 7 lines and display all lines that have the last letter "s" on the screen.

senstences: list = [
    "Sky so blues",
    "AQuiet night",
    "Stars shine bright",
    "Moon's soft light",
    "AGentle breezes",
    "Leaves fall down",
    "Waves on shore",
]

for i in senstences:
    if i[-1] == "s":
        print(i)

# 14. Створіть список з 6 чисел і виведіть на екран всі парні числа в цьому списку.
#
# 14. Create a list of 6 numbers and display all even numbers in this list.

number: list = [22, 12, 34, 15, 6, 2]

answer: list = [el for el in number if el % 2 == 0]

print(answer)

# 15. Створіть список з 8 рядків і виведіть на екран всі рядки, що мають другу літеру "o".
#
# 15. Create a list of 8 strings and display all strings that have the second letter "o".

sentences: list = [
    "Sky so blue",
    "Quiet night",
    "Stars shine bright",
    "Moon's soft light",
    "Gentle breeze",
    "Leaves fall down",
    "Waves on shore",
    "Heart's true beat",
]

answer: list = [el for el in sentences if el[1] == "o"]
print(answer)

# 16. Створіть список з 7 чисел і виведіть на екран суму всіх непарних чисел в цьому списку.
#
# 16. Create a list of 7 numbers and display the sum of all odd numbers in this list.

num_list: list = [12, 13, 3, 45, 34, 99, 81]

math_list: list = [el for el in num_list if el % 2 == 1]
print(sum((math_list)))

# 17. Створіть список з 9 рядків і виведіть на екран всі рядки, що мають третю літеру "e".
#
# 17. Create a list of 9 strings and display all strings that have the third letter "e".

sentences: list = [
    "Sky so blue",
    "Quiet night",
    "Stars shine bright",
    "Moon's soft light",
    "Gentle breeze",
    "Leaves fall down",
    "Waves on shore",
    "Heart's true beat",
    "Dreaming free",
]

for i in sentences:
    if i[-2] == "e":
        print(i)

# 18. Створіть список з 6 чисел і виведіть на екран суму останніх трьох чисел в цьому списку.
#
# 18. Create a list of 6 numbers and display the sum of the last three numbers in this list.

num_list: list = [23, 15, 95, 2, 25, 14]

print(sum(num_list[: -4: -1]))

# 19. Створіть список з 5 рядків і виведіть на екран всі рядки, що мають довжину більше
# за перший рядок у списку.
#
# 19. Create a list of 5 lines and display all lines longer than that
# for the first line in the list.

sentences: list = [
    "Sky so blue",
    "Quiet night",
    "Stars shine bright",
    "Moon's soft light",
    "Gentle breeze",
]

len_first_sentence: int = len(sentences[0])

for i in sentences:
    if len(i) > len_first_sentence:
        print(i)

# 20. Створіть список з 7 чисел і виведіть на екран всі числа, які менші за середнє
# значення цього списку.`
#
# 20. Create a list of 7 numbers and display all numbers that are less than the average
# the value of this list.`

num_list: list = [12, 65, 1, 13, 76, 54, 2]

math_sum: int = sum(num_list) / len(num_list)

for i in num_list:
    if i < math_sum:
        print(i)

# 21. Напишіть програму, яка знаходить найбільш довге слово у списку.
#
# 21. Write a program that finds the longest word in a list.

words: list = ["Sky", "Quiet", "Stars", "Moon", "Breezem", "Leaves", "Waves", "Heart"]

print(max(words, key=len))

# 22. Напишіть програму, яка знаходить найкоротше слово у списку.
#
# 22. Write a program that finds the shortest word in a list.

words: list = ["Sky", "Quiet", "Stars", "Moon", "Breezem", "Leaves", "Waves", "Heart"]

print(min(words, key=len))

# 23. Напишіть програму, яка приймає список чисел і друкує числа які
# парні numbers = [7, 12, 0, 14, 5, 10]
#
# 23. Write a program that accepts a list of numbers and prints which numbers
# even numbers = [7, 12, 0, 14, 5, 10]

user_input: str = input("Write here your list numbers: ")

list_user_input:str = user_input.split(" ")

even_numbers: list = [el for el in list_user_input if int(el) % 2 == 0]

print(even_numbers)


"""

Складний рівень
Difficult level

"""

# 1. Створити список материків західної півкулі. Доповнити список материками зі східної півкулі.
# Відсортувати материки за алфавітом і вивести на екран
#
# 1. Create a list of the continents of the Western Hemisphere. Complete the list with continents
# from the Eastern Hemisphere.Sort the continents alphabetically and display them on the screen

# 2. Порівняти, чи перша літера імені співпадає з першою літерою прізвища і вивести відповідне
# повідомлення.
#
# 2. Compare whether the first letter of the name matches the first letter of the surname and
# output the corresponding one messages.

# 3. Таблицю Піфагора помістити в двовимірний список, де кожне число буде елементом списка
#
# 3. Place the Pythagorean table in a two-dimensional list, where each number will be
# an element of the list

# 4. Виведіть елементи цього списку у зворотному порядку, не змінюючи сам список.
#
# 4. Output the elements of this list in reverse order without changing the list itself.

# 5. Напишіть програму, яка знаходить у масиві елемент, найближчий за величиною до цього числа.
#
# 5. Write a program that finds the element in the array that is closest in size to this number.

# 6. У списку всі елементи різні різні. Поміняйте місцями мінімальний та максимальний елемент
# цього списку.
#
# 6. In the list, all the elements are different. Swap the minimum and maximum elements
# of this list.

# 7. Даний список заповнений довільними цілими числами. Знайдіть у списку два числа, добуток
# яких максимально. Виведіть ці числа в порядку невтрати.
#
# 7. This list is filled with arbitrary integers. Find the product of two numbers in the list
# of which is the maximum. Output these numbers in lossless order.

# 8. Дано список. Виведіть ті елементи, які зустрічаються у списку лише один раз.
# Елементи потрібно виводити в порядку, в якому вони зустрічаються в списку.
#
# 8. Given a list. Output those elements that occur in the list only once.
# Items must be displayed in the order they appear in the list.

# 9. Наведено список цілих чисел. Потрібно "стиснути" його, перемістивши всі ненульові
# елементи в ліву частину списку, не змінюючи їхній порядок, а всі нулі - у праву частину.
# Порядок ненульових елементів не можна змінювати, додатковий список використовувати не можна,
# завдання потрібно виконати за один прохід по списку. Надрукуйте отриманий список.
#
# 9. Given a list of integers. It is necessary to "compress" it by moving all non-zeros
# elements to the left part of the list without changing their order, and all zeros to the right
# part. The order of non-zero elements cannot be changed, an additional list cannot be used,
# the task must be completed in one pass through the list. Print the resulting list.

# 10. Дано список. Не змінюючи його та не використовуючи додаткові списки, визначте,
# яке число у цьому списку зустрічається найчастіше. Якщо таких чисел декілька,
# виведіть будь-яке з них.
#
# 10. Given a list. Without changing it and without using additional lists, determine
# which number in this list occurs most often. If there are several such numbers,
# output any of them.
