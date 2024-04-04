def check_gender(pin):
    gender=pin.split('-')[1]
    if (int(gender[0])%2==0):
        return "Female"
    else:
        return "Male"

my_pin = '200101-9012345'
print(check_gender(my_pin))