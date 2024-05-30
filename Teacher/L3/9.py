def factorial(n):
    print(n)
    if n <= 1:
        return 1
    else:
        suma = n * factorial(n - 1)
        print(n)
    return suma

print(factorial(5))
