import time
import os 
os.system('cls' if os.name == 'nt' else 'clear')

#vars=
strength=69
proficiency=3247
# luck=0

#Durability display
durability=[
    '[\033[34m██████████\033[0m]',
    '[\033[34m█████████▒\033[0m]',
    '[\033[34m████████▒▒\033[0m]',
    '[\033[34m███████▒▒▒\033[0m]',
    '[\033[36m██████▒▒▒▒\033[0m]',
    '[\033[36m█████▒▒▒▒▒\033[0m]',
    '[\033[36m████▒▒▒▒▒▒\033[0m]',
    '[\033[35m███▒▒▒▒▒▒▒\033[0m]',
    '[\033[35m██▒▒▒▒▒▒▒▒\033[0m]',
    '[\033[31m█▒▒▒▒▒▒▒▒▒\033[0m]',
    '[\033[31m▒▒▒▒▒▒▒▒▒▒\033[0m]'
]

#ASCII art for different axe levels
axes={
    #Axe lvl one
    'beginner_head':'(>|',
    'beginner_body1':'  |',
    'beginner_body2':'  !',
    'beginner_body3':' ',
    'beginner_durability':100,
    

    #Axe lvl two
    'woodcutter_head':'(>+<)',
    'woodcutter_body1':'x',
    'woodcutter_body2':'|',
    'woodcutter_body3':'!', 
    'woodcutter_durability':200,

    #Axe lvl three
    'lumberjack_head':'/\-[]-/\\',
    'lumberjack_body1':'\/-||-\/',
    'lumberjack_body2':'||',
    'lumberjack_body3':'[]',
    'lumberjack_durability':300,

    #Axe lvl four
    'berserker_head':"/`-'\\",
    'berserker_body1':'\,T./',
    'berserker_body2':'|',
    'berserker_body3':'!',
    'berserker_durability':400,

    #Axe lvl five
    'warlord_head':"/\ ) \\",
    'warlord_body1':'<=()=>  )',
    'warlord_body2':'|| )_/',
    'warlord_body3':'||   ',
    'warlord_durability':500
}

#PLAYER STATS
player_stats={
    'player_axeHead':'',
    'player_axeBody1':'',
    'player_axeBody2':'',
    'player_axeBody3':''
}

#Main stats dict
def get_stats_text(player_name):
    return {
        'player':f'\033[1mPlayer: \033[0m "{player_name}"',
        'line1':f'\033[1mAxe Lvl:\033[0m',
        'line2':f'\033[35m {player_stats["player_axeHead"]}\033[0m',
        'line3':f'\033[35m {player_stats["player_axeBody1"]}\033[0m',
        'line4':f'\033[35m {player_stats["player_axeBody2"]}\033[0m',
        'line5':f'\033[35m {player_stats["player_axeBody3"]}\033[0m'
}

#Dynamically sets player's axe appearance based on current level
def update_axe(level):
    player_stats['player_axeHead']=axes.get(f'{level}_head')
    player_stats['player_axeBody1']=axes.get(f'{level}_body1')
    player_stats['player_axeBody2']=axes.get(f'{level}_body2')
    player_stats['player_axeBody3']=axes.get(f'{level}_body3')

#Stats display ---MAIN FUNCTION
def stats_display(coins,player_durability,player_name,axe_lvl):
    update_axe(axe_lvl)
    stats_text=get_stats_text(player_name)
    print(f'''
\033[1;32m╔═════════════╗\033[0m \033[1;32m╔═══════════════════════════════════════════╗\033[0m \033[1;32m╔══════════════════╗\033[0m
\033[1;32m║\033[0m{(stats_text['line1']).center(21)}\033[1;32m║ ║\033[0m{(stats_text['player']).center(50)} \033[1;32m║ ║\033[0m     \033[1mOPTIONS:\033[0m     \033[1;32m║\033[0m
\033[1;32m║\033[0m{axe_lvl.center(13)}\033[1;32m║ ║\033[0m                  \033[1mSTATS\033[0m                    \033[1;32m║ ║\033[0m                  \033[1;32m║\033[0m
\033[1;32m║\033[0m{(stats_text['line2']).center(22)}\033[1;32m║ ║\033[0m \033[1mCoins:\033[0m {str(coins).ljust(34)} \033[1;32m║ ║\033[0m \033[31m 1.\033[0m Save & Exit  \033[1;32m║\033[0m
\033[1;32m║\033[0m{(stats_text['line3']).center(22)}\033[1;32m║ ║\033[0m \033[1mStrength:\033[0m {str(strength).ljust(31)} \033[1;32m║ ║\033[0m \033[31m 2.\033[0m Shop         \033[1;32m║\033[0m
\033[1;32m║\033[0m{(stats_text['line4']).center(22)}\033[1;32m║ ║\033[0m \033[1mProficiency:\033[0m {str(proficiency).ljust(28)} \033[1;32m║ ║\033[0m \033[31m 3.\033[0m Continue     \033[1;32m║\033[0m
\033[1;32m║\033[0m{(stats_text['line5']).center(22)}\033[1;32m║ ║\033[0m \033[1mDurability:\033[0m {get_durability_bar(player_durability,axe_lvl).ljust(43)} \033[1;32m║ ║                  ║\033[0m
\033[1;32m╚═════════════╝\033[0m \033[1;32m╚═══════════════════════════════════════════╝\033[0m \033[1;32m╚══════════════════╝\033[0m
''',end='')

def get_durability_bar(player_durability,axe_lvl):
    # Calculate index (0 = full, 10 = empty)
    if player_durability<0:
        player_durability=0
    index = min(10, 10 - int((player_durability / axes.get(f'{axe_lvl}_durability'))*10))
    return (durability[index].ljust(22)+f'{player_durability}/\033[32m'+str(axes.get(f'{axe_lvl}_durability')))



#DISPLAY
# while player_durability>=0:
#     stats_display()
#     player_durability-=1
#     time.sleep(0.05) 
# else:
#     print('\tDone!')





