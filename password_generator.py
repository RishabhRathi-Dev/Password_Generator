from random import *

def rand_num():
    x = randrange(0, 10, 1)
    return str(x)

def rand_alpha():
    x = randrange(97, 123, 1)
    return chr(x)

allowed_sp_symbol = ['@', '#', '!', '?', '&']
allowed_re_symbol = ['%', '^', '*', '=', '-', '.', ',']

password = []

no_num = randrange(3,6,1)
no_alpha = randrange(4,7,1)
no_re_symbol = randrange(2,5,1)
no_sp_symbol = randrange(2,4,1)

running = True

while running:
    for i in range(no_num):
        password.append(rand_num())

    for i in range(no_alpha):
        if i%2 == 0:
            password.append(rand_alpha())
        else:
            password.append(rand_alpha().upper())

    for i in range(no_re_symbol):
        password.append(choice(allowed_re_symbol))

    for i in range(no_sp_symbol) :
        password.append(choice(allowed_sp_symbol))

    if len(password)>12 :
        shuffle(password)
        passwrd = ''.join(password)
        print('Password: ', passwrd)
        print('Press Enter to generate another')
        print('Enter 0 to exit')

        cond = input()

        if cond == '0' :
            running = False
            break
        else :
            running = True

    password.clear()
