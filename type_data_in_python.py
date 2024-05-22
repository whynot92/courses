# 1. Створити дві змінні типу string і помістити туди ім’я та прізвище. Вивести привітання, враховуючи персональні дані:

first_name: str = 'Vadym'
second_name: str = 'Sokolov'

print(f'Hello {first_name} {second_name}!!!')

# 2. Ввести з клавіатури 2 числа, знайти різницю, суму, добуток та остачу першого числа від другого:

first_input_user: int = int(input('Write here your first number: '))
second_input_user: int = int(input('Write here your second number: '))
answer: int = 0

if first_input_user > second_input_user:
    answer = first_input_user - second_input_user
    print(answer)
elif first_input_user < second_input_user:
    second_input_user, first_input_user = first_input_user, second_input_user
    answer = first_input_user - second_input_user
    print(answer)

print(first_input_user + second_input_user)
print(first_input_user / second_input_user)
print(first_input_user ** second_input_user)
print(first_input_user % second_input_user)

# 3. Знайдіть результат операції:

print(f'10 + 10 // 2 = {10 + 10 // 2}')    # 15
print(f'18 / 3 ** 2 = {18 / 3 ** 2}')    # 2.0
print(f'14 % 4 = {14 % 4}')    # 2
print(f'10 * 10 + 5 = {10 * 10 + 5}')    # 105
print(f'5 ** 2 - 10 = {5 ** 2 - 10}')    # 15
print(f'20 * 5 // 4 = {20 * 5 // 4}')    # 25
print(f'20 + 2 * 4 = {20 + 2 * 4}')    # 28
print(f'25 - 10 % 5 = {25 - 10 % 5}')    # 25
print(f'16 // 4 ** 2 = {16 // 4 ** 2}')    # 1
print(f'30 - 15 * 2 = {30 - 15 * 2}')    # 0

# 4. Знайдіть результат операції:

print(f'7 * 3 <= 25 - {7 * 3 <= 25}')   # True
print(f'12 % 5 >= 2 - {12 % 5 >= 2}')   # True
print(f'4 + 5 > 6 - {4 + 5 > 6}')   # True
print(f'10 - 2 * 3 == 4 - {10 - 2 * 3 == 4}')   # True
print(f'2 * 4 + 1 >= 9 - {2 * 4 + 1 >= 9}')    # True
print(f'16 / 4 + 2 > 6 - {16 / 4 + 2 > 6}')    # False
print(f'3 * 4 - 5 <= 7 - {3 * 4 - 5 <= 7}')    # True
print(f'6 / 3 + 1 < 4 - {6 / 3 + 1 < 4}')    # True
print(f'11 - 3 == 9 + 2 - {11 - 3 == 9 + 2}')    # False
print(f'5 * 3 > 14 - {5 * 3 > 14}')    # True
print(f'(5 + 2) * 3 > 15 - {(5 + 2) * 3 > 15}')    # True
print(f'10 - (6 + 2) == 2 - {10 - (6 + 2) == 2}')    # True
print(f'(9 / 3) + (5 * 2) <= 20 - {(9 / 3) + (5 * 2) <= 20}')    # True
print(f'(7 % 3) * (2 + 3) >= 10 - {(7 % 3) * (2 + 3) >= 10}')    # False
print(f'(10 / 2) + (8 - 4) > 9 - {(10 / 2) + (8 - 4) > 9}')    # False
