PLAYER_1 = "X"
PLAYER_2 = "O"

positions = [i for i in range(1, 10)]

def print_board(positions):
    BOARD = f"  {positions[0]} | {positions[1]} | {positions[2]} \n" \
        "  ----------- \n" \
        f"  {positions[3]} | {positions[4]} | {positions[5]} \n" \
        "  ----------- \n" \
        f"  {positions[6]} | {positions[7]} | {positions[8]} \n"
    print(BOARD)

def set_current_player(counter):
    if counter % 2 == 0:
        return PLAYER_1
    else:
        return PLAYER_2

def player_move(player):
    position = int(input(f"Player {player}, enter your move (1-9): "))
    if position in positions:
        positions[position - 1] = player
    else:
        print("Invalid move. Try again.")
        player_move(player)

def check_winner():
    if (positions[0] == positions[1] == positions[2]) or \
       (positions[3] == positions[4] == positions[5]) or \
       (positions[6] == positions[7] == positions[8]) or \
       (positions[0] == positions[3] == positions[6]) or \
       (positions[1] == positions[4] == positions[7]) or \
       (positions[2] == positions[5] == positions[8]) or \
       (positions[0] == positions[4] == positions[8]) or \
       (positions[2] == positions[4] == positions[6]):
        return True

def main():
    print_board(positions=positions)
    counter = 0
    while True:
        player = set_current_player(counter)
        player_move(player)
        print_board(positions=positions)

        if check_winner():
            print(f"Player {player} wins!")
            break
        counter += 1
        if counter == 9:
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()