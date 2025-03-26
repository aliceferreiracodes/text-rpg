class Skill:
    
    def __init__(self, name, skill_points, skill_level, skill_expertise):
        self._name = name
        self._skill_points = skill_points
        self._skill_level = skill_level
        self._skill_expertise = skill_expertise

    @property
    def skill_points(self):
        return self._skill_points
    
    @property
    def skill_level(self):
        return self._skill_level
    
    @property
    def skill_expertise(self):
        return self._skill_expertise
    
    def increment_points(self):
        self._skill_points += 1

    def increment_level(self):
        self._skill_level += 1

        if self._skill_level >= 35:
            self._skill_expertise = "Master"
        elif self._skill_level >= 25:
            self._skill_expertise = "Expert"
        elif self._skill_level >= 15:
            self._skill_expertise = "Skilled"
        elif self._skill_level >= 5:
            self._skill_expertise = "Half Skilled"
