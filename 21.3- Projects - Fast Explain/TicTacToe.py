from Players import HumanPlayer

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.winner = None

    def PrintCurrentBoard(self):
        ChunckedBoard = [self.board[index*3 : (index+1)*3 ] for index in range(3)]
        for row in ChunckedBoard:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def PrintBoardIndex():
        IndexedBoard = [[str(index) for index in range(r*3, (r+1)*3)] for r in range(3)]
        for row in IndexedBoard:
            print("| " + " | ".join(row) + " |")

    def IsEmptyBoard(self):
        return " " in self.board

    def GetAvaliableSpacesIndex(self):
        return [index for (index, value) in enumerate(self.board) if value == " "]

    def PutOnBoard(self, letter, position):
        if self.board[position] == " ":
            self.board[position] = letter
            if self.CheckWinners(letter, position):
                self.winner = letter
            return True
        return False

    def CheckWinners(self, letter, position):
        # Rows
        floored = position // 3
        ChunckedRows = self.board[floored*3: (floored+1)*3]
        if all([letter == inPosition for inPosition in ChunckedRows]):
            return True

        # columns
        modulues = position % 3
        ChunckedColumns = [self.board[modulues + i* 3] for i in range(3)]
        if all([letter == inPosition for inPosition in ChunckedColumns]):
            return True

        # Diagonals
        if position % 2 ==0:
            Diagonal1 = [self.board[d1] for d1 in range(0, 10, 4)]
            if all([letter == inPosition for inPosition in Diagonal1]):
                return True

            Diagonal2 = [self.board[d2] for d2 in range(2, 8, 2)]
            if all([letter == inPosition for inPosition in Diagonal2]):
                return True

# OutSide The Class ______________________________________________
def PlayGame(TTT, PlayerX, PlayerO):
    if True:
        TTT.PrintBoardIndex()

    letter = "x"
    while TTT.IsEmptyBoard():
        if letter == "o":
            position = PlayerO.PlayOnBoard(TTT)
        else:
            position= PlayerX.PlayOnBoard(TTT)

        if TTT.PutOnBoard(letter, position):
            if True:
                print(f"Player {letter} played on position {position}: ")
                TTT.PrintCurrentBoard()

        if TTT.CheckWinners(letter, position):
            if True:
                print(f"The winner is of player letter {TTT.winner}: ")
            return letter

        letter = "o" if letter == "x" else 'x'
    print("Tied board no one win the game ")

if __name__ == "__main__":
    TTT = TicTacToe()
    PlayerX = HumanPlayer("x")
    PlayerO = HumanPlayer("o")
    PlayGame(TTT, PlayerX, PlayerO)