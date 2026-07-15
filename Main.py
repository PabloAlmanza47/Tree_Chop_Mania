import time
import GameLogic
import stats
import shop
import saving
from Forest_generator.loading_screen import LoadingScreen
import Forest_generator.loading_text as loadingText


#Player vars
coins=0
axe_lvl='beginner'
strength=0
proficiency=0
luck=0
player_durability=stats.axes.get(f'{axe_lvl}_durability')

#Loading Screen
LoadingScreen()

#Asking the user if they are ready to begin
player_name=input('Input your name to start >> ').capitalize()

#Loading any existing save for this player
save_data=saving.load_user(player_name)
if save_data:
    coins=save_data['coins']
    strength=save_data['strength']
    proficiency=save_data['proficiency']
    luck=save_data['luck']
    axe_lvl=save_data['axe_lvl']
    player_durability=save_data['durability']
    print(f'\nWelcome back, {player_name}!')
else:
    print(f'\nCreating a new save for {player_name}...')

print('\nType "chop" as fast as you can to cut down the tree!')
time.sleep(2)
loadingText.line()
time.sleep(.5)


#Game run variable & Main game loop
while True:

    #Main Game Logic w/ coins
    temp=GameLogic.Logic(player_durability,strength,proficiency,luck,axe_lvl)
    player_durability=temp[2]
    if temp[0] == '-':
        coins-=temp[1]
    else:
        coins+=temp[1]
    coins=max(0,coins)

    #Axe breaks once durability is exhausted, forcing a repair
    if player_durability<=0:
        print('\nYour axe has broken!')
        coins,player_durability=shop.repair_axe(coins,axe_lvl)

    #Asking the user if they wish to continue playing
    loadingText.line()
    player_resonse=0
    stats.stats_display(coins,player_durability,player_name,axe_lvl,strength,proficiency)
    while player_resonse not in ['1','2','3']:
        player_resonse=input('Please select a state: ')

    #Players choice [Save & End, Shop, Continue]
    if player_resonse == '1':
        break
    elif player_resonse =='2':
        loadingText.line()
        coins,strength,proficiency,luck,axe_lvl,player_durability=shop.shop_menu(coins,strength,proficiency,luck,axe_lvl,player_durability)

    time.sleep(.5)
    loadingText.line()




#Game over text
saving.save_user(player_name,coins,strength,proficiency,luck,axe_lvl,player_durability)

intro_text=['Saving Progress','Saving Progress.','Saving Progress..','Saving Progress...','Saving Progress....']
CLEAR_LINE = '\033[K'
for i in 2*intro_text :
    time.sleep(0.4)
    print('\r'+i+CLEAR_LINE, end="",flush=True)
print('''\r\033[KProgress Saved!\033[0m''',flush=True)
time.sleep(.5)

print('════════════════════════════════════════════════════════════════[GAME OVER]═══════════════════════════════════════════════════════════════════════════')
stats.stats_display(coins,player_durability,player_name,axe_lvl,strength,proficiency)
time.sleep(3)



#Chuncking tree down add percent that it may auto chop tree or fail