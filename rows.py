# 1. Дано рядок, що складається зі слів, розділених пробілами. Визначте, скільки у ній слів.
# 1. Given a string consisting of words separated by spaces. Determine how many words it contains.

user_strings: str = ("Hello myy friend")

answer: str = user_strings.split(" ")
print(f"A line consists of {len(answer)} words.")

# 2. Дано рядок. Замініть у цьому рядку всі цифри 1 слово one.
# 2. Given a string. Replace all numbers 1 in this line with the word one.

string_answer: str = ("Hello. We have 1 users here.")

print(string_answer.replace("1", "one"))


# 3. Дано рядок. Видаліть із цього рядка всі символи @.
# 3. Given a string. Remove all @ symbols from this string @.

string_with_dogs:str = "why_@no7@proton.@me"

print(string_with_dogs.replace("@", ""))

# 4. Повернути другу половину рядка.
# 4. Turn the second half of the row.

string_hello: str = "Hello world!"

second_half:int = int(len(string_hello) / 2 - 1)
print(string_hello[second_half::])

# 5. Напишіть програму, яка перевіряє, чи введений користувачем рядок містить лише великі літери.
# 5. Write a program that checks whether the string entered by the user contains only uppercase
# letters.

user_input: str = input("Write your sentence here: ")

if user_input.isupper():
    print("Your sentence has only uppercase letters.")
else:
    print("Your sentence doesn't have only uppercase letters.")

# 6. Напишіть програму, яка перевіряє, чи введений користувачем рядок містить лише малі літери.
# 6. Write a program that checks whether a string entered by the user contains
# only lowercase letters.

first_user_input:str = input("Write here your string: ")

if first_user_input.islower():
    print("Your string has only lowercase latters.")
else:
    print("Your string doesn't have only lowercase latters.")

# 7. Напишіть програму, яка перевіряє, чи введений користувачем рядок закінчується на крапку.
# 7. Write a program that checks whether the string entered by the user ends with a period.

string_first: str = "Hello."

if string_first.find(".") == (len(string_first) - 1):
    print("Your sentences end with a full stop")
else:
    print("Your sentences don't end with a full stop")

# 8. Напишіть програму, яка перевіряє, чи введений користувачем рядок закінчується на малу літеру.
# 8. Write a program that checks whether a string entered by the user ends with a lowercase letter.

user_input:str = input("Write here your string: ")

if user_input[-1].islower():
    print("Your string ends with a lowercase letter")
else:
    print("Your string isn't ends with a lowercase letter")

# 9. Перевірити, чи є рядок паліндромом (читається однаково зліва направо і справа наліво).
# Наприклад слова: racecar
# 9. Check whether the string is a palindrome (reads the same from left to right and
# from right to left). For example, the words: racecar

palindrome_word: str = "racecar"

if palindrome_word[::-1] == palindrome_word:
    print("Your string is a palindrome")
else:
    print("Yor string isn't a palindrome")

# 10. Замінити всі пробіли в рядку на підкреслення.
# 10. Replace all spaces in the line with underscores.

text_string: str = "I love my girlfriend!"

print(text_string.replace(" ", "_"))

# 11. Написати програму, яка перетворює кожне слово в рядку так, щоб воно починалося
# з великої літери.
# 11. Write a program that converts each word in a string so that it starts with
# with capital letter.

input_string_user: str = input("Write here your strign: ")

print(input_string_user.title())

# 12. Перевірити, чи містить рядок задану підстроку.
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
# 15. Given a string consisting of exactly two words separated by a space. Rearrange these words
# in some places. Write the result in a line and display the resulting line.

string_with_two_words: str = "Hello world"

main_text: list = string_with_two_words.split(" ")
print(" ".join(main_text[:: -1]))

# 16. Дано рядок. Замініть у цьому рядку всі появи літери h на літеру H, крім першого та
# останнього входження.
# 16. Given a string. Replace all occurrences of the letter h with the letter H in this line,
# except for the first and of last entry.

text: str = "hdkahsadlhlklad"

first: str = text[0]
last: str = text[len(text) - 1]
middle: str = text[1:len(text)-1].replace("h", "H")

print(text)
print(first + middle + last)
