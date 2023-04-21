class Players:
    def __init__(self, letter):
        self.letter = letter

    def PlayOnBoard(self):
        ...

class HumanPlayer(Players):
    def __init__(self, letter):
        super().__init__(letter)

    def PlayOnBoard(self, TTT):
        ValidPosition = None
        VALIDATION = False
        while not VALIDATION:
            position = input(f"Player {self.letter} please enter position from 0-8: ")
            try:
                ValidPosition = int(position)
                if ValidPosition not in TTT.GetAvaliableSpacesIndex():
                    raise ValueError
                VALIDATION = True
            except ValueError:
                print("Please enter valid position: ")
        return ValidPosition