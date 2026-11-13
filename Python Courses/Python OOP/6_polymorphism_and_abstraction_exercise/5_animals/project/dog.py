from project.animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender: str):
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound():
        return "Woof!"