#-*- coding: utf-8 -*-#

import random
import sys
import math
import pygame
from pygame import mixer
import time
from time import sleep
from math import pi

 

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

#한글 폰트 불러오기
pygame.font.init()
font = pygame.font.SysFont('malgungothic', 20)

#토마토 불러오기
redtomato = pygame.image.load('tomatotomato.png')
happytomato = pygame.image.load('redtomato.png')
sadtomato = pygame.image.load('sadtomato.png')
mansaytomato = pygame.image.load('tomato.png')

# 배경 불러오기
basicbackground = pygame.image.load('basicbackground.png')
basicbackground = pygame.transform.scale(basicbackground, (800, 500))
studying = pygame.image.load('studying.png')
studying = pygame.transform.scale(studying, (800, 500))
wheretogo = pygame.image.load('wheretogo.png')
wheretogo = pygame.transform.scale(wheretogo, (800, 500))
worldview = pygame.image.load('worldview.png')
worldview = pygame.transform.scale(worldview, (800, 500))
pop = pygame.image.load('pop.png')
pop = pygame.transform.scale(pop, (800, 500))
pop1 = pygame.image.load('pop1.png')
pop1 = pygame.transform.scale(pop1, (800, 500))
pop2 = pygame.image.load('pop2.png')
pop2 = pygame.transform.scale(pop2, (800, 500))
pop3 = pygame.image.load('pop3.png')
pop3 = pygame.transform.scale(pop3, (800, 500))
pop4 = pygame.image.load('pop4.png')
pop4 = pygame.transform.scale(pop4, (800, 500))

#아이콘 불러오기
icon = pygame.image.load('tomato.png')
pygame.display.set_icon(icon)

 
VELOCITY = 7
MASS = 2
 

class Car:

 

    def __init__(self):
        self.image = ""
        self.subimage = ""
        self.dx = 0
        self.dy = 0
        self.rect = ""
        self.isJump = 0
        self.v = VELOCITY # ?ӵ?
        self.m = MASS  # ????
        self.map_num = 0
        self.tomato = 0
        self.one = 0
        self.two = 0
        self.three = 0
        self.four = 0
        self.space = 0
        self.theta = 0.001

 

    def load_car(self):
        # ?÷??̾? ????
        self.image = pygame.image.load("tomato.png")
        # ũ?? ????
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = round(WINDOW_WIDTH / 2)
        self.rect.bottom = WINDOW_HEIGHT - 57

 

    # ?ڵ????? ??ũ???? ?׸???
    def draw_car(self):
        SCREEN.blit(self.image, [self.rect.x, self.rect.y])

 

    # x ??ǥ ?̵? - ?÷??̾? ?ڵ????? ?????? ?????? ?? ?ʿ?
    def move_x(self):
        self.rect.x += self.dx

 

    # ȭ?? ?????? ?? ?????? ????
    def check_screen(self):
        if self.rect.bottom > WINDOW_HEIGHT or self.rect.y < 0:
            self.rect.y -= self.dy

    #???? ???¸? üũ
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

            if self.rect.bottom > WINDOW_HEIGHT - 57:
                self.rect.bottom = WINDOW_HEIGHT - 57
                self.isJump = 0
                self.v = VELOCITY

    def map(self):
        # x값에 반응하는 곳
        #basic
        if self.map_num == 0:
            SCREEN.blit(basicbackground, (0,0))
            if self.rect.x == 800:
                self.rect.x = 0
                self.space  = 0
                self.map_num += 1
            elif self.rect.x < 0:
                self.rect.x = 0
                self.space = 0
        #worldview
        elif self.map_num == 1:
            SCREEN.blit(worldview, (0,0))
            if self.rect.x == 800:
                self.rect.x = 0
                self.space = 0
                self.map_num += 1
            elif self.rect.x < 0:
                self.map_num -= 1
                self.rect.x += 800
                self.space = 0
        #최상위 + 최상위
        elif self.map_num == 2:
            SCREEN.blit(wheretogo, (0,0))
            if self.rect.x == 800:
                self.rect.x = 0
                self.space = 0
                self.map_num += 1
            elif self.rect.x < 0:
                self.map_num -= 1
                self.rect.x += 800
                self.space = 0
        #뽑기
        elif self.map_num == 3:
            SCREEN.blit(pop, (0,0))
            if self.rect.x == 800:
                self.rect.x = 0
                self.space = 0
                self.map_num += 1
            elif self.rect.x < 0:
                self.map_num -= 1
                self.rect.x += 800
                self.space = 0
            
        #studying - 열공 중
        elif self.map_num == 4:
            SCREEN.blit(studying, (0,0))
            if self.rect.x >= 700:
                self.rect.x = 0
                self.space = 0
                self.map_num += 1
            elif self.rect.x < 0:
                self.map_num -= 1
                self.rect.x += 800   
                self.space = 0
                self.one = 0
                self.two = 0
                self.three = 0
                self.four = 0
        elif self.map_num == 5:
            SCREEN.fill((255,255,255))
            if self.rect.x >= 700:
                self.rect.x = 700
                self.space = 0
            elif self.rect.x < 0:
                self.map_num -= 1

    def conversation(self):
        # space에 반응하는 곳
        if self.map_num == 0:
            if self.space == 0:
                score = font.render("space바를 눌러주세요", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x -30, 200))
            if self.space == 1:
                score = font.render("안녕?", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x +30, 200))
                score = font.render("반가워", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x +30, 240))
            elif self.space == 3:
                score = font.render("나는 토마토야", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x-30 , 200))
                score = font.render("수학나라에 온 것을 환영해!", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x -30, 240))
            elif self.space == 5:
                score = font.render("오늘부터 여기서 수학을 공부해볼거야!", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x-60 , 200))
                score = font.render("어때?", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x , 240))

            elif self.space == 7:
                score = font.render("그럼 시작해보자!", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x-20 , 200))

            elif self.space == 9:
                SCREEN.fill((0,0,0))

            elif self.space == 11:
                score = font.render("우선 키보드 조작법을 알려줄게", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x-60 , 150))
            elif self.space == 13:
                score = font.render("키보드 방향키를 누르면", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x-60 , 200))
                score = font.render("오른쪽, 왼쪽으로 이동할 수 있어", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x-70 , 240))
            elif self.space == 15:
                score = font.render("잘했어!", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x , 150))
            elif self.space == 17:
                score = font.render("이번엔, 키보드 t를 눌러볼래?", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x-60 , 150))
            elif self.space == 19:
                score = font.render("좋았어!", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x , 150))
            elif self.space == 21:
                score = font.render("이렇게 tomatoworld를 돌아다니면서,", True, (255,0,255))
                SCREEN.blit(score, (self.rect.x -40, 150))
                score = font.render("수학 공부를 할거야 :)", True, (255,0,255))
                SCREEN.blit(score, (self.rect.x -40, 200))
            elif self.space == 23:
                score = font.render("그럼 다음 장소로 이동해보자!", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x -40, 150))

            
        #worldview
        elif self.map_num == 1:
            if self.space == 3:
                score = font.render("우와~", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x+10, 300))       
                
        #최상위 + 최상위
        elif self.map_num == 2:
            if self.space == 1:
                score = font.render("?", True, (255,0,0))
                SCREEN.blit(score, (self.rect.x+10, 300))
            elif self.space == 3:
                score = font.render("???????????????", True, (255,0,0))
                SCREEN.blit(score, (self.rect.x-15, 300))
            elif self.space == 5:
                score = font.render("최상위밖에 없잖아??!!??", True, (255,0,0))
                SCREEN.blit(score, (self.rect.x-15, 300))
                self.image = pygame.image.load("tomatotomato.png") 
                self.image = pygame.transform.scale(self.image, (120, 120))
            elif self.space == 7:
                pass
                


        #뽑기
        elif self.map_num == 3:
            if self.space == 1:
                score = font.render("뽑아보자!", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x-15, 300))

            if self.one != 0:
                SCREEN.blit(pop1, (0,0))
                #self.one = 0
            elif self.two != 0:
                SCREEN.blit(pop2, (0,0))
                #self.two = 0
            elif self.three != 0:
                SCREEN.blit(pop3, (0,0))
                #self.three = 0
            elif self.four != 0:
                SCREEN.blit(pop4, (0,0))
                #self.four = 0

            if self.space == 3:
                score = font.render("풀어보자!", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x-15, 300))

        #studying - 열공 중
        elif self.map_num == 4:
            if self.space == 1:
                score = font.render("열공열공!", True, (255,0,0))
                SCREEN.blit(score, (self.rect.x-15, 300))
            elif self.space % 2 == 1:
                score = font.render("열공중", True, (255,0,0))
                SCREEN.blit(score, (self.rect.x-15, 300))
        
        #도형 연습장
        elif self.map_num == 5:
            score = font.render("tomato 's math class", True, (0,0,0))
            SCREEN.blit(score, (15, 30))
            if self.space == 1:
                score = font.render("토마토 그려줘!", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x, 200))
            if self.space == 2:
                score = font.render("토마토 그려줘!", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x, 200))

                #토마토 그리기
                #몸통
                pygame.draw.ellipse(SCREEN, (255,0,0), [577, 340, 104, 124])
                pygame.draw.ellipse(SCREEN, (0,0,0), [571,334, 110, 130], 6) 
                #꽁지1
                pygame.draw.ellipse(SCREEN, (0,0,0), [609,309, 17, 25], 6) 
                pygame.draw.ellipse(SCREEN, (69,179,113), [615, 315, 11, 19])
                #꽁지2
                pygame.draw.ellipse(SCREEN, (0,0,0), [623,309, 17, 25], 6) 
                pygame.draw.ellipse(SCREEN, (69,179,113), [629, 315, 11, 19])
                #꽁지3
                pygame.draw.ellipse(SCREEN, (0,0,0), [636,309, 17, 25], 6) 
                pygame.draw.ellipse(SCREEN, (69,179,113), [642, 315, 11, 19])

                # 눈
                pygame.draw.line(SCREEN, (0,0,0), [613,370], [613,399], 6)
                pygame.draw.line(SCREEN, (0,0,0), [632,370], [632,399], 6)

                # 입
                pygame.draw.line(SCREEN, (0,0,0), [600,409], [625,437], 6)
                pygame.draw.line(SCREEN, (0,0,0), [644,408], [625,437], 6)

                # 팔
                pygame.draw.line(SCREEN, (0,0,0), [697,386], [681,406], 6)
                pygame.draw.line(SCREEN, (0,0,0), [574,417], [552,401], 6)

                # 다리
                pygame.draw.line(SCREEN, (0,0,0), [635,457], [635,478], 6)
                pygame.draw.line(SCREEN, (0,0,0), [614,457], [614,478], 6)                
            elif self.space == 3:
                score = font.render("안녕? ", True, (0,0,0))
                SCREEN.blit(score, (self.rect.x, 200))

            elif self.space == 4:
                #토마토 그리기
                #몸통
                pygame.draw.ellipse(SCREEN, (255,0,0), [577, 340, 104, 124])
                pygame.draw.ellipse(SCREEN, (0,0,0), [571,334, 110, 130], 6) 
                #꽁지1
                pygame.draw.ellipse(SCREEN, (0,0,0), [609,309, 17, 25], 6) 
                pygame.draw.ellipse(SCREEN, (69,179,113), [615, 315, 11, 19])
                #꽁지2
                pygame.draw.ellipse(SCREEN, (0,0,0), [623,309, 17, 25], 6) 
                pygame.draw.ellipse(SCREEN, (69,179,113), [629, 315, 11, 19])
                #꽁지3
                pygame.draw.ellipse(SCREEN, (0,0,0), [636,309, 17, 25], 6) 
                pygame.draw.ellipse(SCREEN, (69,179,113), [642, 315, 11, 19])

                # 눈
                pygame.draw.line(SCREEN, (0,0,0), [613,370], [613,399], 6)
                pygame.draw.line(SCREEN, (0,0,0), [632,370], [632,399], 6)

                # 입
                pygame.draw.line(SCREEN, (0,0,0), [600,409], [625,437], 6)
                pygame.draw.line(SCREEN, (0,0,0), [644,408], [625,437], 6)

                # 다리
                pygame.draw.line(SCREEN, (0,0,0), [635,457], [635,478], 6)
                pygame.draw.line(SCREEN, (0,0,0), [614,457], [614,478], 6) 

                # 왼팔
                pygame.draw.line(SCREEN, (0,0,0), [574,417], [557-27*math.cos(self.theta),401+27*math.sin(self.theta)], 6)
                #pygame.draw.line(SCREEN, (0,0,0), [697,386], [681,406], 6) 

                pygame.draw.line(SCREEN, (0,0,0), [681,406], [681+27*math.cos(self.theta), 406+27*math.sin(self.theta)],6)
                #도착하려고 하는 값은 : theta : ->                 # (27, 0.50575753) = (r,theta) - 시작지점
                # 690,421 (0.54784563)

                #                pygame.draw.line(SCREEN, (0,0,0), [27*theta, 27*theta], [681,406], 6)
                #

                




                    


    def change(self):
        # 토마토값을 바꾸는 곳
        if 1<=tkey < 5:
            score = font.render("토마토의 모양을 바꿀 수 있어요!", True, (255,0,255))
            SCREEN.blit(score, (150,300))

        if self.tomato %4 == 0:
            self.image = pygame.image.load("tomato.png")
        # ũ?? ????
            self.image = pygame.transform.scale(self.image, (100, 100))
        elif self.tomato % 4 == 1:
            self.image = pygame.image.load("tomatotomato.png")
        # ũ?? ????
            self.image = pygame.transform.scale(self.image, (100, 100))
        elif self.tomato % 4 == 2:
            self.image = pygame.image.load("sadtomato.png")
        # ũ?? ????
            self.image = pygame.transform.scale(self.image, (100, 100))
        elif self.tomato % 4 == 3:
            self.image = pygame.image.load("redtomato.png")
        # ũ?? ????
            self.image = pygame.transform.scale(self.image, (100, 100))


    '''
                elif self.space == 4:
                #토마토 그리기
                #몸통
                pygame.draw.ellipse(SCREEN, (255,0,0), [577, 340, 104, 124])
                pygame.draw.ellipse(SCREEN, (0,0,0), [571,334, 110, 130], 6) 
                #꽁지1
                pygame.draw.ellipse(SCREEN, (0,0,0), [609,309, 17, 25], 6) 
                pygame.draw.ellipse(SCREEN, (69,179,113), [615, 315, 11, 19])
                #꽁지2
                pygame.draw.ellipse(SCREEN, (0,0,0), [623,309, 17, 25], 6) 
                pygame.draw.ellipse(SCREEN, (69,179,113), [629, 315, 11, 19])
                #꽁지3
                pygame.draw.ellipse(SCREEN, (0,0,0), [636,309, 17, 25], 6) 
                pygame.draw.ellipse(SCREEN, (69,179,113), [642, 315, 11, 19])

                # 눈
                pygame.draw.line(SCREEN, (0,0,0), [613,370], [613,399], 6)
                pygame.draw.line(SCREEN, (0,0,0), [632,370], [632,399], 6)

                # 입
                pygame.draw.line(SCREEN, (0,0,0), [600,409], [625,437], 6)
                pygame.draw.line(SCREEN, (0,0,0), [644,408], [625,437], 6)

                # 다리
                pygame.draw.line(SCREEN, (0,0,0), [635,457], [635,478], 6)
                pygame.draw.line(SCREEN, (0,0,0), [614,457], [614,478], 6) 

                # 왼팔
                pygame.draw.line(SCREEN, (0,0,0), [574,417], [552,401], 6)

                # 왼쪽 팔 : 중심 (574,417), 반지름 (27), 방정식 ((x-574)^2 + (y-417)^2 = 27^2)
                # 오른쪽 팔 : 중심 (681,406), 반지름 (27), 방정식 ()
                # x^2 + y^2 = 27^2
                # (27, 0.50575753) = (r,theta) - 시작지점
                # 690,421 (0.54784563)

                # 이때 x값은 : r*cos(theta)
                # 이때 y값은 : r*sin(theta)
                theta = 0.50575753
                while True:

                    if theta >= 0.54784563:
                        break

                    x = 27*math.cos(theta)
                    y = 27*math.sin(theta)

                    pygame.draw.line(SCREEN, (0,0,0), [x, y], [681,406], 6)


                    pygame.draw.line(SCREEN, (255,255,255), [x, y], [681,406], 6)
                    theta += 0.0001
                    '''
           

def main():
    global SCREEN, WINDOW_WIDTH, WINDOW_HEIGHT, base, map_num, tkey

    
    map_num = 0
    tkey = 0
    trial = 0
    move = 0.2
    # pygame ?ʱ?ȭ ?? ??ũ?? ????
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("happytomato")

    #SCREEN.blit(base, (800,430))

    clock = pygame.time.Clock()

 

    # ?÷??̾? ?ڵ??? ????
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

 

            # ȭ??ǥ Ű?? ?̿??ؼ? ?÷??̾??? ?????? ?Ÿ??? ???????ش?.
            # Ű?? ???? ?????? ?Ÿ??? 0???? ?Ѵ?.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.dx = 5
                elif event.key == pygame.K_LEFT:
                    player.dx = -5

                if event.key == pygame.K_SPACE:
                    player.space += 1
                    if player.isJump == 0:
                        player.jump(1)
                if event.key == pygame.K_t:
                    player.tomato += 1
                    tkey += 1
                if event.key == pygame.K_1:
                    player.one = 1
                elif event.key == pygame.K_2:
                    player.two = 1
                elif event.key == pygame.K_3:
                    player.three = 1
                elif event.key == pygame.K_4:
                    player.four = 1
                elif event.key == pygame.K_5:
                    
                    if trial % 5 == 0:
                        move = -move
                    player.theta += move

                    trial += 1
 

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
                elif event.key == pygame.K_LEFT:
                    player.dx = 0
                elif event.key == pygame.K_t:
                    pass


        # ?????? ???????
        player.map()
        player.conversation()
        player.draw_car()
        
        player.move_x()
        player.update()
        player.check_screen()
        
        player.change()
        pygame.display.flip()

        

        # ?ʴ? ?????? ????
        clock.tick(60)


if __name__ == '__main__':
    main()