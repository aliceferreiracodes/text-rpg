from core.game import Game
from core.character import Character
from core.ability import Ability
from core.skill import Skill
from core.statc import StatC
from time import sleep
from data.ingame_text import create_character_txt
from data.ingame_text import get_race_txt
from data.ingame_text import get_class_txt

def create():
    print(
        '''
          === New Game ===
        '''
    )
    while True:
        input_name = input("Choose a name for your new game up to 50 characters:\n> ")
        confirmation = input("Confirm name:\n> ")
        if not (input_name == confirmation):
            print("Confirmation doesn't match. Try again.\n")
        elif not (len(input_name) <= 50):
            print("Too long! Try again.\n")
        else:
            New_game = Game(input_name)
            print(f"\nGreat! Your new game's name is '{New_game.name}'. Let's get started!")
            break
    create_character()

    input("\nPress 'Enter' to continue.\n")

    


def create_character():
    for x in range(len(create_character_txt)):
        print(create_character_txt[x])
        sleep(1)

    full_name = get_name()
    first_name = full_name.split(" ")[0]
    gender = get_gender()
    race = get_race()
    cclass = get_class()
    ability_bonuses = get_ability_bonuses(race, cclass)
    ability_points = get_ability_points(first_name, ability_bonuses)
    skill_points = get_skill_points(first_name, ability_points)

    con_bonus = ability_bonuses[2]
    mag_bonus = ability_bonuses[5]
    dex_bonus = ability_bonuses[1]

    abilities = init_abilities(ability_bonuses, ability_points)
    skills = init_skills(skill_points)
    stats = init_stats(con_bonus, mag_bonus, dex_bonus, race)

    New_character = Character(full_name, first_name, gender, race, cclass, abilities, skills, stats)
    
    print("\nGood job, you finished character creation! Take a look at your character's info:\n")
    sleep(4)
    New_character.display_info()
    
    
def get_name():
    while True: 
        input_name = input("First, enter a name for your character up to 50 characters (if it is a full name, they will be referred to by their first name in most occasions):\n> ").title()
        confirmation = input("Confirm name:\n> ").title()
        if not (input_name == confirmation):
            print("Confirmation doesn't match. Try again.\n")
        elif not (len(input_name) <= 50):
            print("Too long! Try again.\n")
        else:
            print(f"\nGreat! Your character's name is {input_name}!")
            return input_name


def get_gender():
    while True: 
        input_gender = input("\nEnter character gender (feminine/masculine):\n> ").capitalize()
        if not (input_gender == "Feminine" or input_gender == "Masculine"):
            print("Enter valid option.")
        else:
            while True:
                confirmation = input("Confirm gender (yes/no)?\n> ").lower()
                if confirmation == "yes":
                    return input_gender
                elif confirmation == "no":
                    break
                else:
                    print("Enter valid option.")
            

def get_race():
    for x in range(len(get_race_txt)):
        print(get_race_txt[x])
        sleep(1)
    
    while True:
        input_race = input("\nEnter the desired race (Human, Elf, Dwarf):\n> ").capitalize()
        if not (input_race == "Human" or input_race == "Elf" or input_race == "Dwarf"):
            print("Enter a valid option.\n")
        else:
            while True:
                confirmation = input("Confirm race (yes/no)?\n> ").lower()
                if confirmation == "yes":
                    print(f"\nGreat choice! Your character is a {input_race}!")
                    return input_race
                elif confirmation == "no":
                    break
                else:
                    print("Enter a valid option.")


def get_class():
    for x in range(len(get_class_txt)):
        print(get_class_txt[x])
        sleep(1)

    while True:
        input_class = input("\nEnter the desired class (Bard, Rogue, Wizard, Fighter):\n> ").capitalize()
        if not (input_class == "Bard" or input_class == "Rogue" or input_class == "Wizard" or input_class == "Fighter"):
            print("Enter a valid option.\n")
        else:
            while True:
                confirmation = input("Confirm class (yes/no)?\n> ").lower()
                if confirmation == "yes":
                    print(f"\nGreat choice! Your character is a {input_class}!")
                    return input_class
                elif confirmation == "no":
                    break
                else:
                    print("Enter a valid option.")


def get_ability_points(name, ability_bonuses):
    distributed_points = [0, 0, 0, 0, 0, 0, 0]
    print("\nNow it's time for you to distribute Ability Points between your character's abilities.")
    sleep(1)
    print(f'''\n{name}'s total Ability Points equal the sum of their Ability Bonus and the points you distribute. Here are their 
current Ability Points:''')
    display_ability_points(distributed_points, ability_bonuses, ability_bonuses)
    sleep(1)
    print('''\nNow, you will distribute 5 points among the abilities above. The ability will be shown, and you will enter the number of points you
want to assign to it. You can enter any number from 0 to the number of points you have left.''')

    while True:
        distributed_points = ability_points_input()
        ability_points = [distributed_points[x] + ability_bonuses[x] for x in range(len(ability_bonuses))]
        print("\nThis is how you chose to distribute your character's Ability Points:")
        display_ability_points(distributed_points, ability_points, ability_bonuses)

        while True:
            confirmation = input("\nConfirm this distribution (yes/no)?\n> ").lower()
            if confirmation == "yes":
                print(f"\nGreat!")
                return ability_points
            elif confirmation == "no":
                print("Fine! Let's try again.")
                break
            else:
                print("Enter a valid option.")
    

def ability_points_input():
    ability_list = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Magic", "Charisma"]
    distributed_points = [0, 0, 0, 0, 0, 0, 0]
    points_left = 5

    for x in range(len(ability_list)):
        while True:
            print(f"\nPoints left: {points_left}")
            try:
                num = int(input(f"\nHow many points do you want to assign to {ability_list[x]}?\n> "))
            except ValueError:
                num = -1
            if points_left < num or num < 0:
                print("Please, enter a valid input.")
            else:
                distributed_points[x] = num
                points_left -= num
                break

    return distributed_points


def get_ability_bonuses(race, cclass):
    match race:
        case "Human":
            race_bonuses = [0, 0, 0, 0, -1, 0, 1]
        case "Elf":
            race_bonuses = [0, 1, -1, 0, 1, 0, -1]
        case "Dwarf":
            race_bonuses = [1, -1, 1, 0, 0, 0, 0]

    match cclass:
        case "Bard":
            class_bonuses = [0, 0, -1, 0, 0, 0, 1]
        case "Rogue":
            class_bonuses = [-1, 2, -1, 0, 0, 0, 0]
        case "Wizard":
            class_bonuses = [-1, 0, -1, 1, 0, 1, 0]
        case "Fighter":
            class_bonuses = [1, 0, 0, 0, -1, 0, 0]

    return [race_bonuses[x] + class_bonuses[x] for x in range(len(race_bonuses))] 


def init_abilities(ability_bonuses, ability_points):

    Strength_ability = Ability("Strength", ability_bonuses[0], ability_points[0])
    Dexterity_ability = Ability("Dexterity", ability_bonuses[1], ability_points[1])
    Constitution_ability = Ability("Constitution", ability_bonuses[2], ability_points[2])
    Intelligence_ability = Ability("Intelligence", ability_bonuses[3], ability_points[3])
    Wisdom_ability = Ability("Wisdom", ability_bonuses[4], ability_points[4])
    Magic_ability = Ability("Magic", ability_bonuses[5], ability_points[5])
    Charisma_ability = Ability("Charisma", ability_bonuses[6], ability_points[6])

    return [Strength_ability, Dexterity_ability, Constitution_ability, Intelligence_ability, Wisdom_ability, Magic_ability, Charisma_ability]


def display_ability_points(distributed_points, points, bonuses):
    print(f'''
    |  Character's  | Distributed | Ability | Ability |
    |   Abilities   |   Points    |  Bonus  | Points  |
    |---------------|-------------|---------|---------|
    | Strength      | {distributed_points[0]:^+11} | {bonuses[0]:^+7} | {points[0]:^+7} |
    | Dexterity     | {distributed_points[1]:^+11} | {bonuses[1]:^+7} | {points[1]:^+7} |
    | Constitution  | {distributed_points[2]:^+11} | {bonuses[2]:^+7} | {points[2]:^+7} |
    | Intelligence  | {distributed_points[3]:^+11} | {bonuses[3]:^+7} | {points[3]:^+7} |
    | Wisdom        | {distributed_points[4]:^+11} | {bonuses[4]:^+7} | {points[4]:^+7} |
    | Magic         | {distributed_points[5]:^+11} | {bonuses[5]:^+7} | {points[5]:^+7} |
    | Charisma      | {distributed_points[6]:^+11} | {bonuses[6]:^+7} | {points[6]:^+7} |
    ''')


def get_skill_points(name, ability_points):
    distributed_points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    initial_skill_points = get_initial_skill_points(ability_points)

    print(f"\nAfter allocating {name}'s Ability Points, the last thing to finish creating your character is assigning their Skill Points.")
    sleep(1)
    print('''\nThe Skill Points will affect success rates in every action your character performs throughout the game. In order to determine
the Skill Points, they will initially inherit the Ability Points of the Ability they derive from, as follows:''') 
    sleep(1)
    display_skill_points(initial_skill_points)
    sleep(1)
    print('''Now, you will distribute 15 points among the skills above. The skill will be shown, and you will enter the number of points you
want to assign to it. You can enter any number from 0 to the number of points you have left.''')
    
    while True:
        distributed_points = skill_points_input()
        skill_points = [distributed_points[x] + initial_skill_points[x] for x in range(len(distributed_points))]
        print("\nThis is how you chose to distribute your character's Skill Points:")
        display_skill_points(skill_points)

        while True:
            confirmation = input("\nConfirm this distribution (yes/no)?\n> ").lower()
            if confirmation == "yes":
                return skill_points
            elif confirmation == "no":
                print("Fine! Let's try again.")
                break
            else:
                print("Enter a valid option.")


def skill_points_input():
    skill_list = ["Acrobatics", "Animal Handling", "Athletics", "Brewing", "Charm", "Crafting", "Deception", "Intimidation", 
                  "Investigation", "Magical Botany", "Magical Equipment", "Medicine", "Nature", "Perception", "Perspicacity", "Persuasion", 
                  "Science", "Spells", "Stealth", "Survival", "Theft"]
    distributed_points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    points_left = 15

    for x in range(len(skill_list)):
        while True:
            print(f"\nPoints left: {points_left}")
            try:
                num = int(input(f"\nHow many points you want to assign to {skill_list[x]}?\n> "))
            except ValueError:
                num = -1
            if points_left < num or num < 0:
                print("Please, enter a valid input.")
            else:
                distributed_points[x] = num
                points_left -= num
                break

    return distributed_points


def get_initial_skill_points(ability_points):
    return [
        ability_points[1],
        ability_points[4],
        ability_points[0],
        ability_points[5],
        ability_points[6],
        ability_points[3],
        ability_points[6],
        ability_points[6],
        ability_points[3],
        ability_points[5],
        ability_points[5],
        ability_points[3],
        ability_points[3],
        ability_points[4],
        ability_points[4],
        ability_points[6],
        ability_points[3],
        ability_points[5],
        ability_points[1],
        ability_points[4],
        ability_points[1]
    ]


def init_skills(skill_points):
    
    Acrobatics_skill = Skill("Acrobatics", skill_points[0], 1, "Not Skilled")
    Animal_handling_skill = Skill("Animal Handling", skill_points[1], 1, "Not Skilled")
    Athletics_skill = Skill("Athletics", skill_points[2], 1, "Not Skilled")
    Brewing_skill = Skill("Brewing", skill_points[3], 1, "Not Skilled")
    Charm_skill = Skill("Charm", skill_points[4], 1, "Not Skilled")
    Crafting_skill = Skill("Crafting", skill_points[5], 1, "Not Skilled")
    Deception_skill = Skill("Deception", skill_points[6], 1, "Not Skilled")
    Intimidation_skill = Skill("Intimidation", skill_points[7], 1, "Not Skilled")
    Investigation_skill = Skill("Investigation", skill_points[8], 1, "Not Skilled")
    Magical_botany_skill = Skill("Magical Botany", skill_points[9], 1, "Not Skilled")
    Magical_equipment_skill = Skill("Magical Equipment", skill_points[10], 1, "Not Skilled")
    Medicine_skill = Skill("Medicine", skill_points[11], 1, "Not Skilled")
    Nature_skill = Skill("Nature", skill_points[12], 1, "Not Skilled")
    Perception_skill = Skill("Perception", skill_points[13], 1, "Not Skilled")
    Perspicacity_skill = Skill("Perspicacity", skill_points[14], 1, "Not Skilled")
    Persuasion_skill = Skill("Persuasion", skill_points[15], 1, "Not Skilled")
    Science_skill = Skill("Science", skill_points[16], 1, "Not Skilled")
    Spells_skill = Skill("Spells", skill_points[17], 1, "Not Skilled")
    Stealth_skill = Skill("Stealth", skill_points[18], 1, "Not Skilled")
    Survival_skill = Skill("Survival", skill_points[19], 1, "Not Skilled")
    Theft_skill = Skill("Theft", skill_points[20], 1, "Not Skilled")

    return [Acrobatics_skill, Animal_handling_skill, Athletics_skill, Brewing_skill, Charm_skill, Crafting_skill, Deception_skill, 
            Intimidation_skill, Investigation_skill, Magical_botany_skill, Magical_equipment_skill, Medicine_skill, Nature_skill, 
            Perception_skill, Perspicacity_skill, Persuasion_skill, Science_skill, Spells_skill, Stealth_skill, Survival_skill, Theft_skill]


def display_skill_points(skill_points):
    print(f'''
    |       Character's       |  Skill  |
    |         Skills          |  Points |
    |-------------------------|---------|
    | Acrobatics (Dex)        | {skill_points[0]:^+7} |
    | Animal Handling (Wis)   | {skill_points[1]:^+7} |
    | Athletics (Str)         | {skill_points[2]:^+7} |
    | Brewing (Mag)           | {skill_points[3]:^+7} |
    | Charm (Cha)             | {skill_points[4]:^+7} |
    | Crafting (Int)          | {skill_points[5]:^+7} |
    | Deception (Cha)         | {skill_points[6]:^+7} |
    | Intimidation (Cha)      | {skill_points[7]:^+7} |
    | Investigation (Int)     | {skill_points[8]:^+7} |
    | Magical Botany (Mag)    | {skill_points[9]:^+7} |
    | Magical Equipment (Mag) | {skill_points[10]:^+7} |
    | Medicine (Int)          | {skill_points[11]:^+7} |
    | Nature (Int)            | {skill_points[12]:^+7} |
    | Perception (Wis)        | {skill_points[13]:^+7} |
    | Perspicacity (Wis)      | {skill_points[14]:^+7} |
    | Persuasion (Cha)        | {skill_points[15]:^+7} |
    | Science (Int)           | {skill_points[16]:^+7} |
    | Spells (Mag)            | {skill_points[17]:^+7} |
    | Stealth (Dex)           | {skill_points[18]:^+7} |
    | Survival (Wis)          | {skill_points[19]:^+7} |
    | Theft (Dex)             | {skill_points[20]:^+7} |
    ''')


def init_stats(con_bonus, mag_bonus, dex_bonus, race):
    hp_max_value = 50 + (con_bonus * 10)
    mm_max_value = 50 + (mag_bonus * 10)
    stamina_max_value = 50 + (con_bonus * 10)
    
    match race:
        case "Human":
            speed_base = 10
        case "Elf":
            speed_base = 11
        case "Dwarf": 
            speed_base = 9

    speed_max_value = speed_base + dex_bonus
    
    Health_points_stat = StatC("Health Points", hp_max_value, hp_max_value)
    Magic_meter_stat = StatC("Magic Meter", mm_max_value, mm_max_value)
    Stamina_stat = StatC("Stamina", stamina_max_value, stamina_max_value)
    Speed_stat = StatC("Speed", speed_max_value, speed_max_value)
    Luck_stat = StatC("Luck", 100, 100)
    Perception_stat = StatC("Perception", 100, 100)
    Reputation_stat = StatC("Reputation", 100, 100)

    return [Health_points_stat, Magic_meter_stat, Stamina_stat, Speed_stat, Luck_stat, Perception_stat, Reputation_stat]
