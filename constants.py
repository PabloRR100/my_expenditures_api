from enum import Enum, IntEnum


class Years(str, Enum):
    y2020 = "2020-2021"
    y2019 = "2019-2020"
    y2018 = "2018-2019"


class Foot(str, Enum):
    right = "diestro"
    left = "zurdo"
    both = "ambidiestro"