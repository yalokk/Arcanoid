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
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))
        
        
    '''Передвижение Эмиля, Захара и Коли'''
def ezk_go(name, step):
    if name.go_right == True:
        name.x += step
        if name.x > 560:
            name.go_right = False
    else:
        name.x -= step
        if name.x <= 0:
            name.go_right = True

        
emil = Brick(0, 0, 'image/emil.png', 10)
emil.go_right = True
kolya = Brick(0, 70, 'image/kolya.png', 8)
kolya.go_right = True
zahar = Brick(560, 70, 'image/zahar.png', 8)
zahar.go_right = True
bricks = [emil, kolya, zahar]
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
    
    
'''Подсчет очков'''
score = 5

'''окно'''
window = pygame.display.set_mode((630, 745))
pygame.display.set_caption('Оля, смари')
'''холст'''
screen = pygame.Surface((630, 700))
'''строка состояния'''
status_bar = pygame.Surface((630, 45))
x = 0
y = 0

'''шрифты'''
pygame.font.init()
score_font = pygame.font.Font('font/foo.otf', 37)

'''Описание Соболевой (мяч)'''
Soboleva = Sprite(0, 0, 'image/soboleva.png')  # поправить стартовые координаты Соболевой
Soboleva.go_right = True
Soboleva.go_down = True
step_sob = 5
'''Описание ракетки'''
racket = Sprite(40, 685, 'image/racket.png')
step_rac = 9

'''ИГРОВОЙ ЦИКЛ'''
done = True
pygame.key.set_repeat(1, 1)
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
    if Soboleva.go_right == True:
        Soboleva.x += step_sob
        if Soboleva.x > 585:
            Soboleva.go_right = False
    else:
        Soboleva.x -= step_sob
        if Soboleva.x <= 0:
            Soboleva.go_right = True

    if Soboleva.go_down == True:
        Soboleva.y += step_sob
        if Soboleva.y > 655:
            Soboleva.go_down = False
    else:
        Soboleva.y -= step_sob
        if Soboleva.y <= 0:
            Soboleva.go_down = True
            
    '''Передвижение Эмиля, Захара и Коли'''
    ezk_go(emil, 11)
    ezk_go(zahar, 9)
    ezk_go(kolya, 9)

    '''Проверка сталкивания Соболевой и ракетки'''
    if Intersect(racket.x, Soboleva.x, racket.y, Soboleva.y, 60, 45, 20, 45) == True:
        Soboleva.go_down = False
        
    '''Минус очки в случае удара НЕ о ракетку'''
    if Soboleva.y == 655:
        score -= 1

    '''отрисовка объектов'''
    for i in bricks:
        i.render()
    racket.render()  
    Soboleva.render()  
    '''отрисовка шрифта'''
    status_bar.blit(score_font.render('Щечки: ' +str(score), 1, (168, 203, 209)), (10, 10))
    window.blit(status_bar, (0, 0))
    '''отрисовка холста'''
    window.blit(screen, (0, 45))
    pygame.display.flip()
    # pygame.time.delay(ЗНАЧ.СКОРОСТИ)  CКОРОСТЬ ГОЛОВЫ
