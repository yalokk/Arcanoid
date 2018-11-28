import pygame


class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((255, 255, 255))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))


def Intersect(x1, x2, y1, y2):
    if (x1 > x2 - 60) and (x1 < x2 + 45) and (y1 > y2 - 20) and (y1 < y2 + 45):
        return 1
    else:
        return 0


window = pygame.display.set_mode((600, 700))
pygame.display.set_caption('Оля, смари')
screen = pygame.Surface((600, 700))

x = 0
y = 0

'''Описание Соболевой (мяч)'''
Soboleva = Sprite(0, 0, 'soboleva.png')  # поправить стартовые координаты Соболевой
Soboleva.go_right = True
Soboleva.go_down = True
'''Описание ракетки'''
racket = Sprite(40, 685, 'racket.png')

down = True
pygame.key.set_repeat(1, 1)
while down:
    '''обработчик событий'''
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        '''перемещение ракетки с помощью клавиш'''
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                if racket.x > 0:
                    racket.x -= 2
            if e.key == pygame.K_RIGHT:
                if racket.x < 540:
                    racket.x += 2

    '''заливка экрана''' # поменять на картинку
    screen.fill((70, 200, 40))  # цвет фона

    '''передвижение Соболевой''' # корект движение (отскакивание от пола)
    if Soboleva.go_right == True:
        Soboleva.x += 0.7
        if Soboleva.x > 555:
            Soboleva.go_right = False
    else:
        Soboleva.x -= 0.7
        if Soboleva.x <= 0:
            Soboleva.go_right = True

    if Soboleva.go_down == True:
        Soboleva.y += 0.7
        if Soboleva.y > 655:
            Soboleva.go_down = False
    else:
        Soboleva.y -= 0.7
        if Soboleva.y <= 0:
            Soboleva.go_down = True

    if Intersect(racket.x, Soboleva.x, racket.y, Soboleva.y) == True:
        Soboleva.go_down = False

    '''отрисовка объектов'''
    racket.render()  # выводим ракетку в нужные координаты
    Soboleva.render()  # выводим Соболеву в нужные координаты
    window.blit(screen, (0, 0))
    pygame.display.flip()
    # pygame.time.delay(ЗНАЧ.СКОРОСТИ)  CКОРОСТЬ ГОЛОВЫ
