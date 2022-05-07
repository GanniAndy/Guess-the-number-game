import random
print("Guess the NUMBER game!!!")
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
    input("press enter to exit...")
    quit()
print(f'Hurray!!U guessed the number!It was {number}')


input('press enter to exit...')


