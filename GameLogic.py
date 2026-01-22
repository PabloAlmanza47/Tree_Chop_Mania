import random
import time
import generator

def Logic(player_durability):
    #vars
    coins=0

    #attempts if input is wrong fail
    interactions=[]
    def checker(count,player_durability):
        #vars
        counter = 0
        start_time = time.time()

        #tree
        if count not in [0,21,22,23]:
            print(f'\tType "chop" \033[1m{count}\033[0m times to cut down the tree!')

            #Player time limit to chop tree down
            while time.time() - start_time < (count*0.8):
                user_input = input(">> ").strip().lower()
                if user_input == 'chop':
                    counter += 1
                    print(f"Chops: {counter}/{count}")
                    player_durability-=1
                else:
                    print('Oops, Try Again!')
                    player_durability-=1
                
                #cut down the tree
                if counter >= count:
                    return [True,player_durability]

        #Wolf
        else:
            print(f'\tType "run" \033[1m10\033[0m times to run from the wolf!')

            #Player time limit to run from wolf 
            while time.time() - start_time < 6.5:
                user_input = input(">> ").strip().lower()
                if user_input == 'run':
                    counter += 1
                    print(f"Runs: {counter}/10")
                else:
                    print('Oops, Try Again!')
                
                #ran from wolf
                if counter >= 10:
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
    #Player interaction
    if strength not in [0,21,22,23]:
        #Success
        if bool_holder[0]:
            #Displaying cut tree art
            generator.cut_tree(coins)
            time.sleep(1.5)
            return ['+',coins,bool_holder[1]]
        #Fail
        else:
            generator.uncut_tree(coins)
            time.sleep(1.5)
            return ['-',coins,bool_holder[1]]
    else:
        if bool_holder[0]:
            generator.wolf_success()
            time.sleep(1.5)
            return ['+',5,bool_holder[1]]
        else:
            generator.wolf_fail()
            time.sleep(1.5)
            return ['-',10,bool_holder[1]]