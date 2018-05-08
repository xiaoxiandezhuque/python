from enum import Enum, unique

@unique
class Bead(Enum):
    bule = 0  # Sun的value被设定为0
    gray = 1
    green = 2
    purple = 3
    red = 4
    yellow = 5
    other = 6

# from enum import Enum
#
# Bead = Enum("Bead", ("bule", "gray", "green", "purple", "red", "yellow", "other"))
