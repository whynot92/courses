class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        return self.name, self.age, self.gender


class Dog(Animal):
    def __init__(self, name, age, gender, breed):
        super().__init__(name, age, gender)
        self.breed = breed

    def get_info(self):
        print(super().get_info())
        return self.name, self.age, self.gender, self.breed

dog1 = Dog("Rex", 20, "man", "Haski")

print(dog1.get_info())