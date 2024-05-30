with open('test.txt', 'w', encoding="UTF-8") as f:
    f.write('Привіт світ')


with open('test.txt', 'r', encoding="UTF-8") as f:
    print(f.read())