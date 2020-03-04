import random 

#P/paper l/lizard s/spock r/rock x/scissor
moves = ("p", "l", "s", "r", "x")
full_name = {"p": "paper", "l":"lizard", "s": "spock", "r": "rock", "x": "scissor"}

print ("P/paper l/lizard s/spock r/rock x/scissor")

def determine_win(user, computer):
    print("User:", full_name[user], "Computer:", full_name[computer])
    if (user == computer):
        return "Draw"
    elif (user == "p" and computer == "l" or computer == "x"):
        return "Computer has won"
    elif (user == "p" and computer == "r" or computer == "s"):
        return "User has won"
    elif (user == "l" and computer == "x" or computer == "r"):
        return "Computer has won"
    elif (user == "l" and computer == "s" or computer == "p"):
        return "User has won"
    elif (user == "s" and computer == "l" or computer == "p"):
        return "Computer has won"
    elif (user == "s" and computer == "x" or computer == "r"):
        return "User has won"
    elif (user == "r" and computer == "p" or computer == "s"):
        return "Computer has won"
    elif (user == "r" and computer == "x" or computer == "l"):
        return "User has won"
    elif (user == "x" and computer == "s" or computer == "r"):
        return "Computer has won"
    elif (user == "x" and computer == "p" or computer == "l"):
        return "User has won"
    


while True:
    while True:
        user_input = input("Enter your move: ")
    
        if user_input in moves:
            break

    computer_input = moves[random.randrange(5)]
    print(determine_win(user_input, computer_input))


    
