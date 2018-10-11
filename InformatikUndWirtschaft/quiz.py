import random

random_number = random.randint(1, 100)
print("Ich habe mir eine Zahl zwischen 1 und 100 gemerkt und du musst raten.")
numbers_guessed = []
while True:
    guess = int(input("Bitte gebe eine Zahl ein!"))
    print("")

    if guess in numbers_guessed:
        print("Don't guess the same number twice, silly!")
        print("")
    numbers_guessed.append(guess)

    if guess == random_number:
        print("Super, die Zahl war " + str(random_number))
        break
    elif guess < random_number:
        print("Die gesuchte Zahl ist grösser")
        print("")
    else:
        print("Die gesuchte Zahl ist kleiner")
        print("")
