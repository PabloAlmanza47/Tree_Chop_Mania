import random
import time
import generator
import stats

def Logic(player_durability,player_strength=0,player_proficiency=0,player_luck=0,axe_lvl='beginner'):
    #vars
    coins=0
    tier_bonus=stats.AXE_TIERS.index(axe_lvl)

    #attempts if input is wrong fail
    interactions=[]
    def checker(count,player_durability):
        #vars
        counter = 0
        start_time = time.time()

        #tree
        if count not in [0,21,22,23]:
            required=max(1,count-player_strength//3-tier_bonus)
            time_limit=(count*0.8)+(player_proficiency*0.3)
            print(f'\tType "chop" \033[1m{required}\033[0m times to cut down the tree!')

            #Player time limit to chop tree down
            while time.time() - start_time < time_limit:
                user_input = input(">> ").strip().lower()
                if user_input == 'chop':
                    counter += 1
                    print(f"Chops: {counter}/{required}")
                    player_durability-=1
                else:
                    print('Oops, Try Again!')
                    player_durability-=1

                #cut down the tree
                if counter >= required:
                    return [True,player_durability]

        #Wolf
        else:
            required=max(3,10-player_strength//3-tier_bonus)
            time_limit=6.5+(player_proficiency*0.3)
            print(f'\tType "run" \033[1m{required}\033[0m times to run from the wolf!')

            #Player time limit to run from wolf
            while time.time() - start_time < time_limit:
                user_input = input(">> ").strip().lower()
                if user_input == 'run':
                    counter += 1
                    print(f"Runs: {counter}/{required}")
                else:
                    print('Oops, Try Again!')

                #ran from wolf
                if counter >= required:
                    return [True,player_durability]

        #time ran out
        return [False,player_durability]

    #Choosing a random tree to grow
    strength=random.randint(0,23)
    if strength in [0,21,22,23]:
        generator.wolf()
    elif strength <= 5:
        generator.small_tree(strength)
    elif strength <= 10:
        generator.medium_tree(strength)
    else:
        generator.large_tree(strength) 


    coins=random.randint(0,strength//2)
    bool_holder=checker(strength,player_durability)
    luck_bonus=random.randint(0,player_luck//2) if player_luck else 0
    #Player interaction
    if strength not in [0,21,22,23]:
        #Success
        if bool_holder[0]:
            #Displaying cut tree art
            coins+=luck_bonus
            generator.cut_tree(coins)
            time.sleep(1.5)
            return ['+',coins,bool_holder[1]]
        #Fail
        else:
            coins=max(0,coins-player_luck//2)
            generator.uncut_tree(coins)
            time.sleep(1.5)
            return ['-',coins,bool_holder[1]]
    else:
        if bool_holder[0]:
            reward=5+luck_bonus
            generator.wolf_success(reward)
            time.sleep(1.5)
            return ['+',reward,bool_holder[1]]
        else:
            loss=max(0,10-player_luck//2)
            generator.wolf_fail(loss)
            time.sleep(1.5)
            return ['-',loss,bool_holder[1]]