#-*- coding: utf-8 -*-#
 
## import
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

## 한글 폰트 불러오기
pygame.font.init()
small_font = pygame.font.SysFont('malgungothic', 10)
font = pygame.font.SysFont('malgungothic', 20)
big_font = pygame.font.SysFont('malgungothic', 50)
## 아이콘 불러오기
icon = pygame.image.load('tomato.png')
pygame.display.set_icon(icon)

## 배경 불러오기
default = pygame.image.load('default.png')
default = pygame.transform.scale(default, (800, 500))
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

## 악마 불러오기
enemy = pygame.image.load('enemy.png')
enemy = pygame.transform.scale(enemy, (300, 300))


VELOCITY = 7
MASS = 2
 



## class Car
class Car:
    ## 필요한 요소들 정의
    def fade(self): 
        pygame.time.delay(5)
        fade = pygame.Surface((800,500))
        fade.fill((255,255,255))
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            SCREEN.fill((0,0,0))
            pygame.draw.rect(SCREEN, (0,0,0), (0,0,800,500),0)
            pygame.draw.rect(SCREEN, (0,0,0), (0,0,800,500),0)           
            SCREEN.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(5)
    def fade_red(self): 
        pygame.time.delay(5)
        fade = pygame.Surface((800,500))
        fade.fill((255,0,0))
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            SCREEN.fill((255,94,0))
            pygame.draw.rect(SCREEN, (255,94,0), (0,0,800,500),0)
            pygame.draw.rect(SCREEN, (255,94,0), (0,0,800,500),0)           
            SCREEN.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(1)

    def __init__(self):

        ## 델타 x, 델타 y
        self.dx = 0
        self.dy = 0

        ## x값, y값
        self.x = -500
        self.y = -30
        self.centerx = (570+self.x) / 2


        ## 점프 관련 변수
        self.isJump = 0
        self.v = VELOCITY 
        self.m = MASS  

        ## 스토리 진행 관련 변수 

        ## 화면 전환
        self.map_num = 0
        ## 진행키 - 사실은 1키
        self.space = 0
        ## 배경 화면
        self.background = 0
        self.map_background = default
        #SCREEN.blit(player.map_background, (0,0))
        ## 반응형
        self.react = False
        self.repeat = 0

        ## 동작 관련 변수
        self.theta = 0.001
        self.right_arm = 0.001
        self.left_arm = 0.001
        self.right_leg = 0.001
        self.left_leg = 0.001

        self.right = 0
        self.left = 0
        self.jumping = 0

        ## test input 관련 변수
        self.user_text = ''
        self.active = False
        self.input_rect = pygame.Rect(200,200,140,32)
        self.color_change = False
    
    def erase_car(self):
        pygame.draw.ellipse(SCREEN, (255,255,255), [577+self.x, 340+self.y, 104, 124])
        pygame.draw.ellipse(SCREEN, (255,255,255), [571+self.x,334+self.y, 110, 130], 6)
                #꽁지1
        pygame.draw.ellipse(SCREEN, (255,255,255), [609+self.x,309+self.y, 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (255,255,255), [615+self.x, 315+self.y, 7, 15])
                #꽁지2
        pygame.draw.ellipse(SCREEN, (255,255,255), [623+self.x,309+self.y, 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (255,255,255), [629+self.x, 315+self.y, 7, 15])
                #꽁지3
        pygame.draw.ellipse(SCREEN, (255,255,255), [636+self.x,309+self.y, 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (255,255,255), [642+self.x, 315+self.y, 7, 15])

                # 눈
        pygame.draw.line(SCREEN, (255,255,255), [613+self.x,370+self.y], [613+self.x,399+self.y], 6)
        pygame.draw.line(SCREEN, (255,255,255), [632+self.x,370+self.y], [632+self.x,399+self.y], 6)

                # 입
        pygame.draw.line(SCREEN, (255,255,255), [600+self.x,409+self.y], [625+self.x,437+self.y], 6)
        pygame.draw.line(SCREEN, (255,255,255), [644+self.x,408+self.y], [625+self.x,437+self.y], 6)

                # 팔

                # 오른팔
        pygame.draw.line(SCREEN, (255,255,255), [697+self.x+25.6*math.cos(self.right_arm),386+self.y+25.6*math.sin(self.right_arm)], [681+self.x,406+self.y], 6)
        pygame.draw.ellipse(SCREEN, (255,255,255), [684+self.x+25.6*math.cos(self.right_arm),368+self.y+25.6*math.sin(self.right_arm), 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (255,255,255), [690+self.x+25.6*math.cos(self.right_arm), 374+self.y+25.6*math.sin(self.right_arm), 7, 15])

                # 왼팔
        pygame.draw.line(SCREEN, (255,255,255), [574+self.x,417+self.y], [552+self.x-25.6*math.cos(self.left_arm),401+self.y+25.6*math.sin(self.left_arm)], 6)

        pygame.draw.ellipse(SCREEN, (255,255,255), [536+self.x-25.6*math.cos(self.left_arm), 386+self.y+25.6*math.sin(self.left_arm), 17, 25], 6) 
        pygame.draw.ellipse(SCREEN, (255,255,255), [542+self.x-25.6*math.cos(self.left_arm), 392+self.y+25.6*math.sin(self.left_arm), 7, 15])



                 # 오른다리
        pygame.draw.line(SCREEN, (255,255,255), [635+self.x,457+self.y], [635+self.x+25.6*math.cos(self.left_leg)-25.6*math.cos(0.001),488+self.y-2.56*math.sin(self.left_leg)], 6) # r = 21

        pygame.draw.ellipse(SCREEN, (255,255,255), [614+self.x+25.6*math.cos(self.left_leg)-25.6*math.cos(0.001),487+self.y-2.56*math.sin(self.left_leg), 30, 16], 6) 

        pygame.draw.ellipse(SCREEN, (255,255,255), [617+self.x+25.6*math.cos(self.left_leg)-25.6*math.cos(0.001), 493+self.y-2.56*math.sin(self.left_leg), 20, 6])
        
                # 왼다리
        pygame.draw.line(SCREEN, (255,255,255), [614+self.x,457+self.y], [614+self.x-25.6*math.cos(self.left_leg)+25.6*math.cos(0.001),488+self.y-2.56*math.sin(self.left_leg)], 6) 
                
        pygame.draw.ellipse(SCREEN, (255,255,255), [590+self.x-25.6*math.cos(self.left_leg)+25.6*math.cos(0.001),486+self.y-2.56*math.sin(self.left_leg), 30, 16], 6) 
        pygame.draw.ellipse(SCREEN, (255,255,255), [596+self.x-25.6*math.cos(self.left_leg)+25.6*math.cos(0.001),492+self.y-2.56*math.sin(self.left_leg), 20, 6])     

    def draw_car(self):

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
        pygame.draw.line(SCREEN, (0,0,0), [635+self.x,457+self.y], [635+self.x+25.6*math.cos(self.left_leg)-25.6*math.cos(0.001),488+self.y-2.56*math.sin(self.left_leg)], 6) # r = 21

        pygame.draw.ellipse(SCREEN, (0,0,0), [614+self.x+25.6*math.cos(self.left_leg)-25.6*math.cos(0.001),487+self.y-2.56*math.sin(self.left_leg), 30, 16], 6) 

        pygame.draw.ellipse(SCREEN, (69,179,113), [617+self.x+25.6*math.cos(self.left_leg)-25.6*math.cos(0.001), 493+self.y-2.56*math.sin(self.left_leg), 20, 6])
        
                # 왼다리
        pygame.draw.line(SCREEN, (0,0,0), [614+self.x,457+self.y], [614+self.x-25.6*math.cos(self.left_leg)+25.6*math.cos(0.001),488+self.y-2.56*math.sin(self.left_leg)], 6) 
                
        pygame.draw.ellipse(SCREEN, (0,0,0), [590+self.x-25.6*math.cos(self.left_leg)+25.6*math.cos(0.001),486+self.y-2.56*math.sin(self.left_leg), 30, 16], 6) 
        pygame.draw.ellipse(SCREEN, (69,179,113), [596+self.x-25.6*math.cos(self.left_leg)+25.6*math.cos(0.001),492+self.y-2.56*math.sin(self.left_leg), 20, 6])     
 



    # 좌우 이동
    def move_x(self):
        self.x += self.dx

    # x,y 제한 설정
    def check_screen(self):
        if self.y > 0:
            pass
        elif self.y < -197:
            self.y = -197

        elif self.x < -500:
            self.x = -500

    # 점프 상태 반영
    def jump(self, j):
        self.isJump = j
    
    # 점프 상태에 따른 움직임
    def update(self):
        if self.isJump > 0:
            if self.v > 0:
                F = (0.5*self.m*(self.v*self.v))
            else:
                F = -(0.5*self.m*(self.v*self.v))
            self.y -=round(F)
            self.v -= 1

            if self.y > 0:
                self.y = 0
                self.isJump = 0
                self.v = VELOCITY

    # user input
    def userinput(self):

        ## input 상자
        self.input_rect = pygame.Rect(200,200,140,32)
        color_active = pygame.Color('lightskyblue3')
        color_passive = pygame.Color('gray15')
        color = color_passive
        
        ## 텍스트 인풋 + 출력
        if self.active == True:
            if self.color_change == True:
                color = color_active
            text_surface = font.render(self.user_text, True, (0,0,0))
            SCREEN.blit(text_surface, (self.input_rect.x+100, self.input_rect.y+5))
            pygame.display.update()
            self.input_rect = pygame.Rect(300,200,max(100,text_surface.get_width()+10),32)
            pygame.draw.rect(SCREEN, color, self.input_rect, 3) 
            pygame.display.update()
            
        else:
            color = color_passive
            pygame.display.update()

    # 게임 진행 구성
  
    def mathclass(self):

            #score = font.render("tomato 's math class", True, (0,0,0))
            #SCREEN.blit(score, (15, 30))

            
            ## intro
            if self.background == 0:
                pass


    def set_background(self):

        if self.background == 0:

            ## intro
            ## 800 * 500

            ## intro 클릭

            

            ## react intro 보여주기

            if self.react == True:

                if self.repeat == 0:
                    SCREEN.fill((0,0,0))
                    self.react_intro = pygame.image.load("reacting_intro.png")
                    self.react_intro = pygame.transform.scale(self.react_intro, (200,200))
                    SCREEN.blit(self.react_intro, [300,250]) 

                    score = font.render("준비됐나요?", True, (255,255,255))
                    SCREEN.blit(score, (340, 200))



                    for i in range(0,5):
                        
                        pygame.display.update()
                        score = big_font.render(f"{5-i}", True, (255,255,255))
                        SCREEN.blit(score,(390,130))
                        pygame.display.update()
                        pygame.time.delay(600)

                        score = big_font.render(f"{5-i}", True, (0,0,0))
                        SCREEN.blit(score,(390,130))
                        pygame.display.update()

                        pygame.time.delay(600)
                    self.repeat += 1

                pygame.display.update()

                if self.repeat == 1:
                    self.fade()
                    self.repeat += 1

                if self.repeat == 2:
                    for i in range(0,170):  
                        self.draw_car()
                        self.mathclass()
                        self.dx = 0.8
                        self.move_x()
                        self.update()
                        pygame.display.update()
                        pygame.time.delay(10)
                        self.move_x()
                        self.update()
                        pygame.display.update()
                        SCREEN.fill((255,255,255))
                    self.dx = 0

                    self.repeat += 1
                    
                if self.repeat == 3:
                    for i in range(1):
                        score = font.render("안녕?", True, (0,0,0))
                        SCREEN.blit(score, (340, 100))
                        self.draw_car()
                        self.mathclass()
                        self.move_x()
                        self.update()
                        pygame.display.update()
                        pygame.time.delay(1000)
               
                    pygame.draw.rect(SCREEN, (255,255,255), [340,100, 100,50])
                    pygame.display.update()
                    self.repeat += 1

                if self.repeat == 4:
                    pygame.time.delay(100)
                    for i in range(1):
                        score = font.render("네 이름이 뭐니?", True, (0,0,0))
                        SCREEN.blit(score, (340, 200))
                        self.draw_car()
                        self.mathclass()
                        self.move_x()
                        self.update()
                        pygame.display.update()
                        pygame.time.delay(1000)
                    
                    pygame.draw.rect(SCREEN, (255,255,255), [340,200,300,50])
                    pygame.display.update()
                    self.repeat += 1

                    self.user_text = ''
                    self.active = True

                if self.repeat == 5:
                    
                    score = font.render("네모박스 안에 이름을 적어주세요", True, (0,0,0))
                    SCREEN.blit(score, (200, 100))

                    self.userinput()

                    if self.active == False:
                        pygame.draw.rect(SCREEN, (255,255,255), [340,200,300,50])
                        pygame.display.update()
                        self.repeat += 1

                if self.repeat == 6:
                    
                    score = font.render(f"{self.user_text}, 안녕", True, (0,0,0))
                    SCREEN.blit(score, (200, 100))
                    self.background +=1
                    self.repeat = 0
            
                        
                
            else:
                SCREEN.fill((0,0,0))
                self.intro = pygame.image.load("intro.png")
                self.intro = pygame.transform.scale(self.intro, (200,200))
                SCREEN.blit(self.intro, [300,250])

                score = font.render("Click to Start . . .", True, (255,255,255))
                SCREEN.blit(score, (330, 200))

            ## 로딩중 보여주기



        elif self.background == 1:
            ##디폴트를 흰 배경으로 설정하고, 1을 basicbackground라고 하자. 
            ##map 함수로 분리할 것!

            ##default를 self.default 이미지로 설정하기!
            if self.repeat == 0:
                for i in range(1):
                   self.fade()
                   self.react = False
                self.repeat += 1

            # 여기부터 시작하면 된다.


            ## 배경 바꾸기
            if self.repeat == 1:
                score = font.render(f"안녕 {self.user_text}아", True, (0,0,0))
                SCREEN.blit(score, (300, 200))


                score = small_font.render("다음으로 넘어가려면, 터치패드 클릭!", True, (178,178,178))
                SCREEN.blit(score, (300, 100))

                if self.react == True:
                    self.repeat += 1
                    self.react = False


            if self.repeat == 2:

                score = font.render("최상위 숲에 온 걸 환영해!", True, (0,0,0))
                SCREEN.blit(score, (300, 200))

                score = small_font.render("다음으로 넘어가려면, 터치패드 클릭!", True, (178,178,178))
                SCREEN.blit(score, (300, 100))

                if self.react == True:
                    self.repeat += 1
                    self.react = False

            if self.repeat == 3:
                ##이거 좀 보충하자. 
                score = font.render("오른쪽/왼쪽 이동, 점프를 해보자!", True, (0,0,0))
                SCREEN.blit(score, (300, 200))

                score = small_font.render("다음으로 넘어가려면, 터치패드 클릭!", True, (178,178,178))
                SCREEN.blit(score, (300, 50))

                if 1<=self.right <4:
                    score = font.render("오른쪽~", True, (0,0,0))
                    SCREEN.blit(score, (700, 200))

                if 1<=self.left <4:
                    score = font.render("왼쪽~", True, (0,0,0))
                    SCREEN.blit(score, (100, 200))

                if 1<= self.jumping <4:
                    score = font.render("점프!", True, (0,0,0))
                    SCREEN.blit(score, (300, 10))

                if self.react == True:
                    self.repeat += 1
                    self.react = False

            ## 댄스댄스~
            if self.repeat == 4:
                score = font.render("내 이름은 토마토야.", True, (0,0,0))
                SCREEN.blit(score, (300, 200))
                score = font.render("나랑 최상위숲에서 놀자!", True, (0,0,0))
                SCREEN.blit(score, (300, 250))
                score = small_font.render("다음으로 넘어가려면, 터치패드 클릭!", True, (178,178,178))
                SCREEN.blit(score, (300, 150))

                if self.react == True:
                    self.repeat += 1
                    self.react = False

            if self.repeat == 5:
                score = font.render("그럼 출발할까?", True, (0,0,0))
                SCREEN.blit(score, (300, 200))

                score = small_font.render("오른쪽 맵으로 이동하세요.", True, (178,178,178))
                SCREEN.blit(score, (300, 150))

                ## 왼쪽 끝 -500 오른쪽 끝 80
                if self.x >= 70:
                    self.x = -800
                    self.react = False
                    self.repeat += 1
                    
            if self.repeat == 6:
                score = small_font.render("오른쪽 맵으로 이동하세요.", True, (178,178,178))
                SCREEN.blit(score, (300, 150))

                score = big_font.render("총총", True, (178,178,178))
                SCREEN.blit(score, (300, 200))

                ## 왼쪽 끝 -500 오른쪽 끝 80
                if self.x >= 70:
                    self.x = -800
                    self.react = False                   
                    self.repeat += 1

            if self.repeat == 7:
                score = small_font.render("오른쪽 맵으로 이동하세요.", True, (178,178,178))
                SCREEN.blit(score, (300, 150))

                ## 왼쪽 끝 -500 오른쪽 끝 80
                if self.x >= 80:
                    self.x = 80
                    self.react = False                   
                    self.repeat = 0
                    self.background = 2
                self.fade_repeat = 0
            ## 사실은 춤출 수도 있어. 

            ## 댄스단스~ 신나신냐

            ## 내 이름은 토마토야!

            ## 나랑 같이 최상위숲에서 놀자!

            ## 그럼 출발할까?

            ## 클릭 인풋 받기

            ## 오른쪽 버튼 누르게 하기

            # 벽에 부딪히면, self.background == 3 으로 넘어감. 

        elif self.background == 2:
            if self.fade_repeat == 0:
                SCREEN.fill((255,0,0))       
                pygame.display.update()
                pygame.time.delay(30)
                self.fade_repeat += 1

            if self.fade_repeat == 1:
                pygame.display.update()
                score = big_font.render("?!?!", True, (0,0,0))
                SCREEN.blit(score, (200, 50))                  
                pygame.display.update()


                self.fade_repeat += 1

            if self.fade_repeat == 2:
                pygame.display.update()
                for i in range(500):
                    if 200 <= i <= 400:
                        score = big_font.render("도와줘~~~~", True, (0,0,0))
                        SCREEN.blit(score, (300, 100))  

                    SCREEN.blit(enemy, (50+i*0.7, 150))
                    
                    self.x = -220+i*0.7
                    self.draw_car()                    
                    self.move_x()
                    self.update()

                    pygame.display.update()
                    pygame.time.delay(3)
                self.fade_repeat+= 1
                pygame.display.update()

            if self.fade_repeat ==3:
                SCREEN.fill((0,0,0))
                pygame.time.delay(10)
                self.fade_repeat += 1

            if self.fade_repeat == 4:
                
                self.y = -300
                self.save_tomato=False
                self.fade_repeat += 1

            if self.fade_repeat == 4:
                score = big_font.render("토마토 구하기 미션", True, (0,0,0))
                SCREEN.blit(score, (200, 50))                   

                score = small_font.render("뽑기로 문제 개수를 고르고, 최상위 문제를 풀면서 토마토를 구할 힘을 기른다.", True, (0,0,0))
                SCREEN.blit(score, (200, 100))    
                
                score = small_font.render("문제 개수를 뽑으려면 터치패드 클릭!", True, (0,0,0))
                SCREEN.blit(score, (200, 150))   
                score = small_font.render("문제를 다 풀면, 스페이스키를 눌러 토마토를 구한다!", True, (0,0,0))
                SCREEN.blit(score, (200, 200))   
                if self.react == True:
                    score = big_font.render(f"문제 개수 : {random.randing(2,4)}", True, (255,0,0))
                    SCREEN.blit(score, (200, 150))   
                    self.react = False
                if self.save_tomato == True and self.y<0:
                    self.y+= 150
                elif self.y >= -10:
                    self.fade_repeat += 1

            if self.fade_repeat == 5:
                for i in range(1):
                    self.fade()
                self.fade_repeat += 1

            if self.fade_repeat == 6:
                score = big_font.render("승리!", True, (0,0,0))
                SCREEN.blit(score, (200, 50)) 
        elif self.background == 3:
            pass

            ##fade in

        elif self.background == 4:
            pass

            ## fade out

            ## 최상위 게임 토마토 살리기

            ## 요소 - 에너지 or 목숨 게이지

            ## 요소 - 토마토 - 머리통만 보이거나 / 진행 상황 보여주기

            ## 문제를 풀 때마다 클릭할 수 있다.

            ## 한 세 번 반복하면 꺼낼 수 있도록 한다. 

        elif self.background == 5:
            pass
            ## 승리 페이지
        elif self.background == 6:
            pass
            ## 패배 페이지
        elif self.background == 7:
            pass
            ## 엔딩 페이지

    def map(self):
        if self.background == 0:
            pass
        elif self.background == 1:
            self.map_background = basicbackground
        elif self.background == 2:
            self.map_background = pop

def main():
    global SCREEN, WINDOW_WIDTH, WINDOW_HEIGHT, base, map_num, tkey

    
    map_num = 0
    tkey = 0
    trial_right = 0
    trial_left = 0
    trial_leg = 3
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


    playing = True

    while playing:

        
        SCREEN.blit(player.map_background, (0,0))
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                sys.exit()

 
            if event.type == pygame.MOUSEBUTTONDOWN:                
                player.react = True
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
                    player.right += 1

                elif event.key == pygame.K_LEFT:
                    player.dx = -5
                    player.left += 1

                if event.key == pygame.K_SPACE:
                    
                    if player.isJump == 0:
                        player.jump(1)
                        player.jumping += 1

                if event.key == pygame.K_1:
                    player.space += 1




                ## 팔 움직이기
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
                    if trial_leg % 7 == 0:
                        move_leg = -move_leg
                    player.left_leg += move_leg
                    trial_leg += 1
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.dx = 0
                elif event.key == pygame.K_LEFT:
                    player.dx = 0

        
        player.draw_car()
        player.mathclass()
        player.move_x()
        player.update()
        player.check_screen()
        player.set_background()
        player.map()
        #player.userinput()
        pygame.display.flip()

        
        clock.tick(60)


if __name__ == '__main__':
    main()
