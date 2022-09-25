import pygame,sys
from pygame import mixer
import os


#initializing pygame
pygame.init()
clock=pygame.time.Clock()

MUSIC_EVENT = pygame.USEREVENT + 1

#variables####################
white=(255,255,255)          #
black=(0,0,0)                #
aqua=(0,255,255)             #
pp=-1                        #
musicnumber=-1               #
xx,yy=0,200                  #
duration=1
seek=0
cheat=""
hold=None
cheatcode="12019725"
##############################



#creating screen

screen=pygame.display.set_mode((800,600))

#backgroung image setting
background=pygame.image.load('assets/background.png')


#title and icon
pygame.display.set_caption("MUSIC PLAYER BY SAURABH PANDEY")
icon=pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

#finding all music files
musics=[]
string=None
string2=""
x=0
dir_path= os.path.dirname(os.path.realpath(__file__))

for root ,dirs,files in os.walk(dir_path):
    for file in files:
        if file.endswith('.mp3'):
            musics.append((root+'/'+str(file)))

#adding these music files in a list
for i in musics:
    string=i
    string2=""
    for j in range(-1,-100,-1):
        if(string[j]=='/'):
            musics[x]=string2
            x+=1
            break
        string2=string[j]+string2

for i in musics:
    print(i)


# defining a font
Font = pygame.font.SysFont('Corbel',20)
Font2= pygame.font.SysFont('Corbel',50)
Font3= pygame.font.SysFont('Corbel',30)
# rendering a text written in
# this font
Next = pygame.image.load('assets/next.png')
Pause = pygame.image.load('assets/pause.png')
Play = pygame.image.load('assets/play.png')
Start  = pygame.image.load('assets/play.png')
Previous  = pygame.image.load('assets/previous.png')





def NEXT():
    pygame.mixer.music.set_endevent(MUSIC_EVENT)
    mixer.music.unload()
    global musicnumber
    musicnumber+=1
    if(musicnumber==len(musics)):
        musicnumber=0
    mixer.music.load('./music/'+musics[musicnumber])
    mixer.music.play(1)

    
def PREVIOUS():
     pygame.mixer.music.set_endevent(MUSIC_EVENT)
     mixer.music.unload()
     global musicnumber
     musicnumber-=1
     if(musicnumber<0):
         musicnumber=len(musics)-1
     mixer.music.load('./music/'+musics[musicnumber])
     mixer.music.play(1)
     

def PLAY_PAUSE():
     global pp
     if(pp==1):
        pp=0
        mixer.music.pause()
        
     elif(pp==0):
         pp=1
         mixer.music.unpause()
     

def START():
    global pp
    pygame.mixer.music.set_endevent(MUSIC_EVENT)
    pp=1
    mixer.music.load('./music/'+musics[musicnumber])
    mixer.music.play(1)

def NAME_ANIMATION(xx,yy):
    Song=Font2.render(musics[musicnumber] , True , white)
    screen.blit(Song,(xx,yy))


def TIME_UPDATE(time):
    
    Time= Font3.render(time , True , white)
    screen.blit(Time,(10,10))
    

def DURATION():
    global duration
    a = pygame.mixer.Sound('./music/'+musics[musicnumber])
    duration=int(a.get_length())
    
    
    



#main loop
stop=True
while stop:
    
    #background color fill
    screen.fill((60,30,60))
    #background image 
    screen.blit(background,(0,0))
    
    

    #capturing all events
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            stop=False
            pygame.quit()
            sys.exit()


        #capturing mouse events
        if eve.type == pygame.MOUSEBUTTONDOWN :
            if 370<=mouse[0]<=434 and 500<=mouse[1]<=564:#play/pause
                if(pp==-1):
                    START()
                    DURATION()
                else: 
                    PLAY_PAUSE()
                
            if 540<=mouse[0]<=604 and 500<=mouse[1]<=564 and pp!=-1:#next
                NEXT()
                DURATION()

            if (200<=mouse[0]<=264 and 500<=mouse[1]<=564 and pp!=-1):#previous
                PREVIOUS()
                DURATION()

            #if 0<=mouse[0]<=800 and 400<=mouse[1]<=420:
                #pygame.mixer.music.set_pos(int((mouse[0]*duration)/800))
        

        #capturing keyboard events 
        if eve.type == pygame.KEYDOWN:
            if eve.key == pygame.K_LEFT and pp!=-1:
                PREVIOUS()
                DURATION()
            if eve.key == pygame.K_RIGHT and pp!=-1:
                NEXT()
                DURATION()
            if eve.key == pygame.K_SPACE:
                if pp==-1:
                    START()
                    DURATION()
                else:
                    PLAY_PAUSE()    
            if eve.type == pygame.KEYDOWN:#cheats
                hold=(eve.unicode)
                cheat=cheat+hold

            if eve.key == pygame.K_x:#cheat reset
                cheat=""
            
                

                
        if eve.type == MUSIC_EVENT:
            NEXT()
            DURATION()
                
            

                
                
             

                
                    
                    
                    
    #cheat setup and comparision                
    if (len(cheat)==len(cheatcode)):
        if(cheat==cheatcode):
            cheat=""
            START()
            DURATION()
        else:
            cheat=""

    # stores the (x,y) coordinates into
    # the variable as a list
    mouse = pygame.mouse.get_pos()


    #button stuff with color change when hover tough part  
    if(pp==0):
        screen.blit(Play,(370,500))
    elif(pp==1):
        screen.blit(Pause,(370,500))
    elif(pp==-1):
        screen.blit(Start,(370,500
                           ))

            

    screen.blit(Next,(540,500))

    screen.blit(Previous,(200,500))

        

    
    if(xx>800):
        xx=-20*(len(musics[musicnumber]))
    else:
        xx+=0.2
    NAME_ANIMATION(xx,yy)

    time=(mixer.music.get_pos())
    time=(time/1000)
    TIME_UPDATE(str(int(time)))

    #making progress bar without any readymade module. why? because i want to
    seek=int(time*(800/duration))
    pygame.draw.rect(screen,aqua,[0,400,seek,10])
    pygame.draw.rect(screen,black,[0,397,800,2])
    pygame.draw.rect(screen,black,[0,411,800,2])
    
        

    pygame.display.update()


    
