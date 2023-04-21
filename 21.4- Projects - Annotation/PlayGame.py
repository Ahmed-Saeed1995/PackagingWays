from Players import HumanPlayer
from TicTacToe import TicTacToe

# OutSide The Class ______________________________________________
def PlayGame(TTT :object, PlayerX :object, PlayerO :object) -> None:
    """Play Tic Tac Toe game using TicTacToe class and Players"""
    if True:
        # print board indexes
        TTT.PrintBoardIndex()

    letter = "x"
    while TTT.IsEmptyBoard():
        # Let player O play his turn if True
        if letter == "o":
            position = PlayerO.PlayOnBoard(TTT)
        else:
            # else if False let Player X play his turn
            position= PlayerX.PlayOnBoard(TTT)

        # Put the letter inside the board according to the Player`s position
        if TTT.PutOnBoard(letter, position):
            print(f"Player {letter} played on position {position}: ")
            TTT.PrintCurrentBoard()

        # Check if there`s winner or not
        if TTT.CheckWinners(letter, position):
            print(f"The winner is of player letter {TTT.winner}: ")
            return letter

        # Switch player if there was no winner yet
        letter = "o" if letter == "x" else 'x'
    print("Tied board no one win the game ")

if __name__ == "__main__":
    TTT = TicTacToe() # TicTacToe board object
    PlayerX = HumanPlayer("x") # PlayerX object
    PlayerO = HumanPlayer("o") # PlayerO object
    PlayGame(TTT, PlayerX, PlayerO)