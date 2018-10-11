# Please do not modify this part of the code!
grade = '-'

# Your code goes here
score = int(input("Please enter your score"))

if score < 0 or score > 100:
    print("Error: Score out of range (0-100)")

elif score < 60:
    grade = 'F'

elif score < 70:
    grade = 'D'

elif score < 80:
    grade = 'C'

elif score < 90:
    grade = 'B'

else:
    grade = 'A'

print(grade)
