import pygame
from settings import *
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.SysFont('arial', 36)
f1 = pygame.font.Font(None, 30)
f2 = pygame.font.Font(None, 50)

clock = pygame.time.Clock()
sound_pong = pygame.mixer.Sound('oh.wav')
pygame.mixer.Sound.set_volume(sound_pong, 0.2)
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

pause_flag = False
ball_speed_horizontal_tmp = 0
ball_speed_vertical_tmp = 0
print(left_score, right_score, sep=" | ")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        if not pause_flag:
            ball_speed_horizontal_tmp = ball_speed_horizontal
            ball_speed_vertical_tmp = ball_speed_vertical
            ball_speed_vertical = 0
            ball_speed_horizontal = 0
            text1 = f2.render("PAUSED", 1, (255, 255, 255))
            sc.blit(text1, (WIDTH // 2 - 70, HEIGHT // 2))
        pause_flag = not pause_flag 
        if not pause_flag:
            ball_speed_vertical = ball_speed_vertical_tmp
            ball_speed_horizontal = ball_speed_horizontal_tmp   
        pygame.time.wait(150)
    
    if not pause_flag:
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

        if keys[pygame.K_e]:
            if ball_speed_vertical > 0:
                ball_speed_vertical += 1
            else:
                ball_speed_vertical -= 1
            if ball_speed_horizontal > 0:
                ball_speed_horizontal += 1
            else:
                ball_speed_horizontal -= 1
            print(ball_speed_horizontal, ball_speed_vertical)

        if keys[pygame.K_q]:
            if ball_speed_vertical > 0:
                if ball_speed_vertical - 1 > 0:
                    ball_speed_vertical -= 1
            elif ball_speed_vertical + 1 < 0:
                ball_speed_vertical += 1
            if ball_speed_horizontal > 0:
                if ball_speed_horizontal - 1 > 0:
                    ball_speed_horizontal -= 1
            elif ball_speed_horizontal + 1 < 0:
                ball_speed_horizontal += 1

            print(ball_speed_horizontal, ball_speed_vertical)

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
            # ball_speed_vertical *= -1

        if (ball_x + ball_speed_horizontal + ball_radius >= WIDTH - 50) and (ball_y >= y2) and (ball_y <= y2 + 100):  # right player
            ball_speed_horizontal *= -1
            # ball_speed_vertical *= -1

        if ball_x + ball_speed_horizontal - ball_radius <= 50 - 5:   # left player
            if left_flag:
                sound_pong.stop()
                sound_pong.play()
                right_score += 1
                print(left_score, right_score, sep=" | ")
                left_flag = False

        if ball_x + ball_speed_horizontal + ball_radius >= WIDTH - 50 + 5:  # right player
            if right_flag:
                sound_pong.stop()
                sound_pong.play()
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