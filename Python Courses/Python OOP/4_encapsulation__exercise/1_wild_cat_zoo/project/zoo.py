from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Lion | Tiger | Cheetah] = []
        self.workers: list[Keeper | Vet | Caretaker] = []

    def add_animal(self, animal, price: float):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        worker = next((worker for worker in self.workers if worker.name == worker_name), None)

        if worker is None:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salary_sum = sum([worker.salary for worker in self.workers])

        if self.__budget >= salary_sum:
            self.__budget -= salary_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money_for_care = sum([animal.money_for_care for animal in self.animals])

        if self.__budget >= needed_money_for_care:
            self.__budget -= needed_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: float):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]

        for animal_type in (Lion, Tiger, Cheetah):
            animals = [
                animal for animal in self.animals
                if isinstance(animal, animal_type)
            ]

            result.append(f"----- {len(animals)} {animal_type.__name__}s:")
            result.extend(repr(animal) for animal in animals)

        return "\n".join(result)


    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]

        for worker_type in (Keeper, Caretaker, Vet):
            workers = [
                worker for worker in self.workers
                if isinstance(worker, worker_type)
            ]

            result.append(f"----- {len(workers)} {worker_type.__name__}s:")
            result.extend(repr(worker) for worker in workers)

        return "\n".join(result)
