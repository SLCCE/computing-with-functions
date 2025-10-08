from abc import ABC, abstractmethod
from enum import Enum

class EquipmentType(Enum):
    HELMET = 1
    CHEST = 2
    LEGS = 3

class Armor(ABC):
    def __init__(self, type: EquipmentType, name: str, defence: int):
        self.name = name
        self.defence = defence

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

