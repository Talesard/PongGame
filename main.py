import pygame
from settings import *
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.SysFont('arial', 36)
f1 = pygame.font.Font(None, 30)

clock = pygame.time.Clock()

player_speed = 10
ball_speed_horizontal = 7
ball_speed_vertical = 7
ball_radius = 15
y1 = 0
y2 = 0
left_flag = True
right_flag = True
left_score = 0
right_score = 0

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

print(left_score, right_score, sep=" | ")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if y1 - player_speed >= 0:
            y1 -= player_speed

    if keys[pygame.K_s]:
        if y1 + player_speed <= HEIGHT - 100:
            y1 += player_speed

    if keys[pygame.K_UP]:
        if y2 - player_speed >= 0:
            y2 -= player_speed

    if keys[pygame.K_DOWN]:
        if y2 + player_speed <= HEIGHT - 100:
            y2 += player_speed

    if keys[pygame.K_r]:  # reset
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2

    if ball_x + ball_speed_horizontal + ball_radius >= WIDTH:   # down side
        ball_speed_horizontal *= -1

    if ball_y + ball_speed_vertical + ball_radius >= HEIGHT:    # right side
        ball_speed_vertical *= -1

    if ball_x + ball_speed_horizontal - ball_radius <= 0:       # left side
        ball_speed_horizontal *= -1

    if ball_y + ball_speed_vertical - ball_radius <= 0:         # up side
        ball_speed_vertical *= -1

    if (ball_x + ball_speed_horizontal - ball_radius <= 50) and (ball_y >= y1) and (ball_y <= y1 + 100):   # left player
        ball_speed_horizontal *= -1
        ball_speed_vertical *= -1

    if (ball_x + ball_speed_horizontal + ball_radius >= WIDTH - 50) and (ball_y >= y2) and (ball_y <= y2 + 100):  # right player
        ball_speed_horizontal *= -1
        ball_speed_vertical *= -1

    if ball_x + ball_speed_horizontal - ball_radius <= 50 - 5:   # left player
        if left_flag:
            right_score += 1
            print(left_score, right_score, sep=" | ")
            left_flag = False

    if ball_x + ball_speed_horizontal + ball_radius >= WIDTH - 50 + 5:  # right player
        if right_flag:
            left_score += 1
            print(left_score, right_score, sep=" | ")
            right_flag = False

    if ball_x >= 100:
        left_flag = True

    if ball_x <= WIDTH - 100:
        right_flag = True

    ball_x += ball_speed_horizontal
    ball_y += ball_speed_vertical

    sc.fill(BLACK)

    text1 = f1.render(str(left_score), 1, (255, 255, 255))
    sc.blit(text1, (WIDTH // 2 - 50, 10))
    text1 = f1.render(str(right_score), 1, (255, 255, 255))
    sc.blit(text1, (WIDTH // 2 + 50, 10))

    pygame.draw.rect(sc, WHITE, (0, y1, 50, 100))
    pygame.draw.rect(sc, WHITE, (WIDTH - 50, y2, WIDTH, 100))
    pygame.draw.line(sc, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)
    pygame.draw.circle(sc, WHITE, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(FPS)