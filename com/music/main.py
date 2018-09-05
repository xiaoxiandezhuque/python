import pygame, sys
import time


def play():
    filename = r"C:\Users\xuhong\Desktop\gem.mp3"
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode([480, 320])  # 注意这一句
    pygame.time.delay(1000)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(120)
    # exit("播放结束")

    #     for event in pygame.event.get():
    #         print(event.type)
    #         if event.type == pygame.QUIT:
    #             sys.exit()


if __name__ == "__main__":
    play()
