import numpy as np
from enum import Enum, IntEnum
import random

class RoomType(IntEnum):
    luxury = 5
    half_luxury = 4
    tho_with_sofa = 3
    two = 2
    one = 1
    
def get_next(our_room_type):
    for room_type in RoomType:
        if room_type - our_room_type == 1:
            return room_type
    return None
