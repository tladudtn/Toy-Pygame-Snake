import pygame
import random
import time

# 글자 표시
pygame.init()

# 해상도 지정
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_height,screen_width))

# 색깔
red   = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255, 255, 255)
# 타이틀
pygame.display.set_caption('PY - SNAKE by PYGAME')


snake_speed = 15
snake_size = 10

clock = pygame.time.Clock()

# 택스트 출력 - 0
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
# 택스트 출력 - 1
def message_display(text):
    x_msg = 10
    y_msg = 10

    largeText = pygame.font.Font('./font/D2Coding-Ver1.3-20171129.ttf',22)
    TextSurf, TextRect = text_objects(text, largeText)
    screen.blit(TextSurf, (x_msg,y_msg))

    pygame.display.update()

# 뱀 길이 늘리는 함수
def snakelong(snake_size, snake_list):
    for x1 in snake_list:
        pygame.draw.rect(screen ,green, [x1[0], x1[1], snake_size, snake_size])

# 게임 작동 중 돌아가는 것
def snakeWorking():

    game_over=False
    
    x = screen_width/2
    y = screen_width/2

    x_update = 0
    y_update = 0

    # 음식 생성되는 범위
    x_food = round(random.randrange(0, screen_width - snake_size)  / 10.0) * 10.0
    y_food = round(random.randrange(0, screen_height - snake_size)  / 10.0) * 10.0

    # 뱀 길이 관련
    snake_list = []
    snake_length = 1


    # (while문 동작시 종료되지 않음)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           
                game_over = True
            #print(event) 
            
            # 키를 누를때 뱀 이동
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_update = 0
                    y_update = -snake_size
                elif event.key == pygame.K_DOWN:
                    x_update = 0
                    y_update = snake_size
                elif event.key == pygame.K_LEFT:
                    x_update = -snake_size
                    y_update = 0
                elif event.key == pygame.K_RIGHT:
                    x_update = snake_size
                    y_update = 0
                
        # 게임 오버 조건
        if x <= 0 or x >= screen_width or y <= 0 or y >= screen_height : 
            game_over=True


        x += x_update
        y += y_update
        screen.fill(black)

        # 랜더링
        #pygame.draw.rect(screen ,green, [x, y, snake_size, snake_size])
        pygame.draw.rect(screen, red, [x_food, y_food, snake_size, snake_size])

        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
 
        for x1 in snake_list[:-1]:
            if x1 == snake_head:
                game_over = True

        snakelong(snake_size, snake_list)

        message_display('Score:{0}'.format(snake_length-1)) 
        # 화면 업데이트
        pygame.display.update()


        if x == x_food and y == y_food:
            # 음식 생성되는 범위
            x_food = round(random.randrange(0, screen_width - snake_size)  / 10.0) * 10.0
            y_food = round(random.randrange(0, screen_height - snake_size)  / 10.0) * 10.0
            snake_length += 1 
              


        # 속도 조정
        clock.tick(snake_speed)        


    pygame.quit()
    quit()


snakeWorking()