import random
from time import sleep
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
prCyan('@@@@@@@  @    @  @@@@@@    @@@@@@  @@@@@@  @     @  @@@@@@\n'
      '   @     @    @  @         @       @    @  @ @ @ @  @    \n' 
      '   @     @@@@@@  @@@@@     @  @@@  @@@@@@  @  @  @  @@@@@\n'
      '   @     @    @  @         @    @  @    @  @     @  @    \n'
      '   @     @    @  @@@@@@    @@@@@@  @    @  @     @  @@@@@@')
prGreen('Guess the number !Player edition')
sleep(2)
prLightPurple('Made by GanniAndy')
sleep(3)

def helpu():
    prYellow('In this game you will guess a number choosed by computer.\n'
          'After starting the game ,you will choose the limit of the number.\n'
          'ex:(0,20). 20 is the highest number that the computer will want to choice.')
    sleep(3)
    input('press enter to proceed to the main menu...')
def gaming():
    import random
    highnr = int(input('Pick the limit of the numbers: '))
    number = random.randint(0,highnr)
    try:
        for i in range(400):
            user = int(input('guess the number '))
            if user < number:
                print('higher!')
            if user > number:
                print('lower!')
            if user == number:
                break
    except:
        print('blank is not a number.GAME OVER!')
        sleep(5)
        quit()
    prGreen(f'Hurray!!U guessed the number!It was {number}')
    sleep(3)
try:
    while True:
        print('1 -Help\n'
              '2-Start\n'
              '3-QUIT')
        algm = int(input('Type the option number: '))
        if algm == 1:
            helpu()
        if algm == 2:
            gaming()
        if algm == 3:
            print('Have a Good day!')
            sleep(3)
            quit()
except:
    print('Please select an option...')
    sleep(2)