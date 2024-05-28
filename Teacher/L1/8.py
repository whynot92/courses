text = 'привіт світ'

count = 0
letters = "абсдефгхійклмнопрстуфхцчшщ"

for i in text:
    # if i.isalpha():
    if i in letters:
        count += 1

print(count)
