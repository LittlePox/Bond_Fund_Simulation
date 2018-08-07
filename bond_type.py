from enum import Enum


class BondType(Enum):
    TREASURY = 1
    INVESTMENT_GRADE = 2
    HIGH_YIELD = 3

    def __str__(self):
        if self.value == 1:
            return "Treasury"
        elif self.value == 2:
            return "Investment Grade"
        else:
            return "High Yield"
