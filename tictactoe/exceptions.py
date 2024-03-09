class Invalid2dIndexException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class TileAtIndexAlreadyOccupiedException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
