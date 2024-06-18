"""

Легкий рівень
Easy level

"""

# 1. Дано рядок, що складається зі слів, розділених пробілами. Визначте, скільки у ній слів.
#
# 1. Given a string consisting of words separated by spaces. Determine how many words it contains.

user_strings: str = ("Hello myy friend")

answer: str = user_strings.split(" ")
print(f"A line consists of {len(answer)} words.")

# 2. Дано рядок. Замініть у цьому рядку всі цифри 1 слово one.
#
# 2. Given a string. Replace all numbers 1 in this line with the word one.

string_answer: str = ("Hello. We have 1 users here.")

print(string_answer.replace("1", "one"))


# 3. Дано рядок. Видаліть із цього рядка всі символи @.
#
# 3. Given a string. Remove all @ symbols from this string @.

string_with_dogs:str = "why_@no7@proton.@me"

print(string_with_dogs.replace("@", ""))

# 4. Повернути другу половину рядка.
#
# 4. Turn the second half of the row.

string_hello: str = "Hello world!"

second_half:int = int(len(string_hello) / 2 - 1)
print(string_hello[second_half::])

# 5. Напишіть програму, яка перевіряє, чи введений користувачем рядок містить лише великі літери.
#
# 5. Write a program that checks whether the string entered by the user contains only uppercase
# letters.

user_input: str = input("Write your sentence here: ")

if user_input.isupper():
    print("Your sentence has only uppercase letters.")
else:
    print("Your sentence doesn't have only uppercase letters.")

# 6. Напишіть програму, яка перевіряє, чи введений користувачем рядок містить лише малі літери.
#
# 6. Write a program that checks whether a string entered by the user contains
# only lowercase letters.

first_user_input:str = input("Write here your string: ")

if first_user_input.islower():
    print("Your string has only lowercase latters.")
else:
    print("Your string doesn't have only lowercase latters.")

# 7. Напишіть програму, яка перевіряє, чи введений користувачем рядок закінчується на крапку.
#
# 7. Write a program that checks whether the string entered by the user ends with a period.

string_first: str = "Hello."

if string_first.find(".") == (len(string_first) - 1):
    print("Your sentences end with a full stop")
else:
    print("Your sentences don't end with a full stop")

# 8. Напишіть програму, яка перевіряє, чи введений користувачем рядок закінчується на малу літеру.
#
# 8. Write a program that checks whether a string entered by the user ends with a lowercase letter.

user_input:str = input("Write here your string: ")

if user_input[-1].islower():
    print("Your string ends with a lowercase letter")
else:
    print("Your string isn't ends with a lowercase letter")

# 9. Перевірити, чи є рядок паліндромом (читається однаково зліва направо і справа наліво).
# Наприклад слова: racecar
#
# 9. Check whether the string is a palindrome (reads the same from left to right and
# from right to left). For example, the words: racecar

palindrome_word: str = "racecar"

if palindrome_word[::-1] == palindrome_word:
    print("Your string is a palindrome")
else:
    print("Yor string isn't a palindrome")

# 10. Замінити всі пробіли в рядку на підкреслення.
#
# 10. Replace all spaces in the line with underscores.

text_string: str = "I love my girlfriend!"

print(text_string.replace(" ", "_"))

# 11. Написати програму, яка перетворює кожне слово в рядку так, щоб воно починалося
# з великої літери.
#
# 11. Write a program that converts each word in a string so that it starts with
# with capital letter.

input_string_user: str = input("Write here your strign: ")

print(input_string_user.title())

# 12. Перевірити, чи містить рядок задану підстроку.
#
# 12. Check whether a string contains a given substring.

hello_string: str = "Hello world!"

if "Hello" in hello_string:
    print("Yes")
else:
    print("No")

# 13. Підрахувати кількість слів у рядку.
# 13. Count the number of words in a line.

main_string: str = "The quick brown fox jumps over the lazy dog"

print(len(main_string.split(" ")))

# 14. Написати програму, яка приймає на вхід строку, введену з клавіатури і підраховує кількість
# входження в строку першої літери, з якої починається ця строка.
#
# 14. Write a program that accepts a term entered from the keyboard and counts the number
# entry into the string of the first letter with which this string begins.

input_string = "Hello world Hello World hello world"

list_input = input_string.split(" ")
counter = 0

for i in list_input:
    counter += 1 if i.istitle() else 0

print(counter)

# 15. Дано рядок, що складається рівно із двох слів, розділених пробілом. Переставте ці слова
# подекуди. Результат запишіть у рядок і виведіть рядок, що вийшов.
#
# 15. Given a string consisting of exactly two words separated by a space. Rearrange these words
# in some places. Write the result in a line and display the resulting line.

string_with_two_words: str = "Hello world"

main_text: list = string_with_two_words.split(" ")
print(" ".join(main_text[:: -1]))

# 16. Дано рядок. Замініть у цьому рядку всі появи літери h на літеру H, крім першого та
# останнього входження.
#
# 16. Given a string. Replace all occurrences of the letter h with the letter H in this line,
# except for the first and of last entry.

text: str = "hdkahsadlhlklad"

first: str = text[0]
last: str = text[len(text) - 1]
middle: str = text[1:len(text)-1].replace("h", "H")

print(text)
print(first + middle + last)

"""

Складний рівень
Difficult level

"""

# 1. Напишіть програму для перевірки, чи є номер квитка щасливим. Щасливим квитком вважається той,
# у якого сума перших трьох цифр дорівнює сумі останніх трьох цифр. Наприклад, якщо номер квитка
# складається з шести цифр, такий як 123321, то він є щасливим, оскільки сума перших трьох цифр
#(1 + 2 + 3) дорівнює сумі останніх трьох цифр (3 + 2 + 1).
#
# 1. Write a program to check if the ticket number is lucky. The lucky ticket is the one
# in which the sum of the first three digits is equal to the sum of the last three digits.
# For example, if the ticket number consists of six digits, such as 123321, then it is lucky
# because the sum of the first three digits (1 + 2 + 3) is equal to the sum of the last
# three digits (3 + 2 + 1).

ticket: str = input("Enter your ticket number. Minimum 6 characters: ")

first_three_latter: str = ticket[0:3]
second_back_three_latter: str = ticket[-3:]

first_math: int = 0
second_math: int = 0

for i in first_three_latter:
    first_math += int(i)

for i in second_back_three_latter:
    second_math += int(i)

answer = "You have a lucky ticket" if first_math == second_math else "You don't have lucky ticket"

print(answer)

# 2. Напишіть програму, яка перевіряє, чи введений користувачем рядок містить як великі
# так і малі літери.
#
# 2. Write a program that checks whether the string entered by the user contains uppercase characters
# and lowercase letters.

user_string: str = "This sentence is famous for containing every letter of the English alpha."

if user_string.islower() or user_string.isupper():
    print("All lower latters or all upper latters")
else:
    print("We have correct task")

# 3. Перевірити, чи містить рядок хоча б одну цифру.
#
# 3. Check if a string contains at least one digit.

user_string: str = "123string here"
counter: int = 0

for i in user_string:
    counter += 1 if i.isdigit() else 0

if counter >= 1:
    print(f"The line contains {counter} numbers")
else:
    print("The string does not contain numbers")

# 4. Знайти суму всіх чисел, які знаходяться в рядку.
#
# 4. Find the sum of all the numbers in the row.

user_math_string: str = "126string here"

counter_math: int = 0

for i in user_math_string:
    counter_math += int(i) if i.isdigit() else 0

print(f"The sum of all the numbers in the row = {counter_math}")

# 5. Видалити всі голосні літери з рядка.
#
# 5. Remove all vowels from the string.

english_alphabet: str = "aeiou"
user_math_string: str = "126string here"
new_string:str = ""

for i in user_math_string:
    new_string += i if i not in english_alphabet else ""

print(new_string)

# 6. Знайти найдовше слово в рядку і вивести його.
#
# 6. Find the longest word in the line and display it.

user_string: str = "This sentence is famous for containing every letter of the English alpha."
answer: str = ""

new_string: list = user_string.split(" ")

print(new_string)

for i in new_string:
    answer = i if len(i) > len(answer) else answer

print(f"Я знайти найдовше слово в рядку і вивести його. Ось воно: {answer}")

# 7. Визначити, скільки разів кожна літера зустрічається у введеному рядку.
#
# 7. Determine how many times each letter occurs in the entered string.

input_string: str = "This sentence is famous for containing every letter of the English alpha."
input_string: str = input_string.lower()

letter_counts: dict = {}

for letter in input_string:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

print(letter_counts)

# 8. Порахувати, яка літера найбільш часто зустрічається у вашому прізвищі
#
# 8. Calculate which letter occurs most often in your last name

second_name: str = "Sokolov"
second_name: str = second_name.lower()

second_name_dict: dict = {}

for i in second_name:
    if i in second_name_dict:
        second_name_dict[i] += 1
    else:
        second_name_dict[i] = 1

print(second_name_dict)

# 9.Ввести строку з клавіатури. Видалити з неї всі цифри.
#
# 9.Enter the term from the keyboard. Remove all the numbers from it.

input_user: str = input("Write here your string: ")

answer_string: str = ""

for i in input_user:
    answer_string += "" if i.isdigit() else i

print(answer_string)

# 10. Розділити рядок на слова і вивести їх в порядку зворотньому до алфавітного.
#
# 10. Divide the line into words and display them in reverse alphabetical order.

str_user: str = "J R F A T X K O V W C L Q E Z G S H M B P N U D I Y"

list_string: list = str_user.split(" ")
print(" ".join(sorted(list_string, reverse=True)))

# 11. Визначити, чи є рядок ізограмою (всі літери в рядку є унікальними).
#
# 11. Determine whether a string is an isogram (all letters in a string are unique).

isogram_word: str = "lumberjacks"

answer: set = set()

for i in isogram_word:
    if i in answer:
        print("The {isogram_word} isn't isogram")
    else:
        answer.add(i)
        if len(answer) == len(isogram_word):
            print(f"The {isogram_word} is an isogram")


# 12. Видалити з рядка всі символи, які не є літерами або цифрами.
#
# 12. Remove all characters that are not letters or numbers from a string.

string_str: str = "Hello, World! 123"
result:str = ""

for i in string_str:
    if i.isalnum():
        result += i

print(result)

# 13. Написати програму, яка обертає слова в реченні (але не саме речення).
#
# 13. Write a program that rotates the words in a sentence (but not the sentence itself).

input_string: str = "This sentence is famous for containing every letter of the English alpha."
list_input: list = input_string.split(" ")
answer: list = list()

for i in list_input:
    answer.append(i[::-1])

print(" ".join(answer))

# 14. Знайти різницю між кількістю голосних і приголосних літер у рядку.
#
# 14. Find the difference between the number of vowels and consonants in the string.

input_string: str = "This sentence is famous for containing every letter of the English alpha."
vowels_words:str = "AEIOUaeiou"

counter_firs: int = 0
counter_second: int = 0

for i in input_string:
    if i in vowels_words:
        counter_firs += 1
    else:
        counter_second += 1

if counter_firs > counter_second:
    print("There are more vowels than consonants")
else:
    print("There are more consonant letters than vowels")

# 15. Дано рядок. Якщо у цьому рядку літера f зустрічається лише один раз, виведіть її індекс.
# Якщо вона зустрічається два і більше разів, виведіть індекс її першої та останньої появи.
# Якщо літера f у цьому рядку не зустрічається, нічого не виводьте. При вирішенні цього завдання
# не можна використовувати метод count та цикли.
#
# 15. Given a string. If the letter f occurs only once in this string, print its index.
# If it occurs two or more times, print the index of its first and last occurrence.
# If the letter f does not occur in this string, do not output anything. When solving this task
# count method and loops cannot be used.

s:str = "example of a string with f and another f"

first_index: int = s.find('f')
last_index: int = s.rfind('f')

if first_index == -1:
    pass
elif first_index == last_index:
    print(first_index)
else:
    print(first_index, last_index)

# 16. Дано рядок, в якому літера h зустрічається щонайменше два рази. Видаліть із цього рядка
# перше і останнє входження літери h, а також усі символи, що знаходяться між ними.
#
# 16. Given a line in which the letter h occurs at least twice. Delete from this row
# the first and last occurrence of the letter h and all characters in between.

s = "This is a sample text with h and another h in it."

first_h_index = s.find('h')
last_h_index = s.rfind('h')

s = s.replace(s[last_h_index - 1: last_h_index + 2], "")
s = s.replace(s[first_h_index - 1: first_h_index + 2], "")

print(s)


s = "This is a sample text with h and another h in it."

to_remove = ["Thi", " h "]

for substring in to_remove:
    s = s.replace(substring, "")

print(s)

# 17. Дано рядок. Видаліть із неї всі символи, чиї індекси діляться на 3.Символи рядка
# нумеруються, починаючи з нуля.
#
# 17. Given a string. Remove from it all characters whose indices are divisible by 3.
# The characters of the string are numbered starting from zero.

s: str = "abcdefghijklmnopqrstuvwxyz"

result: str = ""
index: int = 0

for char in s:
    if index % 3 != 0:
        result += char
    index += 1

print(result)

"""

Модульні задачі
Modular tasks

"""
# 1. Дано рядок.
# Спочатку виведіть третій символ цього рядка.
# У другому рядку виведіть передостанній символ цього рядка.
# У третьому рядку виведіть перші п'ять символів цього рядка.
# У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0,
# тому символи виводяться з першого).
# У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
# У сьомому рядку виведіть усі символи у зворотному порядку.
# У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
# У дев'ятому рядку виведіть довжину цього рядка.

string_here: str = "Hello World!"
print(string_here[2])
print(string_here[-2])
print(string_here[0: 6])
print(string_here[0: -2])
print(string_here[0:: 2])
print(string_here[1::2])
print(string_here[::-1])
print(string_here[::-2])
print(len(string_here))
