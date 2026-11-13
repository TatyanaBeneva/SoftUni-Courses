from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    __oracle = {1: 1500000, 2: 800000}
    __honda = {8: 20000, 10: 10000}
    __expenses = 250000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors_money = 0

        if race_pos <= 1:
            sponsors_money += self.__oracle[1]
        elif race_pos <= 2:
            sponsors_money += self.__oracle[2]

        if race_pos <= 8:
            sponsors_money += self.__honda[8]
        elif race_pos <= 10:
            sponsors_money += self.__honda[10]

        earned_money = sponsors_money - self.__expenses
        self.budget += earned_money

        return f"The revenue after the race is {earned_money}$. Current budget {self.budget}$"