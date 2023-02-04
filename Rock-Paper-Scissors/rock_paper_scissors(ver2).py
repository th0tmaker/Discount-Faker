import random

user_score = 0
ai_score = 0


def play():
    options = ("Rock", "Paper", "Scissors")
    ai_choice = random.choice(options)
    user_choice = input("Rock, Paper, Scissors? Pick one. ").capitalize()

    global user_score
    global ai_score

    # takes tuple user_choice[0] and ai_choice[1] and matches them to corresponding indexes of tuples inside a list
    # if user_choice[0] is "Rock"[0] while ai_choice[1] is "Scissors"[1] etc., user wins
    if (user_choice, ai_choice) in [("Rock", "Scissors"),
                                    ("Paper", "Rock"),
                                    ("Scissors", "Paper")]:
        result = "WON"
        user_score += 1
    # if user_choice[0] and ai_choice[1] are the same at both index 0 and 1, it's a tie
    elif user_choice == ai_choice:
        result = "TIE"
    # if any other combination occurs, user lost
    else:
        result = "LOST"
        ai_score += 1

    print(f"You picked '{user_choice}'.\n"
          f"Computer AI picked '{ai_choice}'.\n"
          f"You {result}.\n"
          f"The current score is...\n"
          f"YOU: {user_score}\n"
          f"COMPUTER AI: {ai_score}")


while True:
    play()
