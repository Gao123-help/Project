import pygame
import time
from pygame.locals import *

hero_x = 260
hero_y = 520
bulletes = []

enemy_x = 230
enemy_y = 20
enemy_path = "right"

a = pygame.image.load("./feiji/enemy2_down1.png")
b = pygame.image.load("./feiji/enemy2_down2.png")
c = pygame.image.load("./feiji/enemy2_down3.png")
d = pygame.image.load("./feiji/enemy2_down4.png")
e = pygame.image.load("./feiji/enemy2_down5.png")
f = pygame.image.load("./feiji/enemy2_down6.png")

enemy_down = [a, b, c, d, e, f]
enemy_status = "alive"
enemy_count = 0


def heroevent(screen, hero, bullete):
    global hero_x
    global hero_y
    screen.blit(hero, (hero_x, hero_y))
    # 通过捕获键盘事件控制飞机上下左右移动
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                hero_y -= 10
            elif event.key == K_DOWN:
                hero_y += 10
            elif event.key == K_LEFT:
                hero_x -= 10
            elif event.key == K_RIGHT:
                hero_x += 10
            elif event.key == K_SPACE:
                bulletes.append({'x': hero_x + 33, 'y': hero_y - 32})
    for i in bulletes:
        screen.blit(bullete, (i['x'], i['y']))
        i['y'] -= 10


def enemyevent(screen, enemy):
    global enemy_x
    global enemy_y
    global enemy_path
    global enemy_status
    global enemy_count
    for i in bulletes:
        if i["x"] >= enemy_x and i["x"] <= enemy_x + enemy.get_width() and i["y"] >= 0 and \
                i["y"] <= enemy.get_height():
            enemy_status = "died"
            del i
            break

    if enemy_status == "alive":
        screen.blit(enemy, (enemy_x, enemy_y))
        enemy_count = 0
        if enemy_x + 260 >= 700:
            enemy_path = "left"
        if enemy_x <= 0:
            enemy_path = "right"
        if enemy_path == "right":
            enemy_x += 5
        elif enemy_path == "left":
            enemy_x -= 5
    elif enemy_status == "died":
        if enemy_count <= 5:
            screen.blit(enemy_down[enemy_count], (enemy_x, enemy_y))
            enemy_count += 1

    enemy_status = "alive"


def main():
    # 创建窗口
    screen = pygame.display.set_mode((600, 700), 0, 32)
    background = pygame.image.load("./feiji/744847.png")
    # 将飞机放在屏幕里
    hero = pygame.image.load("./feiji/hero.gif")
    # 加载子弹图片
    bullete = pygame.image.load("./feiji/plane.png")
    # 敌方飞机
    enemy = pygame.image.load("./feiji/enemy2.png")
    while True:
        screen.blit(background, (0, 0))
        heroevent(screen, hero, bullete)
        enemyevent(screen, enemy)
        pygame.display.update()
        time.sleep(0.05)


if __name__ == "__main__":
    main()
