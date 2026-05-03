import random


def roll():
    min_value = 1
    max_value = 6
    result = random.randint(min_value, max_value)
    
    return result
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4:
            break
        else:
            print("Invalid number, must be between 2 and 4.")
    else:
        print("Invalid, try again.")
  
max_score = 50
player_scores = [0 for _ in range(players)]

game_over = False

while not game_over:
    for player_id in range(players):
        print(f"\nPlayer {player_id + 1}'s turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input(f"Player {player_id + 1}, do you want to roll? (y/n): ").lower()

            if should_roll == "n":
                break
            elif should_roll != "y":
                print("Invalid input. Please enter 'y' or 'n'.")
                continue

            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done!")
                break
            else:
                current_score += value
                print("You rolled a:", value)

        # ✅ ALWAYS update and print score
        player_scores[player_id] += current_score
        print(f"Player {player_id + 1} total score is: {player_scores[player_id]}")

        # ✅ Check winner AFTER printing
        if player_scores[player_id] >= max_score:
            print(f"🎉 Player {player_id + 1} wins!")
            game_over = True
            break


 