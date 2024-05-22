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

print(f'10 + 10 // 2 = {10 + 10 // 2}')
print(f'18 / 3 ** 2 = {18 / 3 ** 2}')
print(f'14 % 4 = {14 % 4}')
print(f'10 * 10 + 5 = {10 * 10 + 5}')
print(f'5 ** 2 - 10 = {5 ** 2 - 10}')
print(f'20 * 5 // 4 = {20 * 5 // 4}')
print(f'20 + 2 * 4 = {20 + 2 * 4}')
print(f'25 - 10 % 5 = {25 - 10 % 5}')
print(f'16 // 4 ** 2 = {16 // 4 ** 2}')
print(f'30 - 15 * 2 = {30 - 15 * 2}')
