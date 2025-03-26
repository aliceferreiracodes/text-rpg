class Ability:
    
    def __init__(self, name, ability_points, ability_bonus):
        self._name = name
        self._ability_points = ability_points
        self._ability_bonus = ability_bonus

    @property
    def name(self):
        return self._name
    
    @property
    def ability_points(self):
        return self._ability_points
    
    @property
    def ability_bonus(self):
        return self._ability_bonus
