import pyfiglet
import keyboard


def game(bullets: int, positin: str) -> str:
    count = 1
    pistol_clip = {x: False for x in range(1, 7)}
    positin = [int(x) for x in positin]

    if len(positin) != bullets:
        return 'Input uncorrectable value'
        
    for k,v in pistol_clip.items():
        if k in positin:
            pistol_clip[k] = True

    print('CLIP ARE RUNNING...')
    while True:
        if count >= 6:
            count = 1
        count += 1
        if keyboard.is_pressed('1'):
            res = pistol_clip.get(count)
            if res:
                return 'YOU DIE!'
            else:
                return 'YOU WILL LIVE!'
    
print(f"""
        {pyfiglet.figlet_format("Welcome to Russian Roulette")}
        1: Play
        2: Rules
        3: Exit
        """)

while True:
    choise = int(input('Select action: '))

    if choise == 1:
        print(f'{pyfiglet.figlet_format("GAME START !")}')
        count_bullets = int(input('Pls input count bullets in clip: '))
        bull_posit = input('Input positione for bullet in a clip (PLS USE SPACE): ').split(' ')
        print(game(count_bullets, bull_posit)) 

    elif choise == 2:
        print(f"""
            {pyfiglet.figlet_format("RULES")}

            Hello!
            It's Russian Rulette game, there you can try survive or not :)

            When game will start you should write:

                1 - How mouch bullets you want load into the gun
                2 - Choise where your bullet will be in your clip
                3 - When clip will start spin you should stop that with number 1 on your keyboard 
                4 - And the last one HAVE FUN!)
        """)
    
    elif choise == 3:
        print(f'{pyfiglet.figlet_format("GOODBYE !")}')
        break

    else:
        print('There is not such number, pls send correct number!')
