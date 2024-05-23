# 1. Напишіть програму, яка зчитує два цілих числа A та B і виводить найбільше значення з них.
# 1. Write a program that reads two integers A and B and outputs the largest value from them.

A: int = int(input("Write first integer number here: "))
B: int = int(input("Write second integer number here: "))

if A > B:
    print(f'The largest number = {A}')
elif A < B:
    print(f'The largest number = {B}')

# 2. Написати програму визначення координатної чверті, перевіряючи спочатку координату «Y»
# 2. Write a program to determine the coordinate quarter, first checking the "Y" coordinate

coordinate: int = int(input("Write the coordinate here: "))

if coordinate == 0:
    print("Yore are on Y coordinates")
elif coordinate < 0:
    print("You are the second quarter of Y coordinates")
else:
    print("You are the first quarter of Y coordinates")

# 3. Написати програму, яка приймає на вхід кількість балів (ціле число). Якщо кількість балів студента більше 80, то
# вивести повідомлення, що студент здав іспит. В протилежному випадку написати, що іспит не складено
# 3. Write a program that takes as input the number of points (an integer). If the number of student points is more
# than 80, then display a message that the student has passed the exam. Otherwise, write that the exam
# has not been passed

exam: int = int(input("Write your bales on exam here: "))

if exam >= 80:
    print('You passed the exam!')
else:
    print("You don't passed the exam")

# 4. Користувач вводить з клавіатури ширину та довжину прямокутника, якщо ширина більша за довжину, то вивести
# периметри прямокутника, якщо менша то вивести площу прямокутника
# 4. The user enters the width and length of the rectangle from the keyboard, if the width is greater than the length,
# then output perimeters of the rectangle, if smaller, then display the area of the rectangle

latitude: int = int(input("Write latitude here: "))
longitude: int = int(input("Write longitude here: "))

if latitude > longitude:
    print(f"Perimeters of the rectangle = {(latitude + longitude) * 2}")
elif latitude < longitude:
    print(f"The area of the rectangle = {latitude * longitude}")

# 5. Ввести число, визначити чи воно додатнє або  відємне
# 5. Enter a number, determine whether it is positive or negative

number: int = int(input("Write here your number: "))

if number < 0:
    print(f'Number {number} is negative')
elif number > 0:
    print(f'Number {number} is positive')

# 6. Ввести число, визначити чи воно додатнє,  відємне або воно нуль
# 6. Enter a number, determine whether it is positive, negative or zero

number: int = int(input("Write here your number: "))

if number < 0:
    print(f'Number {number} is negative')
elif number > 0:
    print(f'Number {number} is positive')
else:
    print(f'{number} does not belong to positive either')

# 7. Користувач вводить з клавіатур 2 числа, вивести на екран більше з них у вигляді, перше число більше за друге або
# друге число більше за перше.
# 7. The user enters 2 numbers from the keyboard, display more of them on the screen in the form, the first number is
# greater than the second or the second number is greater than the first.

first_number: int = int(input("Write here your first number: "))
second_number: int = int(input("Write here your second number"))

if first_number > second_number:
    print(f"The first number {first_number} is greater than the second {second_number}")
elif first_number < second_number:
    print(f"The second number {second_number} is greater than the first {first_number}")

# 8. Користувач вводить імя та свій вік, треба вивести на екран, якщо користувачеві більше або рівно 18 то вивести
# "_імя_ доступ дозволено" інакше "_імя_ доступ не дозволено"
# 8. The user enters his name and age, it should be displayed on the screen, if the user is over or equal to 18,
# then display "_name_ access is allowed" otherwise "_name_ access is not allowed"

user_name: str = input("Write your firstname here: ")
user_age: int = int(input("Write here your age: "))

if user_age >= 18:
    print(f"{user_name} access is allowed.")
else:
    print(f"{user_name} access is not allowed.")
