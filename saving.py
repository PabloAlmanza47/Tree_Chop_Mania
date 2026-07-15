import os

SAVE_FILE='save.txt'

#Looks up a saved player by name, returns a stats dict or None if not found
def load_user(user_name):
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE,'r') as main_file:
        for line in main_file:
            line=line.strip()
            if not line:
                continue

            name,data=line.split(':',1)
            if name.lower()==user_name.lower():
                coins,strength,proficiency,luck,axe_lvl,durability=data.split(',')
                return {
                    'coins':int(coins),
                    'strength':int(strength),
                    'proficiency':int(proficiency),
                    'luck':int(luck),
                    'axe_lvl':axe_lvl,
                    'durability':int(durability)
                }
    return None

#Writes the player's current stats to the save file, replacing their prior entry if any
def save_user(user_name,coins,strength,proficiency,luck,axe_lvl,durability):
    lines=[]

    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE,'r') as main_file:
            for line in main_file:
                line=line.strip()
                if not line:
                    continue

                name,_=line.split(':',1)
                if name.lower()!=user_name.lower():
                    lines.append(line)

    lines.append(f'{user_name}:{coins},{strength},{proficiency},{luck},{axe_lvl},{durability}')

    with open(SAVE_FILE,'w') as main_file:
        for line in lines:
            main_file.write(line+'\n')
