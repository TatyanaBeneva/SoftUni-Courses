from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food: Vegetable | Fruit | Meat | Seed):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 0.1 * food.quantity
        self.food_eaten += food.quantity

class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food: Vegetable | Fruit | Meat | Seed):
        if not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 0.4 * food.quantity
        self.food_eaten += food.quantity

class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food: Vegetable | Fruit | Meat | Seed):
        if not isinstance(food, Meat) and not isinstance(food, Vegetable):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 0.3 * food.quantity
        self.food_eaten += food.quantity

class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food: Vegetable | Fruit | Meat | Seed):
        if not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 1 * food.quantity
        self.food_eaten += food.quantity