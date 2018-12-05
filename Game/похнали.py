import pygame
import sys

# from logic import Intersect, Sprite, Brick, Sergo, ezk_go, nl_go


'''Класс объектов игры'''


class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((255, 255, 255))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))


'''Кирпичи'''


class Brick(Sprite):
    def __init__(self, xpos, ypos, filename, score):
        self.x = xpos
        self.y = ypos
        self.len = 70
        self.height = 70
        self.bitmap = pygame.image.load(filename)
        self.score = score

    def Intersect_with_Sob(self, sob_x, sob_y):
        if Intersect(self.x, sob_x, self.y, sob_y, 70, 45, 70, 45):
            Soboleva.go_down = not Soboleva.go_down
            # Soboleva.go_right = not Soboleva.go_right
            bricks.remove(i)


'''Класс для Сереги'''


class Sergo(Brick):
    def Intersect_with_Sob(self, sob_x, sob_y):
        if Intersect(self.x, sob_x, self.y, sob_y, 70, 45, 70, 45):
            Soboleva.go_down = not Soboleva.go_down
            # Soboleva.go_right = not Soboleva.go_right


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
        if name.y > 450:
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

sergo = Sergo(560, 140, 'image/sergo.png', 0)
sergo2 = Sergo(0, 140, 'image/sergo.png', 0)

liza = Brick(0, 210, 'image/liza.png', 6)
liza.go_down = True
nadya = Brick(560, 210, 'image/nadya.png', 6)
nadya.go_down = True
liza2 = Brick(70, 420, 'image/liza.png', 6)
liza2.go_down = False
nadya2 = Brick(490, 420, 'image/nadya.png', 6)
nadya2.go_down = False

lesha = Brick(280, 140, 'image/lesha.png', 4)
lesha2 = Brick(210, 210, 'image/lesha.png', 4)
lesha3 = Brick(350, 210, 'image/lesha.png', 4)
lesha4 = Brick(280, 280, 'image/lesha.png', 4)

gleb = Brick(140, 140, 'image/gleb.png', 4)
gleb2 = Brick(420, 140, 'image/gleb.png', 4)
gleb3 = Brick(210, 280, 'image/gleb.png', 4)

margo = Brick(210, 140, 'image/margo.png', 2)
margo2 = Brick(350, 140, 'image/margo.png', 2)
margo3 = Brick(140, 280, 'image/margo.png', 2)
margo4 = Brick(420, 280, 'image/margo.png', 2)

andrey = Brick(70, 140, 'image/andrey.png', 4)
andrey2 = Brick(490, 140, 'image/andrey.png', 4)
andrey3 = Brick(280, 350, 'image/andrey.png', 4)

# andrey
# lesha
# gleb
# margo

bricks = [sergo, sergo2, emil, kolya, kolya2, zahar, zahar2, liza, nadya, liza2, nadya2, lesha, lesha2, lesha3, lesha4,
          gleb, gleb2, gleb3, margo, margo2, margo3, margo4, andrey, andrey2, andrey3]

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

'''шрифты'''
pygame.font.init()
health_font = pygame.font.Font('font/foo.otf', 37)
score_font = pygame.font.Font('font/foo.otf', 37)

'''Описание Соболевой (мяч)'''
Soboleva = Sprite(360, 600, 'image/soboleva.png')  # поправить стартовые координаты Соболевой
Soboleva.go_right = True
Soboleva.go_down = True
stepX_sob = 2
stepY_sob = 5
'''Описание ракетки'''
racket = Sprite(340, 640, 'image/racket.png')
step_rac = 9

'''ИГРОВОЙ ЦИКЛ'''
done = True
pygame.key.set_repeat(1, 1)
pygame.time.delay(1)
while done:
    '''обработчик событий'''
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        '''перемещение ракетки с помощью клавиш'''
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                if racket.x > 0:
                    racket.x -= step_rac
            if e.key == pygame.K_RIGHT:
                if racket.x < 570:
                    racket.x += step_rac

    '''заливка экрана'''
    screen = pygame.image.load('image/screen.png')
    '''цвет таблички с жизнями'''
    status_bar.fill((255, 255, 255))

    '''передвижение Соболевой'''
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
    for i in bricks[:2]:
        i.Intersect_with_Sob(Soboleva.x, Soboleva.y)
        if Intersect(i.x, Soboleva.x, i.y, Soboleva.y, 70, 45, 70, 45):
            stepX_sob += 0.5
            stepY_sob += 1.5

    for i in bricks[2:]:
        i.Intersect_with_Sob(Soboleva.x, Soboleva.y)
        if Intersect(i.x, Soboleva.x, i.y, Soboleva.y, 70, 45, 70, 45):
            total_score += i.score

    '''Минус очки в случае удара о пол'''
    if Soboleva.y >= 615:
        health -= 1

    '''отрисовка объектов'''
    for i in bricks:
        i.render()
    racket.render()
    Soboleva.render()
    '''отрисовка шрифта'''
    status_bar.blit(health_font.render('Щечки: ' + str(health), 1, (168, 203, 209)), (10, 10))
    status_bar.blit(score_font.render('Score: ' + str(total_score), 1, (168, 203, 209)), (475, 10))
    window.blit(status_bar, (0, 0))
    '''отрисовка холста'''
    window.blit(screen, (0, 45))
    pygame.display.flip()
    # pygame.time.delay(ЗНАЧ.СКОРОСТИ)  CКОРОСТЬ ГОЛОВЫ
