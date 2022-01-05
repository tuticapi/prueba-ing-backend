from django.conf import settings
from decimal import Decimal


class Core:
    def __init__(self, members):
        self.members = members
        self.levels = settings.RESUELVE_LEVELS
        self.team = {}

    def calculate_salary(self):
        try:
            self.process_init()
            return self.process_salary()
        except Exception as ex:
            raise ex

    def process_init(self):
        for member in self.members:
            team = member.get('equipo')
            if team not in self.team:
                self.team[team] = {}
                self.team[team]['total_goals'] = 0
                self.team[team]['wanted'] = 0
            goles = member.get('goles')
            self.team[team]['total_goals'] += goles
            level = member.get('nivel')
            self.team[team]['wanted'] += self.levels[level]

    def process_salary(self):
        team = []
        for member in self.members:
            level = member.get('nivel')
            member['goles_minimos'] = self.levels[level]
            member["sueldo_completo"] = round(self.process_calculate(member), 2)
            team.append(member)
        return team

    def process_calculate(self, member):
        team = member["equipo"]
        bonus = member["bono"]
        base_salary = member["sueldo"]
        individual_goal = member['goles_minimos']
        team_total_goals = self.team[team]["total_goals"]
        team_wanted_goals = self.team[team]["wanted"]

        player_percentage = self.get_percentage(
            individual_goal,
            member["goles"]
        )
        team_percentage = self.get_percentage(
            team_wanted_goals,
            team_total_goals
        )
        team_bonus = Decimal(0.5) * Decimal(bonus) * Decimal(team_percentage)

        individual_bonus = (Decimal(0.5) *
                            Decimal(bonus) *
                            Decimal(player_percentage))

        return (Decimal(base_salary) +
                Decimal(team_bonus) +
                Decimal(individual_bonus))

    def get_percentage(self, wanted, total):

        if wanted > 0 and total < wanted:
            return total/wanted

        return 1
