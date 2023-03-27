import random

def roll_dice():
    return random.randint(1, 6)Ÿ

def play_turn(player, position, snakes_and_ladders):
    roll = roll_dice()
    print(f"Player {player} rolled a {roll}")
    new_position = position + roll

    for start, end in snakes_and_ladders.items():
        if new_position == start:
            print(f"Player {player} encountered a {'snake' if start > end else 'ladder'}! ({start} -> {end})")
            new_position = end

    return new_position

def play_game(num_players, board_size):
    player_positions = [1] * num_players

    snakes_and_ladders = {
        3: 22,
        5: 8,
        11: 26,
        20: 29,
        27: 1,
        17: 4,
        21: 9,
        19: 7
    }

    while True:
        for i, position in enumerate(player_positions):
            new_position = play_turn(i + 1, position, snakes_and_ladders)
            player_positions[i] = new_position

            if new_position >= board_size:
                print(f"Player {i + 1} wins!")
                return

def main():
    num_players = int(input("Enter the number of players: "))
    board_size = int(input("Enter the board size: "))

    if num_players < 2 or board_size < 2:
        print("Please enter valid values for the number of players and board size.")
    else:
        play_game(num_players, board_size)

if __name__ == "__main__":
    main()
