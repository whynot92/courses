# 1. Написати відповідь True або False:
# 1. Write the answer True or False:

print(f"not (False or False) = {not (False or False)}")    # True
print(f"False or not False = {False or not False}")    # True
print(f"not (True or False) = {not (True or False)}")    # False
print(f"False and not False = {False and not False}")    # False
print(f"not (False and True) = {not (False and True)}")    # True
print(f"True and not False = {True and not False}")    # True
print(f"not (True and False) = {not (True and False)}")    # True
print(f"False and not True = {False and not True}")    # False
print(f"not (False or True) = {not (False or True)}")    # False
print(f"True or not False = {True or not False}")    # True
print(f"not (True or True) = {not (True or True)}")    # False
print(f"False or not True = {False or not True}")    # False
print(f"not (True and True) = {not (True and True)}")    # False
print(f"True and not True = {True and not True}")    # False
print(f"not (False and False) = {not (False and False)}")    # True
print(f"True or not True = {True or not True}")    # True
print(f"not (True or False) = {not (True or False)}")    # False
print(f"False and not False = {False and not False}")    # False
print(f"not (False or True) = {not (False or True)}")    # Falsw
print(f"True and not False = {True and not False}")    # True

# 2. Задано число, визначити чи воно входить в діапазон від 10 до 30
# 2. Given a number, determine if it is in the range from 10 to 30

number: int = int(input("Write here your number: "))

if number >= 10 and number <= 30:
    print(f"{number} is in the range from 10 to 30")
else:
    print(f"{number} isn't in the range from 10 to 30")

# 3. Напишіть програму, яка перевіряє, чи є число парне і додатне.
# 3. Write a program that checks whether a number is even and positive.

user_number: int = int(input("Write your number here: "))

if user_number > 0 and user_number % 2 == 0:
    print(f"{user_number} is even and positive")
else:
    print(f"{user_number} isn't even and positive")

# 4. Напишіть програму, яка перевіряє, чи є число додатним, парним та не кратним 3.
# 4. Write a program that checks whether a number is positive, even, and not a multiple of 3.

intenger: int = int(input("Write here number: "))

if intenger > 0 and intenger % 2 == 0 and intenger % 3 != 0:
    print(f"the number {intenger} is positive, even and not a multiple of 3")
else:
    print(f"the number {intenger} isn't positive, even and not a multiple of 3")

# 5. Напишіть програму, яка перевіряє, чи є число кратним 3 або 5, але не кратним обом одночасно.
# 5. Write a program that checks whether a number is a multiple of 3 or 5, but not a multiple of both.

number: int = int(input("Write here your number: "))

if (number % 3 == 0 or number % 5 == 0) and not (number % 3 == 0 or number % 5 == 0):
    print(True)
else:
    print(False)

# 6. Напишіть програму, яка перевіряє, чи є число менше за 100 і більше за 50.
# 6. Write a program that checks whether a number is less than 100 and greater than 50.

number_user: int = int(input("Write here your number: "))

if number_user < 100 and number_user > 50:
    print(True)
else:
    print(False)

# 7. Напишіть програму, яка перевіряє, чи є число додатним і менше за 50 або від'ємним і більше за -10.

user_int: int = int(input("Write here number: "))

if (user_int > 0 and user_int < 50) or (user_int < 0 and user_int > -10):
    print(True)
else:
    print(False)