# new_game.py

create_character_txt = [
    "\n          === Character Creation ===",
    '''\nBefore starting your new game, the first thing you have to do is creating a character. In this RPG, the process of character 
creation has 4 steps:''',
    "\n1. Choosing a race",
    "2. Choosing a class",
    "3. Distributing Ability Points",
    "4. Distributing Skill Points",
    '''\nEverything you need to know for making a good choice of race and class for your character, as well as for distributing their 
Ability and Skill Points, can be found in the RPG documentation sections 'Classes and Races' and 'Abilities, Skills and Stats'.''',
    '''\nIf you're new to this RPG, you're highly encouraged to read these sections before continuing. Your choices will strongly impact 
your game!''',
    "\nSo let's go!\n"
]

get_race_txt = [
    "\nNow it's time to choose between one of the following races for your character:",
    '''\nHuman: Humans are the most ambitious of the races. Empathetic, charismatic, and excellent at collaboration, they have founded 
great cities and developed impressive technologies. Their curiosity and determination drive them forward, but their short lifespans 
leave little time for deep reflection compared to elves or dwarves.''',
    '''\nElf: Elves are tall, agile, and deeply connected to nature. Despite more frail than humans and dwarves, their grace and 
dexterity make them swift and skilled, particularly in wilderness settings. With their long lifespans, they spend much time in 
meditation and contemplation. Though clever, they often lack the charisma of humans.''',
    '''\nDwarf: Dwarves are a hardy, ancient race, possibly older than elves. Masters of smithing, stonework, and weapon crafting, 
they excel underground and in close contact with the earth. Stubborn and impulsive, they often clash with elves. Though short in 
stature, dwarves are incredibly strong, but less suited to acrobatics or complex reasoning.''',
    '''
    - Race Ability Bonus:

    | Race    | Str | Dex | Con | Int | Wis | Mag | Cha |
    | --------|-----|-----|-----|-----|-----|-----|-----|
    | Humans  | +0  | +0  | +0  | +0  | -1  | +0  | +1  |
    | Elves   | +0  | +1  | -1  | +0  | +1  | +0  | -1  |
    | Dwarves | +1  | -1  | +1  | +0  | +0  | +0  | +0  |
    '''
]

get_class_txt = [
    "\nNow it's time to choose between one of the following classes for your character:",
    '''\nBard: Bards are versatile performers and storytellers, wielding music, poetry, and charm as tools of magic and influence. 
Their talents inspire allies, confuse enemies, and turn the tide of battle with a well-placed melody or tale. While not as tough 
as fighters, bards thrive on creativity, charisma, and quick thinking.''',
    '''\nRogue: Rogues are masters of stealth and precision, striking from the shadows when least expected. Agile and resourceful, 
they excel at infiltration, traps, and surprise attacks. Though not heavily armored, rogues compensate with cunning, speed, and a 
sinister ability to escape even the direst situations.''',
    '''\nWizard: Wizards are scholars of the arcane, wielding immense magical power through years of study and practice. Though 
physically fragile and reliant on their spellbooks, their knowledge grants them unmatched versatility. A single spell, cast at 
the right moment, can obliterate foes or alter reality itself.''',
    '''\nFighter: Fighters are the backbone of any battlefield, skilled in weaponry and combat tactics. Tough, disciplined, and 
adaptable, they can endure harsh conditions and face enemies head-on. Whether wielding a sword, axe, or shield, fighters rely on 
strength, stamina, and determination to triumph.''',
    '''
    - Class Ability Bonus:

    | Class   | Str | Dex | Con | Int | Wis | Mag | Cha |
    | ------- |-----|-----|-----|-----|-----|-----|-----|
    | Bard    | +0  | +0  | -1  | +0  | +0  | +0  | +1  |
    | Rogue   | -1  | +2  | -1  | +0  | +0  | +0  | +0  |
    | Wizard  | -1  | +0  | -1  | +1  | +0  | +1  | +0  |
    | Fighter | +1  | +0  | +0  | +0  | -1  | +0  | +0  |
    '''
]
