
class parameters:
    def __init__(self,
        varianceMax:    float,
        varianceMin:    float,
        maxHeight:      float,
        minHeight:      float,
        sequense:       list[float] = []
        ) -> None:
                 
        #range of random numbers
        self.varianceMax = varianceMax
        self.varianceMin = varianceMin

        #limit of maximum and minimum values
        self.maxHeight = maxHeight
        self.minHeight = minHeight

        self.sequense = sequense
    
    def getLastIndex(self) -> int:
        return len(self.sequense) - 1 if len(self.sequense) != 0 else 0

    def getLastValue(self) -> float:
        return self.sequense[self.getLastIndex()] if len(self.sequense) != 0 else 0
