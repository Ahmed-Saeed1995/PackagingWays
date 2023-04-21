from abc import abstractmethod, ABC

class Players(ABC):
    def __init__(self, letter :str) -> None:
        self.letter = letter

    @abstractmethod
    def PlayOnBoard(self) -> None:
        ...

class HumanPlayer(Players):
    def __init__(self, letter :str):
        super().__init__(letter)

    def PlayOnBoard(self, TTT :object)->int:
        """Return valid position avaliable in the board
        return integer from 0-8 only according to length of the board i.e list"""
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