class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_data(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

user1 = Person("Vadym", 25)
user1.print_data()

user2 = Person("John", 20)
user2.print_data()