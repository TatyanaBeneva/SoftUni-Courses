from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food: Vegetable | Fruit | Meat | Seed):
        if not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity

class Hen(Bird):
    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food: Vegetable | Fruit | Meat | Seed):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity