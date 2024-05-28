N: int = int(input("Enter an integer: "))


result = N+1 if N % 2 != 0 else N+2

print(f"Next for, {N}, even number:, {result}")