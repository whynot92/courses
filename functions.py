'''

Легкий рівень
Easy level

'''

# 1. Нехай у вас є змінні, які приймають ім'я та прізвище студента, номер його курсу. Створіть
# функцію, яка виведе значення цих змінних на екран. При цьому нехай прізвище виводиться у
# верхньому регістрі, а ім'я - тільки перша буква.
#
# 1. Let you have variables that accept the student's first and last name, his course number. Create
# a function that will print the values ​​of these variables to the screen. At the same time,
# let the last name be displayed in in upper case, and the name - only the first letter.
# Вхідні дані:
#
# Incoming data:
# Shelder
# Tomas
# 5
#
# Вихідні дані:
#
# Output data:
# SHELDER
# T
# 5

def curses(a, b, c):
    return print(f'{a.upper()}\n{b[0]}\n{c}')

curses("Shelder", "Tomas", 5)

# 2. Зробіть функцію, яка виводитиме площу прямокутника.
#
# 2. Make a function that will output the area of ​​a rectangle.

def area_of_rectangle(a, b):
    answer = (a + b) * 2
    return answer

print(area_of_rectangle(2, 5))


# 3. Зробіть функцію, яка параметром прийматиме рядок і повертатиме кортеж її символів.
#
# 3. Make a function that takes a string as a parameter and returns a tuple of its characters.

def tuple_def(a: str) -> tuple:
    answer = list()
    for i in a:
        answer.append(i)
    return tuple(answer)

print(tuple_def("hello world"))

# 4. Створіть функцію, яка перевірятиме два числа. Нехай вона виводить повідомлення про те, яке з
# них більше за інше або якщо вони рівні один одному за значенням.
#
# 4. Create a function that checks two numbers. Let it output a message about which of the
# they are greater than the other or if they are equal to each other in value.

def equality(a, b):
    if a > b:
        return print(f'The first number {a} is greater than the second {b}')
    elif a < b:
        return print(f'The second {b} number is greater than the first {a}')
    else:
        return print(f"The first {a} and second numbers {b} are the same")

equality(4,4)

# 5. Зробіть функцію, яка перевірятиме тип змінної і якщо вона є числом, то перетворить її на рядок.
#
# 5. Make a function that will check the type of the variable and if it is a number, then convert
# it to a string.


def audit(a):
    if type(a) == type(int()):
        return print(f"The argument {a} is a number. That's why we make it a line {str(a)=}")
    elif type(a) == type(str()):
        return print(f"The argument {a} is a string")

audit(2)

# 6. Зробіть функцію, що заповнює список парними числами 1 від заданого.
#
# 6. Make a function that fills the list with even numbers 1 from the given one.

user_list = list()

def random_number():
    for i in range(1, 101):
        if i % 2 == 0:
            user_list.append(i)

    return user_list

random_number()
print(user_list)

# 7. Нехай у вас є словник, в якому як ключі зберігаються імена користувачів, а як значення - їх
# вік. Створіть функцію, яка виведе всі пари ключ-значення у вигляді кортежу.
#
# 7. Let you have a dictionary that stores usernames as keys and them as values
# age. Create a function that outputs all key-value pairs as a tuple.

user_ages = {
    "Олександр": 25,
    "Марія": 30,
    "Іван": 22,
    "Катерина": 28
}

def print_user_ages(user_ages):
    pairs = user_ages.items()

    for pair in pairs:
        print(pair)

print_user_ages(user_ages)

# 8. Зробіть функцію, яка параметром прийматиме число, а повертатиме рядок з відповідним днем ​​тижня.
#
# 8. Make a function that will accept a number as a parameter and return a string with
# the corresponding day of the week.

def get_day_of_week(day_number):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if 1 <= day_number <= 7:
        return days_of_week[day_number - 1]
    else:
        return "Invalid day number. Enter a number from 1 to 7."

day_number = 7
day_name = get_day_of_week(day_number)
print(f"День номер {day_number} - це {day_name}.")

# 9. Ви отримуєте масив чисел, повертаєте суму всіх додатних.
# Приклад [1,-4,7,12]=>1 + 7 + 12 = 20
# Примітка: якщо підсумовувати нічого, сума за замовчуванням дорівнює 0.
#
# 9. You get an array of numbers, return the sum of all positive ones.
# Example [1,-4,7,12]=>1 + 7 + 12 = 20
# Note: If there is nothing to sum, the sum defaults to 0.

list_sum = [1,-4,7,12]

def sum_num(a):
    sum_answer = 0

    for i in a:
        if i > 0:
            sum_answer = sum_answer + i

    return print(sum_answer)

sum_num(list_sum)


# 10. Напишіть функцію min4(a, b, c, d), яка обчислює мінімум чотирьох чисел, яка не містить
# інструкції if, а використовує стандартну функцію min від двох чисел. Вважайте чотири цілих
# числа і виведіть їх мінімум.
#
# 10. Write a function min4(a, b, c, d) that calculates the minimum of four numbers that does not
# contain if statements, and uses the standard min function from two numbers. Consider four
# integers of numbers and output their minimum.

a, b, c, d = 4, 2, 7, 3

def min4(a, b, c, d):
    return min(min(a, b), min(c, d))

minimum = min4(a, b, c, d)
print(f"Мінімум чисел {a}, {b}, {c}, {d} - це {minimum}.")

'''

Складний рівень
Difficult level

'''

# 1. Дано чотири дійсні числа: x₁, y₁, x₂, y₂. Напишіть функцію distance(x1, y1, x2, y2), яка
# обчислює відстань між точками (x₁,y₁) та (x₂,y₂). Вважайте чотири дійсні числа і виведіть
# результат роботи цієї функції.
#
# 1. Four real numbers are given: x₁, y₁, x₂, y₂. Write a distance(x1, y1, x2, y2) function that
# calculates the distance between the points (x₁,y₁) and (x₂,y₂). Consider four real numbers and output
# the result of this function.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Enter the coordinates of two points in the format: x1 y1 x2 y2")
x1, y1, x2, y2 = map(float, input("Write here: ").split())

result = distance(x1, y1, x2, y2)

print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {result}")



# 2. Напишіть функцію, яка обчислює довжину відрізка за координатами його кінців. За допомогою
# цієї функції напишіть програму, яка обчислює периметр трикутника за координатами трьох його вершин.
#
# 2. Write a function that calculates the length of a segment based on the coordinates of its ends.
# By using of this function, write a program that calculates the perimeter of a triangle based
# on the coordinates of its three vertices.

def segment_length(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def triangle_perimeter(x1, y1, x2, y2, x3, y3):
    side_a = segment_length(x1, y1, x2, y2)
    side_b = segment_length(x2, y2, x3, y3)
    side_c = segment_length(x3, y3, x1, y1)
    return side_a + side_b + side_c

print("Enter the coordinates of the triangle's vertices:")
print("Input format for each vertex: x y (by space)")

x1, y1 = map(float, input("Enter the coordinates of the first vertex (x1 y1): ").split())
x2, y2 = map(float, input("Enter the coordinates of the second vertex (x2 y2): ").split())
x3, y3 = map(float, input("Enter the coordinates of the third vertex (x3 y3): ").split())

perimeter = triangle_perimeter(x1, y1, x2, y2, x3, y3)

print(f"Perimeter of the triangle: {perimeter}")
