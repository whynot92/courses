# 1. Напишіть програму, яка зчитує два цілих числа A та B і виводить найбільше значення з них.
# 1. Write a program that reads two integers A and B and outputs the largest value from them.

def largest_value(first_value: int, second_value: int) -> None:
    if int(first_value) > int(second_value):
        return print(f"Your first number {first_value} is greater than your second number {second_value}")
    elif int(second_value) > int(first_value):
        return print(f"Your second number {second_value} is greater than your first number {first_value}")


first_type: int = int(input("Write your first number here: "))
second_type: int = int(input("Write your second number here: "))

largest_value(first_type, second_type)

# 2. Написати програму визначення координатної чверті, перевіряючи спочатку координату «Y».
# 2. Write a program to determine the coordinate quarter, first checking the "Y" coordinate.


def coordinat_quarter(value: float) -> None:
    if float(value) > 0:
        return print(f"Your coordinate {value} in I quarter")
    elif value < 0:
        return print(f"Your coordinate {value} in II quarter")
    else:
        return print(f"Your coordinate in axis Y")


input_coordinate: float = float(input("Write the coordinate Y here: "))

coordinat_quarter(input_coordinate)
