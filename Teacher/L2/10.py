users = {
    'john': 'password123',
    'alice': 'alice2022',
    'bob': 'bobiscool',
    'emma': 'emma1234',
    'david': 'davidPassword'
}

login_input = input("write here your login: ")
password_input = input("write here your password: ")

if login in users and password in users.values():
    print("OK")
else:
    print("BAD")

