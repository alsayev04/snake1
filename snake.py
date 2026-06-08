import pygame
import time
import random

<<<<<<< HEAD
#Инициали pygame
pygame.init()
=======
# Инициализация pygame
pygame.init()
>>>>>>> 6a4afc9dcf5e3445baf51cc525bc30ec2d3a02dd

<<<<<<< HEAD
#Цвета (RGB)
white = (255,255,255)
black = (0,0,0)
red = (213,50,80)
green = (0,255,0)
blue = (50,153,213)

# Размеры экрана
dis_width = 800
dis_height = 600

#Создание окна игры
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка на Python')

#Часы для контроля FPS
clock = pygame.time.clock()

#Параметры змейки
snake_block = 20
snake_speed = 15

#Шрифты
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 35)

def your_score(score):
    """Отоброжение счета на экране"""
    value = score_font.render("Счет: " + str(score), True, black)
    dis_blit(value, [10, 10])

def our_snake(snake_block, snake_list):
    """Отрисовка змейки"""
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0],x[1], snake_block, snake_block])

def message(msg, color):
    """Вывод сообщений на экран"""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height/ 3])

def gameLoop():
    """Главный игровой цикл"""
    game_over = False

    #Начальные координаты змейки
    x1 = dis_width / 2
    y1 = dis_height / 2

    #Изменения координат
    x1_change = 0
    y1_change = 0

    #Тело змейки (список координат)
    snake_list = []
    Length_of_snake = 1

    #Координаты еды
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foodx = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    while not game_over:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.Quit:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    x1_change = snake_block
                    y1_change = 0
    
    #Проверка столкновения со стеной
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True


=======