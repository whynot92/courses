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

# 9. Напишіть програму, яка запитує у користувача число і виводить повідомлення "Число парне" або "Число непарне",
# в залежності від того, чи є число парним чи непарним.
# 9. Write a program that asks the user for a number and outputs the message "Number is even" or "Number is odd",
# depending on whether the number is even or odd.

first_user_number: int = int(input("Write here your first number: "))

if first_user_number % 2 == 0:
    print("The number is even")
elif first_user_number % 2 == 1:
    print("The number is odd")

# 10. Напишіть програму, яка запитує у користувача число і виводить повідомлення "Число ділиться на 3" або "Число не
# ділиться на 3", в залежності від того, чи ділиться число на 3 без залишку.
# 10. Write a program that asks the user for a number and outputs the message "The number is divisible by 3" or
# "The number is not is divisible by 3", depending on whether the number is divisible by 3 without a remainder.

first_user_number: int = int(input("Write here your number: "))

if first_user_number % 3 == 0:
    print("The number is divisible by 3")
elif first_user_number % 3 == 1:
    print("Did not is divisible by 3")

# 11.Напишіть програму, яка приймає три цілих числа і перевіряє, чи є перше число кратним сумі другого і третього числа.
# 11. Write a program that accepts three integers and checks whether the first number is a multiple of the sum
# of the second and third numbers.

input_first_number: int = int(input("Write here your first number: "))
input_second_number: int = int(input("Write here your second number: "))
input_third_number: int = int(input("Write here you third number: "))

if input_first_number % (input_second_number + input_third_number) == 0:
    print("The first number is a multiple of the sum of the second and third numbers")
else:
    print("The first number is not a multiple of the sum of the second and third numbers")

# 12 . Напишіть програму, яка приймає два цілих числа і перевіряє, чи є перше число кратним другому.
# 12. Write a program that takes two integers and checks whether the first number is a multiple of the second.

first_integer: int = int(input("Write here your first number: "))
second_integer: int = int(input("Write here your second number: "))

if first_integer % second_integer == 0:
    print(f"The first number {first_integer} is a multiple of the second {second_integer}.")
else:
    print(f"The first number {first_integer} is not a multiple of the second ({second_integer}).")

# 13. Користувач вводить свій вік, вивести на екран повідомлення чи користувач це дитина, підліток, дорослий або
# престарілий.
# 13. The user enters his age, to display a message on the screen whether the user is a child, teenager, adult or
# elderly.

age_user: int = int(input("Write here your age: "))

if age_user < 0:
    print("Enter the correct age.")
elif age_user < 13:
    print("You are a child.")
elif age_user < 18:
    print("You are a teenager.")
elif age_user < 65:
    print("You are an adult.")
else:
    print("You are an old man.")

# 14. Дано три цілих числа. Визначте, скільки з них збігаються. Програма повинна вивести одне з чисел:
# 3 (якщо всі збігаються), 2 (якщо два збігаються) або 0 (якщо всі числа є різними).
# 14. Three integers are given. Determine how many of them match. The program should output one of the numbers:
# 3 (if all match), 2 (if two match), or 0 (if all numbers are different).

num_one: int = int(input("Write first number: "))
num_two: int = int(input("Write second number: "))
num_three: int = int(input("Write third number: "))

if num_one == num_two == num_three:
    print(3)
elif num_one == num_two or num_one == num_three or num_two == num_three:
    print(2)
else:
    print(0)