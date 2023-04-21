
class TicTacToe:
    def __init__(self) -> None:
        self.board = [" " for _ in range(9)]
        self.winner = None

    def PrintCurrentBoard(self) -> None:
        """Convert list to TicTacToe board and print all values inside the list i.e board"""
        ChunckedBoard = [self.board[index*3 : (index+1)*3 ] for index in range(3)]
        for row in ChunckedBoard:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def PrintBoardIndex() -> None:
        """Print indexes related to TicTacToe board"""
        IndexedBoard = [[str(index) for index in range(r*3, (r+1)*3)] for r in range(3)]
        for row in IndexedBoard:
            print("| " + " | ".join(row) + " |")

    def IsEmptyBoard(self)-> bool:
        """Return True if there is avaliable space on the board else return False to break the loop"""
        return " " in self.board

    def GetAvaliableSpacesIndex(self) -> list:
        """Retuen list contain all avaliables places in the board"""
        return [index for (index, value) in enumerate(self.board) if value == " "]

    def PutOnBoard(self, letter :str, position :int) -> bool:
        """Responsible to put letter 'X' or 'O' inside the board i.e the list"""
        if self.board[position] == " ":
            self.board[position] = letter
            if self.CheckWinners(letter, position):
                self.winner = letter
            return True
        return False

    def CheckWinners(self, letter :str, position :int) -> bool:
        """Check if there s winner according to three levels
        1- By rows
        2- By columns
        3- By diagonals
        """
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