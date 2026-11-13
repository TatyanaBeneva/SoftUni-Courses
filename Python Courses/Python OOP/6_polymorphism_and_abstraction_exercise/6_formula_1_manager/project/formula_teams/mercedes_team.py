from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    __petronas = {1: 1000000, 3: 500000}
    __team_viewer = {5: 100000, 7: 50000}
    __expenses = 200000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors_money = 0

        if race_pos <= 1:
            sponsors_money += self.__petronas[1]
        elif race_pos <= 3:
            sponsors_money += self.__petronas[3]

        if race_pos <= 5:
            sponsors_money += self.__team_viewer[5]
        elif race_pos <= 7:
            sponsors_money += self.__team_viewer[7]

        earned_money = sponsors_money - self.__expenses
        self.budget += earned_money

        return f"The revenue after the race is {earned_money}$. Current budget {self.budget}$"
