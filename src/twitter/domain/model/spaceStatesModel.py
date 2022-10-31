from enum import auto
from strenum import LowercaseStrEnum


class SpaceStates(LowercaseStrEnum):
    LIVE = auto()
    SCHEDULED = auto()
