# Please do not modify this part of the code!
result = ""

# Your code goes here
valid_options = ["Rock", "Paper", "Scissors"]
input_user1 = input("User 1, Please enter your choice (Rock, Paper, Scissors): ")
input_user2 = input("User 2, Please enter your choice (Rock, Paper, Scissors): ")

if input_user1 not in valid_options or input_user2 not in valid_options:
    result = "Wrong input"

elif input_user1 == input_user2:
    result = "Tie"

elif input_user1 == "Rock" and input_user2 == "Scissors":
    result = "User 1 wins"

elif input_user1 == "Paper" and input_user2 == "Rock":
    result = "User 1 wins"

elif input_user1 == "Scissors" and input_user2 == "Paper":
    result = "User 1 wins"

elif input_user1 == "Rock" and input_user2 == "Paper":
    result = "User 2 wins"

elif input_user1 == "Paper" and input_user2 == "Scissors":
    result = "User 2 wins"

elif input_user1 == "Scissors" and input_user2 == "Rock":
    result = "User 2 wins"

print(result)
