# 1. Напишіть програму, яка зчитує два цілих числа A та B і виводить найбільше значення з них.
# 1. Write a program that reads two integers A and B and outputs the largest value from them.

first_value: int = int(input("Write your first number here: "))
second_value: int = int(input("Write your second number here: "))

first_answer = f"Your first number {first_value} is greater than your second number {second_value}"
second_answer = f"Your second number {second_value} is greater than your first number {first_value}"

if first_value > second_value:
    print(first_answer)
elif second_value > first_value:
    print(second_answer)

# 2. Написати програму визначення координатної чверті, перевіряючи спочатку координату «Y».
# 2. Write a program to determine the coordinate quarter, first checking the "Y" coordinate.

def test_fink():

    pass