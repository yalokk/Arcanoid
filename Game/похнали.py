import pygame
import sys
from pygame import mixer

'''Класс Меню'''


class Menu:
    def __init__(self, items):
        self.items = items

    # items = [x, y, name, color, active_color, number_item]]

    '''Выделение активных пункто меню'''

    def render(self, area, font, number_item):
        for i in self.items:
            if number_item == i[5]:
                area.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                area.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        is_game_running = True
        font_menu = pygame.font.Font('font/Foo.otf', 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        item = 0
        while is_game_running:
            screen = pygame.image.load('image/menu_down.png')
            status_bar = pygame.image.load('image/menu_up.png')

            mouse_pos = pygame.mouse.get_pos()
            for i in self.items:
                if (mouse_pos[0] > i[0]) and (mouse_pos[0] < (i[0] + 155)) and \
                        (mouse_pos[1] > i[1] + 45) and (mouse_pos[1] < i[1] + 95):
                    item = i[5]
            self.render(screen, font_menu, item)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if item == 0:
                        is_game_running = False
                    elif item == 1:
                        sys.exit()

            window.blit(status_bar, (0, 0))
            window.blit(screen, (0, 45))
            pygame.display.flip()


'''Класс объектов игры'''


class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((255, 255, 255))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))


'''Подкласс Кирпичи'''


class Brick(Sprite):
    def __init__(self, xpos, ypos, filename, score):
        self.x = xpos
        self.y = ypos
        self.len = 70
        self.height = 70
        self.bitmap = pygame.image.load(filename)
        self.score = score

    def Intersect_with_Sob(self, sob_x, sob_y):

        if ((sob_y + 45 >= self.y) and (sob_y + 45 <= self.y + 10)) or \
                ((sob_y <= self.y + 70) and (sob_y >= self.y + 60)):
            Soboleva.go_down = not Soboleva.go_down
        elif ((sob_x + 45 >= self.x) and (sob_x + 45 <= self.x + 10)) or \
                ((sob_x <= self.x + 70) and (sob_x >= self.x + 60)):
            Soboleva.go_right = not Soboleva.go_right
        else:
            Soboleva.go_down = not Soboleva.go_down


'''Класс объектов строки состояния'''


class Indicator(Sprite):
    def render(self):
        status_bar.blit(self.bitmap, (self.x, self.y))


'''Функции для окончания игры'''


def game_over():
    if health == 0:
        return True
    else:
        return False


def congratulations():
    if total_score == 118:
        return True
    else:
        return False


'''Передвижение Эмиля, Захара и Коли'''


def ezk_go(name, step):
    if name.go_right:
        name.x += step
        if name.x > 560:
            name.go_right = False
    else:
        name.x -= step
        if name.x <= 0:
            name.go_right = True


'''Передвижение Нади и Лизы'''


def nl_go(name):
    if name.go_down:
        name.y += 8
        if name.y >= 280:
            name.go_down = False
    else:
        name.y -= 8
        if name.y <= 210:
            name.go_down = True


'''Пересечение 2х объектов'''


def Intersect(x1, x2, y1, y2, len1, len2, height1, height2):
    if (x1 > x2 - len1) and (x1 < x2 + len2) and (y1 > y2 - height1) and (y1 < y2 + height2):
        return 1
    else:
        return 0


'''Описание кирпичей'''
emil = Brick(0, 0, 'image/emil.png', 10)
emil.go_right = True

kolya = Brick(0, 70, 'image/kolya.png', 8)
kolya.go_right = True
kolya2 = Brick(140, 210, 'image/kolya.png', 8)
kolya.go_right = True

zahar = Brick(560, 70, 'image/zahar.png', 8)
zahar.go_right = True
zahar2 = Brick(420, 210, 'image/zahar.png', 8)
zahar.go_right = True

sergo = Brick(560, 140, 'image/sergo.png', 0)
sergo2 = Brick(0, 140, 'image/sergo.png', 0)

liza = Brick(0, 210, 'image/liza.png', 6)
liza.go_down = True
nadya = Brick(560, 210, 'image/nadya.png', 6)
nadya.go_down = True
liza2 = Brick(490, 280, 'image/liza.png', 6)
liza2.go_down = False
nadya2 = Brick(70, 280, 'image/nadya.png', 6)
nadya2.go_down = False

lesha = Brick(280, 140, 'image/lesha.png', 4)
lesha2 = Brick(210, 210, 'image/lesha.png', 4)
lesha3 = Brick(350, 210, 'image/lesha.png', 4)
lesha4 = Brick(280, 280, 'image/lesha.png', 4)
lesha5 = Brick(70, 350, 'image/lesha.png', 4)

gleb = Brick(140, 140, 'image/gleb.png', 4)
gleb2 = Brick(420, 140, 'image/gleb.png', 4)
gleb3 = Brick(210, 280, 'image/gleb.png', 4)
gleb4 = Brick(350, 280, 'image/gleb.png', 4)
gleb5 = Brick(560, 350, 'image/gleb.png', 4)

margo = Brick(210, 140, 'image/margo.png', 2)
margo2 = Brick(350, 140, 'image/margo.png', 2)
margo3 = Brick(140, 280, 'image/margo.png', 2)
margo4 = Brick(420, 280, 'image/margo.png', 2)
margo5 = Brick(0, 350, 'image/margo.png', 2)

andrey = Brick(70, 140, 'image/andrey.png', 4)
andrey2 = Brick(280, 210, 'image/andrey.png', 4)
andrey3 = Brick(490, 140, 'image/andrey.png', 4)
andrey4 = Brick(490, 350, 'image/andrey.png', 4)

bricks = [emil, kolya, kolya2, zahar, zahar2, liza, nadya, liza2, nadya2, lesha, lesha2, lesha3, lesha4,
          gleb, gleb2, gleb3, gleb4, margo, margo2, margo3, margo4, andrey, andrey2, andrey3, sergo, sergo2]

'''Подсчет здоровья и очков'''
health = 3
total_score = 0

'''окно'''
window = pygame.display.set_mode((630, 705))
pygame.display.set_caption('Оля, смари')
'''холст'''
screen = pygame.Surface((630, 660))
'''строка состояния'''
status_bar = pygame.Surface((630, 45))
x = 0
y = 0
health_image = Indicator(537, 7, 'image/health.png')
score_image = Indicator(33, 7, 'image/score.png')

'''шрифты строки состояния, cooбщений о конце игры'''
pygame.font.init()
health_font = pygame.font.Font('font/AC Line.otf', 25)
score_font = pygame.font.Font('font/AC Line.otf', 25)
mes_game_over = pygame.font.Font('font/foo.otf', 95)
mes_congratulations = pygame.font.Font('font/foo.otf', 64)
mess_send_down = pygame.font.Font('font/foo.otf', 35)
mes_pressEsc = pygame.font.Font('font/AC Line.otf', 25)

'''Конец игры'''
screen_end = pygame.Surface((630, 660))
status_bar_end = pygame.Surface((630, 45))

'''Описание пашки Соболевой (мяч)'''
Soboleva = Sprite(360, 600, 'image/soboleva.png')  # поправить стартовые координаты Соболевой
Soboleva.go_right = True
Soboleva.go_down = True
stepX_sob = 2
stepY_sob = 5
'''Описание ракетки'''
racket = Sprite(340, 640, 'image/racket.png')
step_rac = 9

'''создаем меню'''
items = [(260, 500, 'Game', (254, 9, 13), (250, 216, 25), 0),
         (265, 570, 'Quit', (254, 9, 13), (250, 216, 25), 1)]
game = Menu(items)
game.menu()

'''Звук'''
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
sound = pygame.mixer.Sound('mus/funnyENG.ogg')
'''Воспроизведение звука'''
sound.play(-1)
hit = mixer.Sound('mus/Sergo.ogg')

'''ИГРОВОЙ ЦИКЛ'''

'''подготовка к запуску игры'''
is_game_running = True
pygame.key.set_repeat(1, 1)
pygame.mouse.set_visible(False)
pygame.mixer.pause()

while is_game_running:

    pygame.mixer.unpause()

    '''Обработчик событий'''
    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            is_game_running = False

        if e.type == pygame.KEYDOWN:
            '''событие - перемещение ракетки с помощью клавиш'''
            if e.key == pygame.K_LEFT:
                if racket.x > 0:
                    racket.x -= step_rac
            if e.key == pygame.K_RIGHT:
                if racket.x < 570:
                    racket.x += step_rac
            '''событие - выход в меню'''
            if e.key == pygame.K_ESCAPE:
                pygame.mixer.pause()
                game.menu()
                pygame.key.set_repeat(1, 1)
                pygame.mouse.set_visible(False)

    '''фон игры'''
    screen = pygame.image.load('image/screen.png')
    '''информационная строка'''
    status_bar = pygame.image.load('image/status_bar.png')

    '''передвижение Соболевой - столкновение о стены'''
    if Soboleva.go_right:
        Soboleva.x += stepX_sob
        if Soboleva.x > 585:
            Soboleva.go_right = False
    else:
        Soboleva.x -= stepX_sob
        if Soboleva.x <= 0:
            Soboleva.go_right = True

    if Soboleva.go_down:
        Soboleva.y += stepY_sob
        if Soboleva.y >= 615:
            Soboleva.go_down = False
    else:
        Soboleva.y -= stepY_sob
        if Soboleva.y <= 0:
            Soboleva.go_down = True

    '''Передвижение Эмиля, Захара, Коли, Нади и Лизы'''
    ezk_go(emil, 11)
    ezk_go(zahar, 9)
    ezk_go(kolya, 9)
    nl_go(nadya)
    nl_go(liza)
    nl_go(nadya2)
    nl_go(liza2)

    '''Проверка сталкивания Соболевой и ракетки'''
    if Intersect(racket.x, Soboleva.x, racket.y, Soboleva.y, 60, 45, 20, 45):
        Soboleva.go_down = False

    '''Проверка столкновения Соболевой и кирпича'''
    for i in bricks:
        if i in bricks[-2:]:
            if Intersect(i.x, Soboleva.x, i.y, Soboleva.y, 70, 45, 70, 45):
                Soboleva.go_down = not Soboleva.go_down
                stepX_sob += 0.5
                stepY_sob += 1.5
                break

        if i in bricks[:-2]:
            if Intersect(i.x, Soboleva.x, i.y, Soboleva.y, 70, 45, 70, 45):
                i.Intersect_with_Sob(Soboleva.x, Soboleva.y)
                total_score += i.score
                bricks.remove(i)
                break

    '''Минус очки в случае удара о пол'''
    if Soboleva.y >= 615:
        hit.play()
        health -= 1

    '''отрисовка объектов'''
    for i in bricks:
        i.render()
    racket.render()
    Soboleva.render()
    '''отрисовка показателей и текста строки состояния'''
    score_image.render()
    health_image.render()
    status_bar.blit(score_font.render(str(total_score), 0, (0, 0, 0)), (73, 12))
    status_bar.blit(health_font.render(str(health), 0, (0, 0, 0)), (578, 12))
    window.blit(status_bar, (0, 0))
    '''отрисовка холста'''
    window.blit(screen, (0, 45))
    pygame.display.flip()

    '''Проверка окончания игры'''
    game_over()
    congratulations()

    '''Игра проиграна'''
    while game_over():
        pygame.mixer.pause()
        screen_end = pygame.image.load('image/screen_end.png')
        status_bar_end = pygame.image.load('image/status_bar_end.png')
        screen_end.blit(mes_game_over.render('GAME OVER', 0, (252, 8, 10)), (75, 300))
        screen_end.blit(mess_send_down.render('Ученики нокаутировали Вас', 0, (252, 8, 10)), (65, 400))
        screen_end.blit(mes_pressEsc.render('Чтобы выйти из игры, нажмите Q', 1, (0, 0, 0)), (150, 500))

        window.blit(status_bar_end, (0, 0))
        window.blit(screen_end, (0, 45))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                is_game_running = False
                break
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    is_game_running = False
                    break

        if is_game_running is False:
            break

        pygame.display.flip()

    '''Игра выиграна'''
    while congratulations():
        pygame.mixer.pause()
        screen_end = pygame.image.load('image/screen_end.png')
        status_bar_end = pygame.image.load('image/status_bar_end.png')
        screen_end.blit(mes_congratulations.render('CONGRATULATIONS', 0, (41, 162, 78)), (30, 300))
        screen_end.blit(mess_send_down.render('Вы исключили всех учеников!', 0, (41, 162, 78)), (120, 380))
        screen_end.blit(mes_pressEsc.render('Чтобы выйти из игры, нажмите Q', 1, (0, 0, 0)), (150, 500))

        window.blit(status_bar_end, (0, 0))
        window.blit(screen_end, (0, 45))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                is_game_running = False
                break
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    is_game_running = False
                    break

        if is_game_running is False:
            break
        pygame.display.flip()
