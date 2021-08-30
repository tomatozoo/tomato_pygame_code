import random
import sys
import math
import pygame
from pygame import mixer
import time
from time import sleep

 

# 게임 화면 크기
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
base = pygame.image.load("base.png")
icon = pygame.image.load('love.png')
pipe_image=pygame.image.load("cloud.png")
pipe_image = pygame.transform.scale(pipe_image, (70, 70))

flip_pipe=pygame.transform.flip(pipe_image,False,True)


pygame.display.set_icon(icon)


# 색상
WHITE = (255,255,255)

 

# 속도와 질량 기본 값
VELOCITY = 7
MASS = 2
 

class Car:

 

    def __init__(self):
        self.image = ""
        self.dx = 0
        self.dy = 0
        self.rect = ""
        self.isJump = 0
        self.v = VELOCITY # 속도
        self.m = MASS  # 질량

 

    def load_car(self):
        # 플레이어 차량
        self.image = pygame.image.load("sj.png")
        # 크기 조정
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.centerx = round(WINDOW_WIDTH / 2)
        self.rect.bottom = WINDOW_HEIGHT

 

    # 자동차를 스크린에 그리기
    def draw_car(self):
        SCREEN.blit(self.image, [self.rect.x, self.rect.y])

 

    # x 좌표 이동 - 플레이어 자동차의 움직임 제어할 때 필요
    def move_x(self):
        self.rect.x += self.dx

 

    # 화면 밖으로 못 나가게 방지
    def check_screen(self):
        if self.rect.bottom > WINDOW_HEIGHT or self.rect.y < 0:
            self.rect.y -= self.dy

    #점프 상태를 체크
    def jump(self, j):
        self.isJump = j

    def update(self):
        if self.isJump > 0:
            if self.isJump == 2:
                self.v = VELOCITY
            if self.v > 0:
                F = (0.5*self.m*(self.v*self.v))
            else:
                F = -(0.5*self.m*(self.v*self.v))
            self.rect.y -=round(F)
            self.v -= 1

            if self.rect.bottom > WINDOW_HEIGHT:
                self.rect.bottom = WINDOW_HEIGHT
                self.isJump = 0
                self.v = VELOCITY

    def birthday(self):
        if self.rect.x > WINDOW_WIDTH:
            SCREEN.fill((0,0,0))
            image = pygame.image.load("happy.png")
            SCREEN.blit(image, (self.rect.x-WINDOW_WIDTH, self.rect.bottom-70))

            if self.rect.x > WINDOW_WIDTH + 100:
                question = font.render("?", True, (255,255,255))
                SCREEN.blit(question, (self.rect.x-WINDOW_WIDTH, 150))
            

                if self.rect.x > 2 * WINDOW_WIDTH:
                    
                
                    song = ["happy", "birthday", "to", "you~", "happy birthday", "to you~"]
                    for i in range(len(song)): 
                        if self.rect.x > 2*WINDOW_WIDTH + i * 80:
                            score = font.render(song[i], True, (255, 0, 255))
                            SCREEN.fill((0,0,0))
                            SCREEN.blit(score, (self.rect.x-2*WINDOW_WIDTH, i*50))
                    snail = pygame.image.load("snail.png")
                    SCREEN.blit(image, (self.rect.x-2*WINDOW_WIDTH, self.rect.bottom-70))
                    SCREEN.blit(snail, (3*WINDOW_WIDTH - self.rect.x,self.rect.bottom - 70))
                    if 5*WINDOW_WIDTH - 20 < 2*self.rect.x < 5*WINDOW_WIDTH + 20:
                        love = pygame.image.load("love.png")
                        love = pygame.transform.scale(love, (70, 70))

                        SCREEN.blit(love, (self.rect.x-2*WINDOW_WIDTH, 300))

                 
           

def main():
    global SCREEN, WINDOW_WIDTH, WINDOW_HEIGHT



    p1x=random.randint(0,700)
    p1y=random.randint(0,500)

    p2x=random.randint(0,700)
    p2y=random.randint(0,500)

    p3x=random.randint(0,700)
    p3y=random.randint(0,500)


    # pygame 초기화 및 스크린 생성
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("happytomato")



    clock = pygame.time.Clock()

 

    # 플레이어 자동차 생성
    player = Car()
    player.load_car()

 

    playing = True

    while playing:
        



        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()

 

            # 화살표 키를 이용해서 플레이어의 움직임 거리를 조정해준다.
            # 키를 떼면 움직임 거리를 0으로 한다.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.dx = 5
                elif event.key == pygame.K_LEFT:
                    player.dx = -5

                if event.key == pygame.K_SPACE:
                    if player.isJump == 0:
                        player.jump(1)

 

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
                elif event.key == pygame.K_LEFT:
                    player.dx = 0


        # 배경색을 흰색으로
        SCREEN.fill(WHITE)
        player.draw_car()
        player.move_x()
        player.update()
        player.check_screen()
        player.birthday()
        score = font.render("Go right", True, (0, 0, 0))

        SCREEN.blit(score, (100, 120)) 
        SCREEN.blit(pipe_image, (p1x, p1y))
        SCREEN.blit(pipe_image, (p2x, p2y))
        SCREEN.blit(pipe_image, (p3x, p3y))
        pc=-0.3
        p1x+=pc
        p2x+=pc #파이프가 왼쪽으로 이동한다.
        p3x+= pc

        if p1x<=-40:
            p1x=700
            p1y=random.randint(0,600)

        if p2x<=-40:
             p2x=700
             p2y=random.randint(0,600)
        if p3x<=-40:
             p3x=700
             p3y=random.randint(0,600)


        pygame.display.flip()

        

        # 초당 프레임 설정
        clock.tick(60)


if __name__ == '__main__':
    main()