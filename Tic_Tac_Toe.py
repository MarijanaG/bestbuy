def display_board(board):

    print(f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print("─────────────")
    print(f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print("─────────────")
    print(f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |")

    return board


player_1 = input("Please choose one symbol 'X' or 'O' ")
if player_1 == "X".lower():
    player_2 = "O"
    print("Player_2 your symbol is 'O'")
elif player_1 == "O".lower():
    player_2 = "X"
    print("Player_2 your symbol is 'X'")
else:
    print("Invalid character, please enter 'X' or 'O'")


def check_space(current_player, board):
    while True:
        place_char = input("Where would you like to enter your symbol 1-9 ")
        if place_char == "1" and board[0][0] == "-":
            board[0][0] = current_player
            break
        elif place_char == "2" and board[0][1] == "-":
            board[0][1] = current_player
            break
        elif place_char == "3" and board[0][2] == "-":
            board[0][2] = current_player
            break
        elif place_char == "4" and board[1][0] == "-":
            board[1][0] = current_player
            break
        elif place_char == "5" and board[1][1] == "-":
            board[1][1] = current_player
            break
        elif place_char == "6" and board[1][2] == "-":
            board[1][2] = current_player
            break
        elif place_char == "7" and board[2][0] == "-":
            board[2][0] = current_player
            break
        elif place_char == "8" and board[2][1] == "-":
            board[2][1] = current_player
            break
        elif place_char == "9" and board[2][2] == "-":
            board[2][2] = current_player
            break
        else:
            print("please enter a valid number (1-9)")


def check_winner(board):
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O"):
        print("Congratulations you won")
        return True
    elif (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O"):
        print("Congratulations you won")
        return True
    elif (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O"):
        print("Congratulations you won")
        return True
    elif (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O"):
        print("Congratulations you won")
        return True
    elif (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O"):
        print("Congratulations you won")
        return True
    elif (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
        print("Congratulations you won")
        return True
    elif (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"):
        print("Congratulations you won")
        return True
    elif (board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X") or (board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O"):
        print("Congratulations you won")
        return True
    elif ("-" not in board[0]) and ("-" not in board[1]) and ("-" not in board[2]):
        print("Its a tie")
        return True


def change_player(current_player, board):

    if current_player == player_1:
        current_player = player_2
        return current_player
    elif current_player == player_2:
        current_player = player_1
        return current_player


def main():
    print("Lets put some color on a code")
    print("marijana change too")
    print("now line 100 belongs to lydia")
    print("Xhefri changed line 100 again :)))")
    print("enough printing messages here-xh:)")
    board = [["-", "-", "-", ],
             ["-", "-", "-", ],
             ["-", "-", "-"]]
    display_board(board)
    current_player = player_1
    while True:

        check_space(current_player, board)
        display_board(board)
        winner = check_winner(board)
        if winner is True:
            play_again = input("Do you want to play again? Y/N")
            if play_again == "Y".lower():
                board = [["-", "-", "-", ],
                         ["-", "-", "-", ],
                         ["-", "-", "-"]]
            else:
                break

        current_player = change_player(current_player, board)


if __name__=="__main__":
    main()
