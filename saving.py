user_name=input('Enter your username to start >> ').strip().lower()


#checking to see if the users information is already saved in the file
with open('save.txt','a+') as main_file:
    main_file.seek(0) #Moves the cursor back to the beginning of the file
    found=False

    #searching for the user
    for line in main_file:
        name,stats=line.strip().split(':')

        if name.lower()==user_name:
            coins,strength=map(int,stats.split(','))
            print(f'Welcome back, {name.capitalize()}!\n\tCoins: {coins}\n\tStrength: {strength}')
            found=True
            break

    #Creating a new save file for the playerr
    if not found:
        print(f'Creating  a new save for {user_name.capitalize()}...')
        coins=0
        strength=0
        main_file.write(f'{user_name}:{coins},{strength}\n')


def update_user_data(user_name,coins,strength):
    updated_lines = []

    with open('save.txt', 'r') as main_file:


        for line in main_file:
            line = line.strip()

            #Empty line
            if not line:
                continue

            name, stats = line.split(':')
            # Updating users information if name is found
            if name.lower() == user_name.lower():
                updated_lines.append(f"{name}:{coins},{strength}")
                user_found = True

            #Keeping the rest of the information the same
            else:
                updated_lines.append(line)

    # Write all lines back to the file
    with open('save.txt', 'w') as main_file:
        for line in updated_lines:
            main_file.write(line + '\n')

