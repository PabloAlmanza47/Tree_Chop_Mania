import time
import GameLogic
import stats
import shop
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
print('\nType "chop" as fast as you can to cut down the tree!')
time.sleep(2)  
loadingText.line() 
time.sleep(.5)


#Game run variable & Main game loop
while True:

    #Main Game Logic w/ coins
    temp=GameLogic.Logic(player_durability)
    player_durability=temp[2]
    if temp[0] == '-':
        coins-=temp[1]
    else:
        coins+=temp[1]

    #Asking the user if they wish to continue playing
    loadingText.line()
    player_resonse=0
    stats.stats_display(coins,player_durability,player_name,axe_lvl)
    while player_resonse not in ['1','2','3']:
        player_resonse=input('Please select a state: ')

    #Players choice [Save & End, Shop, Continue]
    if player_resonse == '1':
        break
    elif player_resonse =='2':
        loadingText.line()
        shop.shop_display(strength,proficiency,luck,coins)

    time.sleep(.5)
    loadingText.line() 




#Game over text
intro_text=['Saving Progress','Saving Progress.','Saving Progress..','Saving Progress...','Saving Progress....']
CLEAR_LINE = '\033[K'
for i in 2*intro_text :
    time.sleep(0.4)
    print('\r'+i+CLEAR_LINE, end="",flush=True)
print('''\r\033[KProgress Saved!\033[0m''',flush=True)
time.sleep(.5)

print('════════════════════════════════════════════════════════════════[GAME OVER]═══════════════════════════════════════════════════════════════════════════')
stats.stats_display(coins,player_durability,player_name)
time.sleep(3)



#Chuncking tree down add percent that it may auto chop tree or fail