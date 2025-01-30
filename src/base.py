from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def __str__(self):
        pass
