import pygame
import time


def main():
    # 创建窗口
    screen = pygame.display.set_mode((600, 700), 0, 32)
    background = pygame.image.load("./feiji/744847.png")
    screen.blit(background, (0, 0))
    pygame.display.update()
    time.sleep(10)


if __name__ == "__main__":
    main()
