text = "This is a test"


for index, char in enumerate(text, start=1):
    print(index, char)

print(list(enumerate(text, start=1)))