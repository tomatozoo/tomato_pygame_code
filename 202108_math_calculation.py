#-*- coding: utf-8 -*-#

import sympy as sp
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
        self.x = 0
        self.y = 0
        self.bottom = 0
        self.centerx = 0
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
        self.right_arm = 0.001
        self.left_arm = 0.001
        self.right_leg = 0
        self.left_leg = 0
        self.user_text = ''
        self.active = False
        self.input_rect = pygame.Rect(200,200,140,32)
        self.color_change = False

 

    def load_car(self):
        self.x = 0
        self.y = 0


 

    # ?ڵ????? ??ũ???? ?׸???
    def draw_car(self):
        self.bottom = 124 + self.y
        self.centerx = (570+self.x) / 2


        # 몸통
        pygame.draw.ellipse(SCREEN, (255,0,0), [577+self.x, 340+self.y, 104, 124])
        pygame.draw.ellipse(SCREEN, (0,0,0), [571+self.x,334+self.y, 110, 130], 6)
                #꽁지1
        pygame.draw.ellipse(SCREEN, (0,0,0), [609+self.x,309+self.y, 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [615+self.x, 315+self.y, 7, 15])
                #꽁지2
        pygame.draw.ellipse(SCREEN, (0,0,0), [623+self.x,309+self.y, 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [629+self.x, 315+self.y, 7, 15])
                #꽁지3
        pygame.draw.ellipse(SCREEN, (0,0,0), [636+self.x,309+self.y, 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [642+self.x, 315+self.y, 7, 15])

                # 눈
        pygame.draw.line(SCREEN, (0,0,0), [613+self.x,370+self.y], [613+self.x,399+self.y], 6)
        pygame.draw.line(SCREEN, (0,0,0), [632+self.x,370+self.y], [632+self.x,399+self.y], 6)

                # 입
        pygame.draw.line(SCREEN, (0,0,0), [600+self.x,409+self.y], [625+self.x,437+self.y], 6)
        pygame.draw.line(SCREEN, (0,0,0), [644+self.x,408+self.y], [625+self.x,437+self.y], 6)

                # 팔

                # 오른팔
        pygame.draw.line(SCREEN, (0,0,0), [697+self.x+25.6*math.cos(self.right_arm),386+self.y+25.6*math.sin(self.right_arm)], [681+self.x,406+self.y], 6)
        pygame.draw.ellipse(SCREEN, (0,0,0), [684+self.x+25.6*math.cos(self.right_arm),368+self.y+25.6*math.sin(self.right_arm), 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [690+self.x+25.6*math.cos(self.right_arm), 374+self.y+25.6*math.sin(self.right_arm), 7, 15])

                # 왼팔
        pygame.draw.line(SCREEN, (0,0,0), [574+self.x,417+self.y], [552+self.x-25.6*math.cos(self.left_arm),401+self.y+25.6*math.sin(self.left_arm)], 6)

        pygame.draw.ellipse(SCREEN, (0,0,0), [536+self.x-25.6*math.cos(self.left_arm), 386+self.y+25.6*math.sin(self.left_arm), 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [542+self.x-25.6*math.cos(self.left_arm), 392+self.y+25.6*math.sin(self.left_arm), 7, 15])


                # 오른다리
        pygame.draw.line(SCREEN, (0,0,0), [635+self.x,457+self.y], [635+self.x,478+self.y], 6) # r = 21

        pygame.draw.ellipse(SCREEN, (0,0,0), [631+self.x,477+self.y, 30, 16], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [637+self.x, 483+self.y, 20, 6])

                # 왼다리
        pygame.draw.line(SCREEN, (0,0,0), [614+self.x,457+self.y], [614+self.x,478+self.y], 6) 
                
        pygame.draw.ellipse(SCREEN, (0,0,0), [590+self.x,476+self.y, 30, 16], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [596+self.x,482+self.y, 20, 6])     

 

    # x ??ǥ ?̵? - ?÷??̾? ?ڵ????? ?????? ?????? ?? ?ʿ?
    def move_x(self):
        self.x += self.dx


 

    # ȭ?? ?????? ?? ?????? ????
    def check_screen(self):
        if self.y > 10:
            self.y = 10
        elif self.y < -197:
            self.y = -197

    #???? ???¸? üũ
    def jump(self, j):
        self.isJump = j

    def update(self):
        if self.isJump > 0:
            if self.v > 0:
                F = (0.5*self.m*(self.v*self.v))
            else:
                F = -(0.5*self.m*(self.v*self.v))
            self.y -=round(F)
            self.v -= 1

            if self.y > 13:
                self.y = 13
                self.isJump = 0
                self.v = VELOCITY

    def userinput(self):
        self.input_rect = pygame.Rect(200,200,140,32)
        color_active = pygame.Color('lightskyblue3')
        color_passive = pygame.Color('gray15')
        color = color_passive

        if self.active == True:
            if self.color_change == True:
                color = color_active
            text_surface = font.render(self.user_text[1:], True, (0,0,0))
            SCREEN.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))

            self.input_rect = pygame.Rect(200,200,max(100,text_surface.get_width()+10),32)
            pygame.draw.rect(SCREEN, color, self.input_rect, 3) 
        else:
            color = color_passive

        #겹치는 거 처리 - 1이 진행키라서 1이 자꾸 나온다. 
        #엔터 동작 처리
        #color 바뀌는 것 처리
        
    def mathclass(self):
            score = font.render("tomato 's math class", True, (0,0,0))
            SCREEN.blit(score, (15, 30))

            if self.space == 0:
                #토마토 그림
                pass


            if self.space == 1:
                score = font.render("안녕? :)", True, (0,0,0))
                SCREEN.blit(score, (self.centerx, 200))
                self.user_text = ''
                self.active = True 

            if self.space == 2:

                score = font.render("네 이름이 뭐니?", True, (0,0,0))
                SCREEN.blit(score, (self.centerx, 200))                                                
                self.userinput()

            if self.space == 3:


                score = font.render(f"안녕 {self.user_text[1:]}아", True, (0,0,0))
                SCREEN.blit(score, (self.centerx-10, 200))


            if self.space > 3:
                if self.space % 4 == 0:
                    self.user_text = ''
                    self.active = True
                elif self.space %4 == 1:
                    score = font.render(f"수식을 입력하세요.", True, (0,0,0))
                    SCREEN.blit(score, (self.centerx-10, 200))                
                    self.userinput()
                    '''import sympy as sp
pol = input("Enter polynomial: ")
p = sp.sympify(pol)
dpdx = p.diff()
print("f(x) : " + sp.latex(p))
print("f'(x): " + sp.latex(dpdx))
print("g(x) : " + sp.latex(p + dpdx))'''
                elif self.space % 4 == 2:
                    p = sp.sympify(self.user_text[1:])
                    dpdx = p.diff()
                    score = font.render(f"f(x) = {sp.latex(p)}", True, (0,0,0))
                    SCREEN.blit(score, (self.centerx+50, 100))

                    score = font.render(f"f'(x) = {sp.latex(dpdx)}", True, (0,0,0))
                    SCREEN.blit(score, (self.centerx+150, 200))

                    score = font.render(f"g(x) = {sp.latex(p+dpdx)}", True, (0,0,0))
                    SCREEN.blit(score, (self.centerx+350, 300))


                else:
                    pass



    def move_legs(self):
        pass


def main():
    global SCREEN, WINDOW_WIDTH, WINDOW_HEIGHT, base, map_num, tkey

    
    map_num = 0
    tkey = 0
    trial_right = 0
    trial_left = 0
    trial_leg = 0
    move_left = 0.2
    move_right = 0.2
    move_leg = 0.2

    # pygame ?ʱ?ȭ ?? ??ũ?? ????
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("happytomato")



    clock = pygame.time.Clock()

 

    # ?÷??̾? ?ڵ??? ????
    player = Car()
    player.load_car()

 

    playing = True

    while playing:

        SCREEN.fill((255,255,255))

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()

 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player.input_rect.collidepoint(event.pos):
                    player.color_change = True

            # ȭ??ǥ Ű?? ?̿??ؼ? ?÷??̾??? ?????? ?Ÿ??? ???????ش?.
            # Ű?? ???? ?????? ?Ÿ??? 0???? ?Ѵ?.
            if event.type == pygame.KEYDOWN:
                if player.active == True:
                    if event.key == pygame.K_BACKSPACE:
                        player.user_text = player.user_text[:-1]
                    else:
                        player.user_text += event.unicode
                if event.key == pygame.K_KP_ENTER:
                    player.active = False
                if event.key == pygame.K_RIGHT:
                    player.dx = 5

                elif event.key == pygame.K_LEFT:
                    player.dx = -5

                if event.key == pygame.K_SPACE:
                    
                    if player.isJump == 0:
                        player.jump(1)
                if event.key == pygame.K_t:
                    player.tomato += 1
                    tkey += 1
                    #진행키
                if event.key == pygame.K_1:
                    player.space += 1
                    #움직임
                elif event.key == pygame.K_2:
                    pass
                elif event.key == pygame.K_3:
                    player.three = 1
                elif event.key == pygame.K_4:
                    player.four = 1
                elif event.key == pygame.K_5:                    
                    pass
                elif event.key == pygame.K_l:
                    if trial_left % 5 == 0:
                        move_left = -move_left
                    player.left_arm += move_left
                    trial_left += 1

                elif event.key == pygame.K_r:
                    if trial_right % 5 == 0:
                        move_right = -move_right
                    player.right_arm += move_right
                    trial_right += 1
                elif event.key == pygame.K_g:
                    pass
                ##사용자 인풋

                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
                elif event.key == pygame.K_LEFT:
                    player.dx = 0
                elif event.key == pygame.K_t:
                    pass


        # ?????? ???????
        
        player.draw_car()
        player.move_x()
        player.update()
        player.check_screen()
        player.mathclass()
        #player.userinput()

        pygame.display.flip()

        

        # ?ʴ? ?????? ????
        clock.tick(60)


if __name__ == '__main__':
    main()