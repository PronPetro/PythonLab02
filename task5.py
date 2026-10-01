numeric_string='12345'

for value in numeric_string:
    if value.isdigit() == True:
        print(value, "є цифрою")
    if value.isdigit() == False:
        print(value, "не є цифрою")