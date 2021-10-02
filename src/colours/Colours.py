from abc import ABC, abstractmethod
from typing import List

from colour import  Color

class Colours(ABC):
    @abstractmethod
    def getColours(self) -> List[Color]:
        pass
