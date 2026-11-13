from abc import ABC, abstractmethod

from project.food import Vegetable, Fruit, Meat, Seed


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @abstractmethod
    def feed(self, food: Vegetable| Fruit | Meat | Seed):
        pass

class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return (
            f"{type(self).__name__} "
            f"[{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
        )

class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return (
            f"{type(self).__name__} "
            f"[{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
        )