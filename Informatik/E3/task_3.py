# Please do not modify this part of the code!
special_character_set = "@/%&*_-"

is_valid = False

# Your code goes here
req_a = False
req_b = False
req_c = False
req_d = False
req_e = False
number_of_upper = 0
number_of_lower = 0
number_of_digits = 0
number_of_specialchar = 0

password = input("Please enter Password: ")

if 8 <= len(password) <= 30:
    req_a = True
    # weiter mit req
    for ch in password:
        if ch.isupper():
            number_of_upper += 1
        elif ch.islower():
            number_of_lower += 1
        elif ch.isdigit():
            number_of_digits += 1
        elif ch in special_character_set:
            number_of_specialchar += 1

else:
    req_a = False

if number_of_upper >= 2:
    req_b = True
if number_of_lower >= 2:
    req_c = True
if number_of_digits >= 1:
    req_d = True
if number_of_specialchar == 1:
    req_e = True

requirements = [req_a, req_b, req_c, req_d, req_e]

for req in requirements:
    if req:
        is_valid = True
        continue
    else:
        is_valid = False
        break

print("Requirements met: " + str(is_valid))
