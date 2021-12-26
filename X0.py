import random

def hello():
    print('-------------------')
    print('Добро пожаловать в ИГРУ В КАЛЬМАРА!')
    print('Шутка. Это просто крестики-нолики')
    print('( с не очень умным ботом :Р )')
    print('-------------------')
    print('Для того, чтобы сделать свой ход, необходимо:')
    print('1. Выбрать клетку для хода')
    print('2. Найти сначала номер её строки, затем номер столбца')
    print('3. И записать эти цифры поочереди через пробел')
    print(f'{name}, Вы играете за крестик. УДАЧИ!')
    print('-------------------')

def show_field(f):
    print('  0 1 2 ')
    for i in range(len(field)):
        print(str(i), *field[i])

def user_input(f):
    while True:
        move = input('Введите координаты: ').split()
        if len(move) != 2:
            print('Введите две координаты')
            continue

        if not(move[0].isdigit() and move[1].isdigit()):
            print('Введите числа')
            continue

        x, y = map(int, move)

        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Введите координаты в диапазоне от 0 до 2')
            continue

        if f[x][y] != '-':
            print('Такое поле уже занято')
            continue

        break

    return x, y

def winner(f, user):
    def check_line(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True
    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
            check_line(f[0][n], f[1][n], f[2][n], user) or \
            check_line(f[0][0], f[1][1], f[2][2], user) or \
            check_line(f[2][0], f[1][1], f[0][2], user):
            return True
    return False

def bot(f):
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        if f[x][y] != '-':
            continue
        else:
            return x, y

        break


name = input('Здравствуйте! Представьтесь, пожалуйста! ')
hello()
field = [['-'] * 3 for _ in range(3)]
count = 0
while True:
    if count == 9:
        print('Ничья')
        break
    show_field(field)
    if count % 2 == 0:
        user = 'x'
        print()
        print(f'Ваш ход, {name}: ')
        x, y = user_input(field)
    else:
        user = 'o'
        print()
        print('Ходит бот: ')
        x, y = bot(field)
    field[x][y] = user
    if winner(field, user):
        if user == 'x':
            print('-------------------')
            print(f'Победа! {name}, Вы великолепны!')
        else:
            print('-------------------')
            print('Бот победил! Это его первый шаг на пути к порабощению человечества...')
        show_field(field)
        break
    count += 1