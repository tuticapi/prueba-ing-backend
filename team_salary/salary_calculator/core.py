from django.conf import settings

class Core:
    def __init__(self, members):
        self.members = members
        self.levels = settings.RESUELVE_LEVELS
        self.team = {}
    
    def calculate_salary(self):
        for member in self.members:
            team = member.get('equipo')
            if team not in self.team:
                self.team[team] = {}
                self.team[team]['total_goals'] = 0
            goles = member.get('goles')
            self.team[team]['total_goals'] += goles
            print('team')
            print(self.team)


