class Character:

    def __init__(self, full_name, first_name, gender, race, cclass, abilities, skills, stats):
        # info
        self._full_name = full_name
        self._first_name = first_name
        self._gender = gender
        self._race = race
        self._cclass = cclass

        # level
        self._level = 1
        
        # abilities
        self._abilities = abilities

        # skills
        self._skills = skills
        
        # stats
        self._stats = stats

    @property
    def full_name(self):
        return self._full_name
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def gender(self):
        return self._gender
    
    @property
    def race(self):
        return self._race
    
    @property
    def cclass(self):
        return self._cclass
    
    def display_info(self):

        print(
            f'''

    Name: {self._full_name:<50}   Race: {self._race}
    Gender: {self._gender:<48}   Class: {self._cclass}

     ____________     ____________     ____________     ____________     ____________     ____________     ____________     ____________
    |     HP     |   |     MM     |   |  Stamina   |   |   Speed    |   |    Luck    |   | Perception |   | Reputation |   |   Level    |
    --------------   --------------   --------------   --------------   --------------   --------------   --------------   --------------
    | {self._stats[0].overall_value:^10} |   | {self._stats[1].overall_value:^10} |   | {self._stats[2].overall_value:^10} |   | {self._stats[3].overall_value:^10} |   | {self._stats[4].overall_value:^10} |   | {self._stats[5].overall_value:^10} |   | {self._stats[6].overall_value:^10} |   | {self._level:^10} |
    |____________|   |____________|   |____________|   |____________|   |____________|   |____________|   |____________|   |____________|   
    
     _________________________ __________ _________ _______________                                   ______________ _________ _________
    |         Skills          |  Skill   |  Skill  |     Skill     |                                 |  Abilities   | Ability | Ability |
    |                         |  Points  |  Level  |   Expertise   |                                 |              | Points  |  Bonus  |
    |-------------------------|----------|---------|---------------|                                 |--------------|---------|---------|
    | Acrobatics (Dex)        | {self._skills[0].skill_points:^+8} | {self._skills[0].skill_level:^7} | {self._skills[0].skill_expertise:<13} |                                 | Strength     | {self._abilities[0].ability_bonus:^+7} | {self._abilities[0].ability_points:^+7} |
    | Animal Handling (Wis)   | {self._skills[1].skill_points:^+8} | {self._skills[1].skill_level:^7} | {self._skills[1].skill_expertise:<13} |                                 | Dexterity    | {self._abilities[1].ability_bonus:^+7} | {self._abilities[1].ability_points:^+7} |
    | Athletics (Str)         | {self._skills[2].skill_points:^+8} | {self._skills[2].skill_level:^7} | {self._skills[2].skill_expertise:<13} |                                 | Constitution | {self._abilities[2].ability_bonus:^+7} | {self._abilities[2].ability_points:^+7} |
    | Brewing (Mag)           | {self._skills[3].skill_points:^+8} | {self._skills[3].skill_level:^7} | {self._skills[3].skill_expertise:<13} |                                 | Intelligence | {self._abilities[3].ability_bonus:^+7} | {self._abilities[3].ability_points:^+7} |
    | Charm (Cha)             | {self._skills[4].skill_points:^+8} | {self._skills[4].skill_level:^7} | {self._skills[4].skill_expertise:<13} |                                 | Wisdom       | {self._abilities[4].ability_bonus:^+7} | {self._abilities[4].ability_points:^+7} |
    | Crafting (Int)          | {self._skills[5].skill_points:^+8} | {self._skills[5].skill_level:^7} | {self._skills[5].skill_expertise:<13} |                                 | Magic        | {self._abilities[5].ability_bonus:^+7} | {self._abilities[5].ability_points:^+7} |
    | Deception (Cha)         | {self._skills[6].skill_points:^+8} | {self._skills[6].skill_level:^7} | {self._skills[6].skill_expertise:<13} |                                 | Charisma     | {self._abilities[6].ability_bonus:^+7} | {self._abilities[6].ability_points:^+7} |
    | Intimidation (Cha)      | {self._skills[7].skill_points:^+8} | {self._skills[7].skill_level:^7} | {self._skills[7].skill_expertise:<13} |                                 |______________|_________|_________|
    | Investigation (Int)     | {self._skills[8].skill_points:^+8} | {self._skills[8].skill_level:^7} | {self._skills[8].skill_expertise:<13} |
    | Magical Botany (Mag)    | {self._skills[9].skill_points:^+8} | {self._skills[9].skill_level:^7} | {self._skills[9].skill_expertise:<13} |
    | Magical Equipment (Mag) | {self._skills[10].skill_points:^+8} | {self._skills[10].skill_level:^7} | {self._skills[10].skill_expertise:<13} |
    | Medicine (Int)          | {self._skills[11].skill_points:^+8} | {self._skills[11].skill_level:^7} | {self._skills[11].skill_expertise:<13} |
    | Nature (Int)            | {self._skills[12].skill_points:^+8} | {self._skills[12].skill_level:^7} | {self._skills[12].skill_expertise:<13} |
    | Perception (Wis)        | {self._skills[13].skill_points:^+8} | {self._skills[13].skill_level:^7} | {self._skills[13].skill_expertise:<13} |
    | Perspicacity (Wis)      | {self._skills[14].skill_points:^+8} | {self._skills[14].skill_level:^7} | {self._skills[14].skill_expertise:<13} |
    | Persuasion (Cha)        | {self._skills[15].skill_points:^+8} | {self._skills[15].skill_level:^7} | {self._skills[15].skill_expertise:<13} |
    | Science (Int)           | {self._skills[16].skill_points:^+8} | {self._skills[16].skill_level:^7} | {self._skills[16].skill_expertise:<13} |
    | Spells (Mag)            | {self._skills[17].skill_points:^+8} | {self._skills[17].skill_level:^7} | {self._skills[17].skill_expertise:<13} |
    | Stealth (Dex)           | {self._skills[18].skill_points:^+8} | {self._skills[18].skill_level:^7} | {self._skills[18].skill_expertise:<13} |
    | Survival (Wis)          | {self._skills[19].skill_points:^+8} | {self._skills[19].skill_level:^7} | {self._skills[19].skill_expertise:<13} |
    | Theft (Dex)             | {self._skills[20].skill_points:^+8} | {self._skills[20].skill_level:^7} | {self._skills[20].skill_expertise:<13} |
    |_________________________|__________|_________|_______________|

        '''
        )

            