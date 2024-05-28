dict_person = {
    "name": "Vadum",
    "age": 20,
    "height": 180,
    "weight": 80,
    "sex": "male"
}

for key, value in dict_person.items():
    print(f"{key}: {value}")


for index, data, in enumerate(dict_person.items()):
    key, value = data
    print(index, key, value )


print(dict_person.values())