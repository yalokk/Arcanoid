import pygame

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((255, 255, 255))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

'''Кирпичи'''     
class Brick:
    def __init__(self, xpos, ypos, filename, score):
        self.x = xpos
        self.y = ypos
        self.len = 70
        self.height = 70
        self.bitmap = pygame.image.load(filename)
        self.score = score
        
emil = Brick(0, 0, 'image/emil', 10)
kolya = Brick(245, 70, 'image/kolya', 9)
zahar = Brick(315, 70, 'image/zahar', 8)
#sergo 
#liza
#nadya
#lesha
#gleb
#margo

       
    
'''Пересечение 2х объектов'''
def Intersect(x1, x2, y1, y2, len1, len2, height1, height2):
    if (x1 > x2 - len1) and (x1 < x2 + len2) and (y1 > y2 - height1) and (y1 < y2 + height2):
        return 1
    else:
        return 0

'''окно'''
window = pygame.display.set_mode((600, 700))
pygame.display.set_caption('Оля, смари')
'''холст'''
screen = pygame.Surface((600, 700))
# Создать строку состояния

x = 0
y = 0

'''Описание Соболевой (мяч)'''
Soboleva = Sprite(0, 0, 'image/soboleva.png')  # поправить стартовые координаты Соболевой
Soboleva.go_right = True
Soboleva.go_down = True
'''Описание ракетки'''
racket = Sprite(40, 685, 'image/racket.png')

'''ИГРОВОЙ ЦИКЛ'''
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

    '''заливка экрана''' 
    screen = pygame.image.load('image/screen.png')

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

    if Intersect(racket.x, Soboleva.x, racket.y, Soboleva.y, 60, 45, 20, 45) == True:
        Soboleva.go_down = False

    '''отрисовка объектов'''
    racket.render()  # выводим ракетку в нужные координаты
    Soboleva.render()  # выводим Соболеву в нужные координаты
    window.blit(screen, (0, 0))
    pygame.display.flip()
    # pygame.time.delay(ЗНАЧ.СКОРОСТИ)  CКОРОСТЬ ГОЛОВЫ
