from enum import Enum
class tarik(Enum):
    WEST = 0b1000
    EAST = 0b0010

num = tarik.EAST.value
print(tarik.WEST.name)

