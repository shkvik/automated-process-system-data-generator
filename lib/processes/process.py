from primitive.primitive import unit
import datetime

class algorithm:
    def __init__(self) -> None:
        self.start: int
        self.stop: int

        self.primitive = unit()

class event:
    def __init__(self) -> None:
        self.start: int
        self.stop: int

        self.initiators: list[algorithm]
        self.handlers: list[algorithm]

class cycle:
    def __init__(self) -> None:
        '''
        The cycle class includes the repetition of different algorithms, 
        their sequence and the number of repetitions
        '''

        self.start: int
        self.stop: int

        self.repeatCounter: int
        self.algorithms: list[algorithm]
        pass
