import re

num_phone = "+380977894561 +380951234567 +380987654325  +380959876543"

numbers = re.findall('\+38095\d{7}', num_phone)

print(numbers)