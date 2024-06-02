'''

Легкий рівень
Easy level

'''

# # 1. Написати програму, яка зчитує дані з текстового файлу і виводить їх на екран.
# #
# # 1. # 1. Write a program that reads data from a text file and displays it on the screen.

# with open('test.txt', 'r', encoding='utf-8') as text:
#     print(text.read())

# # 2. Написати програму, яка зчитує дані з текстового файлу і записує їх у новий файл, перетворивши
# # кожне слово на малі літери.
# #
# # 2. Write a program that reads data from a text file and writes it to a new file, converting
# # lowercase each word.

# with open('test.txt', 'r', encoding='utf-8') as file:
#     text = file.read()

# with open('test_two.txt', 'w', encoding='utf-8') as test:
#     test.write(text)

# # 3. Написати програму, яка зчитує дані з текстового файлу і підраховує кількість слів у файлі.
# #
# #  3. Write a program that reads data from a text file and counts the number of words in the file.

# with open('test.txt', 'r', encoding='utf-8') as test:
#     text = test.read()
#     print(f"In the text {len(text.split(" "))} words")

# # 4. Відкрити файл з назвою "data.txt" у режимі запису та дописати у нього
# # рядок "Python is awesome!".
# #
# # 4. Open the file named "data.txt" in write mode and add to it
# # line "Python is awesome!".

# with open('data.txt', 'w', encoding='utf-8') as write_text:
#     write_text.write("Python is awesome!")

# # 5. Відкрити файл з назвою "data.txt" у режимі читання та вивести кількість рядків у файлі.
# #
# # 5. Open the file named "data.txt" in reading mode and display the number of lines in the file.

# line_conter = 0

# with open('data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         line_conter += 1

# print(f'Number of lines in file: {line_conter}')

'''

Складний рівень

'''

# 1. Дано словник, який містить «Прізвище»-«оцінка». На його основі створити новий словник,
# який буде містити лише учнів, які навчаються на 4 та 5. Результат вивести на екран,
# а також записати у файл з назвою student.txt

# 2. Відкрити файл з назвою "data.txt" у режимі читання та вивести перші 5 символів з файлу.

# 3. Відкрити файл з назвою "data.txt" у режимі читання та вивести останні 5 символів з файлу.

# 4. Відкрити файл з назвою "data.txt" у режимі читання та вивести тільки рядки, які містять слово
# "Python". разом з прикладом та файликом.
