users = {
    'john': 'password123',
    'alice': 'alice2022',
    'bob': 'bobiscool',
    'emma': 'emma1234',
    'david': 'davidPassword'
}

login_input = input("write here your login: ")
password_input = input("write here your password: ")

for login, password in users.items():
    if login == login_input and password == password_input:
        print("OK")
        break
    else:
        print("BAD")

