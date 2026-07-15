import stats

ATTRIBUTE_MAX=10
ATTRIBUTE_COST_STEP=15

def _attribute_cost(level):
    return (level+1)*ATTRIBUTE_COST_STEP

#Spends coins to raise one attribute (strength/proficiency/luck) by one level
def buy_attribute(coins,level,name):
    if level>=ATTRIBUTE_MAX:
        print(f'\n{name} is already maxed out!')
        return coins,level
    cost=_attribute_cost(level)
    if coins<cost:
        print(f'\nNot enough coins! {name} upgrade costs {cost} coins.')
        return coins,level
    print(f'\n{name} upgraded to {level+1} for {cost} coins!')
    return coins-cost,level+1

#Spends coins to move up to the next axe tier, granting that axe's full durability
def buy_axe(coins,axe_lvl,player_durability):
    tiers=stats.AXE_TIERS
    current_index=tiers.index(axe_lvl)
    if current_index>=len(tiers)-1:
        print('\nYou already own the best axe!')
        return coins,axe_lvl,player_durability
    next_tier=tiers[current_index+1]
    cost=stats.AXE_COSTS[next_tier]
    if coins<cost:
        print(f'\nNot enough coins! The {next_tier.capitalize()} axe costs {cost} coins.')
        return coins,axe_lvl,player_durability
    new_durability=stats.axes.get(f'{next_tier}_durability')
    print(f'\nPurchased the {next_tier.capitalize()} axe for {cost} coins!')
    return coins-cost,next_tier,new_durability

#Repairs the current axe, fully if affordable, otherwise as much as coins allow
def repair_axe(coins,axe_lvl):
    full=stats.axes.get(f'{axe_lvl}_durability')
    cost=max(1,full//5)
    if coins>=cost:
        print(f'\nAxe fully repaired for {cost} coins!')
        return coins-cost,full
    durability=max(full//10,coins*5)
    print(f'\nNot enough coins for a full repair. Partially repaired using all {coins} coins.')
    return 0,durability




# ⛃⛂⛁⛀
def shop_display(strength,proficiency,luck,coins,axe_lvl):
    print(f'''
\033[1;32m╔{'══'*51}╗\033[0m
\033[1;32m║\033[0m                                                                                                      \033[1;32m║\033[0m
\033[1;32m║\033[0m                            ▄████████    ▄█    █▄     ▄██████▄     ▄███████▄                          \033[1;32m║\033[0m
\033[1;32m║\033[0m                            ███    ███   ███    ███   ███    ███   ███    ███                         \033[1;32m║\033[0m
\033[1;32m║\033[0m                            ███    █▀    ███    ███   ███    ███   ███    ███                         \033[1;32m║\033[0m
\033[1;32m║\033[0m                            ███         ▄███▄▄▄▄███▄▄ ███    ███   ███    ███                         \033[1;32m║\033[0m
\033[1;32m║\033[0m                          ▀███████████ ▀▀███▀▀▀▀███▀  ███    ███ ▀█████████▀                          \033[1;32m║\033[0m
\033[1;32m║\033[0m                                   ███   ███    ███   ███    ███   ███                                \033[1;32m║\033[0m
\033[1;32m║\033[0m                             ▄█    ███   ███    ███   ███    ███   ███                                \033[1;32m║\033[0m
\033[1;32m║\033[0m                           ▄████████▀    ███    █▀     ▀██████▀   ▄████▀                              \033[1;32m║\033[0m
\033[1;32m║\033[0m                                                                                                      \033[1;32m║\033[0m
\033[1;32m╚{'══'*51}╝\033[0m''',end='')

    print(f'''
\033[1;32m╔{'══'*51}╗\033[0m 
\033[1;32m║\033[0m                                     _____  __  __  _____  _____                                      \033[1;32m║\033[0m 
\033[1;32m║\033[0m                                    /  _  \/  \/  \/   __\/  ___>                                     \033[1;32m║\033[0m 
\033[1;32m║\033[0m                                    |  _  |>-    -<|   __||___  |                                     \033[1;32m║\033[0m 
\033[1;32m║\033[0m                                    \__|__/\__/\__/\_____/<_____/                                     \033[1;32m║\033[0m 
\033[1;32m║\033[0m                                                                                                      \033[1;32m║\033[0m
\033[1;32m╚{'══'*51}╝''',end='')

    print(f'''   
\033[1;32m╔{'═'*18}╗\033[0m \033[1;32m╔{'═'*18}╗\033[0m \033[1;32m╔{'═'*18}╗\033[0m \033[1;32m╔{'═'*18}╗\033[0m \033[1;32m╔{'═'*18}╗\033[0m
\033[1;32m║\033[0m\033[1m{'Beginner'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[1m{'Woodcutter'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[1m{'Lumberjack'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[1m{'Berserker'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[1m{'Warlord'.center(18)}\033[0m\033[1;32m║                      
\033[1;32m║\033[0m\033[35m{'(>|'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[35m{'(>+<)'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[35m     /\-[]-/\\     \033[0m\033[1;32m║ ║\033[0m\033[35m      /`-'\\       \033[0m\033[1;32m║ ║\033[0m\033[35m      /\ ) \\      \033[0m\033[1;32m║\033[0m
\033[1;32m║\033[0m\033[35m{'  |'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[35m{'x'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[35m     \/-||-\/     \033[0m\033[1;32m║ ║\033[0m\033[35m      \,T./       \033[0m\033[1;32m║ ║\033[0m\033[35m{'<=()=>  )'.center(18)}\033[0m\033[1;32m║\033[0m
\033[1;32m║\033[0m\033[35m{'  !'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[35m{'|'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[35m{'||'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[35m{'|'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[35m{'|| )_/'.center(18)}\033[0m\033[1;32m║\033[0m
\033[1;32m║\033[0m\033[35m{''.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[35m{'!'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[35m{'[]'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[35m{'!'.center(18)}\033[0m\033[1;32m║ ║\033[0m\033[35m{'||   '.center(18)}\033[0m\033[1;32m║\033[0m
\033[1;32m║\033[0m      \033[1m10\033[0m\033[33m ⛂⛁⛀      \033[0m\033[1;32m║ ║\033[0m      \033[1m20\033[0m\033[33m ⛂⛁⛃      \033[0m\033[1;32m║ ║\033[0m      \033[1m30\033[0m\033[33m ⛂⛁⛀      \033[0m\033[1;32m║ ║\033[0m      \033[1m40\033[0m\033[33m ⛂⛁⛃      \033[0m\033[1;32m║ ║\033[0m      \033[1m50\033[0m\033[33m ⛂⛁⛃      \033[0m\033[1;32m║\033[0m
\033[1;32m╚{'═'*18}╝\033[0m \033[1;32m╚{'═'*18}╝\033[0m \033[1;32m╚{'═'*18}╝\033[0m \033[1;32m╚{'═'*18}╝\033[0m \033[1;32m╚{'═'*18}╝\033[0m''',end='')

    print(f'''
\033[1;32m╔{'══'*51}╗\033[0m
\033[1;32m║\033[0m                                   _______ __     __ __ __                                            \033[1;32m║
\033[1;32m║\033[0m                                  |     __|  |--.|__|  |  |.-----.                                    \033[1;32m║      
\033[1;32m║\033[0m                                  |__     |    < |  |  |  ||__ --|                                    \033[1;32m║   
\033[1;32m║\033[0m                                  |_______|__|__||__|__|__||_____|                                    \033[1;32m║  \033[0m 
\033[1;32m║\033[0m                                                                                                      \033[1;32m║\033[0m
\033[1;32m╚{'══'*51}╝\033[0m''',end='')

    print(f'''   
\033[1;32m╔{'═'*32}╗\033[0m \033[1;32m╔{'═'*32}╗\033[0m \033[1;32m╔{'═'*32}╗\033[0m 
\033[1;32m║\033[0m\033[1m{'Strength'.center(32)}\033[0m\033[1;32m║ ║\033[0m\033[1m{'Proficiency'.center(32)}\033[0m\033[1;32m║ ║\033[0m\033[1m{'Luck'.center(32)}\033[0m\033[1;32m║\033[0m

\033[1;32m╚{'═'*32}╝\033[0m \033[1;32m╚{'═'*32}╝\033[0m \033[1;32m╚{'═'*32}╝\033[0m
\033[1;32m╔{'═'*32}╗\033[0m \033[1;32m╔{'═'*32}╗\033[0m \033[1;32m╔{'═'*32}╗\033[0m 
\033[1;32m║\033[0m\033[1m{(str(strength)+'/10').center(32)}\033[0m\033[1;32m║ ║\033[0m\033[1m{(str(proficiency)+'/10').center(32)}\033[0m\033[1;32m║ ║\033[0m\033[1m{(str(luck)+'/10').center(32)}\033[0m\033[1;32m║\033[0m
\033[1;32m╚{'═'*32}╝\033[0m \033[1;32m╚{'═'*32}╝\033[0m \033[1;32m╚{'═'*32}╝\033[0m
    Coins: {coins}
    Current axe: {axe_lvl.capitalize()}''')

#Interactive shop menu ---MAIN FUNCTION, returns the (possibly updated) player stats
def shop_menu(coins,strength,proficiency,luck,axe_lvl,player_durability):
    shop_display(strength,proficiency,luck,coins,axe_lvl)

    while True:
        print(f'''
    1. Upgrade Strength  ({_attribute_cost(strength)} coins)
    2. Upgrade Proficiency ({_attribute_cost(proficiency)} coins)
    3. Upgrade Luck ({_attribute_cost(luck)} coins)
    4. Buy next axe tier
    5. Repair axe
    0. Leave shop
    Coins: {coins}''')
        choice=input('What would you like to do? ').strip()

        if choice=='1':
            coins,strength=buy_attribute(coins,strength,'Strength')
        elif choice=='2':
            coins,proficiency=buy_attribute(coins,proficiency,'Proficiency')
        elif choice=='3':
            coins,luck=buy_attribute(coins,luck,'Luck')
        elif choice=='4':
            coins,axe_lvl,player_durability=buy_axe(coins,axe_lvl,player_durability)
        elif choice=='5':
            coins,player_durability=repair_axe(coins,axe_lvl)
        elif choice=='0':
            break
        else:
            print('\nPlease enter a valid choice')

    return coins,strength,proficiency,luck,axe_lvl,player_durability