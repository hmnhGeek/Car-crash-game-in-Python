import pygame, random
from Tkinter import*
from PIL import ImageTk, Image
import tkMessageBox


import pickle, os
from uuid import getnode as get_mac
mac = get_mac()

level = 3
def game():
    def start():
        root.destroy()
        gameLevel = level
        pygame.init()

        display_width=800
        display_height=600
        AppleThickness = 100
        FPS=100

        redImg = pygame.image.load('red.png')
        yellImg = pygame.image.load('yellow.png')

        x=pygame.display.set_mode((display_width, display_height))
        pygame.display.set_icon(redImg)
        pygame.display.set_caption('Car Crash!')

        clock=pygame.time.Clock()

        smallfont=pygame.font.SysFont('comicsansms', 25)
        medfont=pygame.font.SysFont('comicsansms', 50)
        largefont=pygame.font.SysFont('comicsansms', 80)

        def score(score):
            text = smallfont.render('Score: '+str(score), True, (255, 255, 255))
            x.blit(text, [0,0])

        def pause():
            paused=True
            msg_2_scr('Paused', (0,0,0), -100, 'large')
            msg_2_scr('Press C to continue or Q to quit.', (0,0,0), 25)
            pygame.display.update()
            while paused:
                pygame.mixer.music.pause()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            pygame.mixer.music.unpause()
                            paused = False
                        elif event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                clock.tick(5)

        def randCarGen():
            applX = round(random.randrange(0, display_width-AppleThickness))
            applY = 0
            pygame.draw.rect(x, (0, 255, 0), (applX, applY, 100, 100))
            pygame.display.update()
            return applX, applY

        def game_intro():
            intro=True
            while intro:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            intro = False

                        elif event.key == pygame.K_q:
                            pygame.quit()
                            quit()
                            
                        
                x.fill((255, 255, 255))
                msg_2_scr('Welcome to Car Crash!', (0, 255, 0), -100, 'large')
                msg_2_scr('The objective of the game is to save your car from',
                          (0, 0, 0), -30)
                msg_2_scr('the cars coming from opposite side.',
                          (0, 0, 0), 10)
                msg_2_scr('Press C to play, P to pause or Q to quit.',
                          (0, 0, 0), 180)
                pygame.display.update()
                clock.tick(15)

        def text_objects(text, color, size):
            if size == 'small':
                textSurface = smallfont.render(text, True, color)
            elif size == 'medium':
                textSurface = medfont.render(text, True, color)
            elif size == 'large':
                textSurface = largefont.render(text, True, color)
                
            return textSurface, textSurface.get_rect()

        def msg_2_scr(msg, clr, y_displace=0, size='small'):
            textSurf, textRect = text_objects(msg, clr, size)
            textRect.center = (display_width/2), (display_height/2) + y_displace
            x.blit(textSurf, textRect)

        pygame.mixer.music.load('car.mp3')
        def gameLoop():
            pygame.mixer.music.play(-1)
            car_width = 100
            var_y = car_width*2**(-1)
            horx = 400
            hory = 500
            scr = 0
            gameExit=False
            gameOver=False
            while not gameExit:

                if gameOver == True:
                    msg_2_scr('Game over', (255, 0,0), -50, size='large')
                    msg_2_scr('Press C to play again or Q to quit', (0, 0, 0), 50, size='medium')
                    pygame.display.update()
                while gameOver==True:

                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            gameExit=True
                            gameOver=False
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_q:
                                gameExit=True
                                gameOver=False
                                scr -=1
                            elif event.key==pygame.K_c:
                                pygame.mixer.music.load('car.mp3')
                                gameLoop()
                cx, cy = randCarGen()
                while cy < display_height:
                    x.fill((49, 79, 79))
                    cy += gameLevel
                    x.blit(redImg, (cx, cy))
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            gameExit=True
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_LEFT:
                                horx-=(car_width)
                            elif event.key==pygame.K_RIGHT:
                                horx+=(car_width)
                            elif event.key==pygame.K_ESCAPE:
                                gameExit=True
                            elif event.key==pygame.K_p:
                                pause()
                    if horx>=display_width-100 or horx<100:
                        pygame.mixer.music.stop()
                        gameOver=True
                    if ((cy+car_width) >= hory):
                        
                        if (cx > horx and cx < (horx + car_width)) or ((cx + car_width) > horx and cx < horx):
                            pygame.mixer.music.stop()
                            gameOver = True
                    x.blit(yellImg, (horx, hory))
                    score(scr)
                    pygame.display.update()
                else:
                    scr += 1
                clock.tick(FPS)

            pygame.quit()
            quit()

        game_intro()
        gameLoop()
    root = Tk()
    root.title('Car Crash!!')
    img = ImageTk.PhotoImage(Image.open('logo.png'))
    panel = Label(root, image = img)
    panel.pack(side = 'bottom', fill = 'both', expand = 'yes')
    l = Label(root, text = 'Choose game level')
    l.pack()
    rvar = IntVar()
    def levelEasy():
        global level
        level = 2
    def levelHard():
        global level
        pass
    def Help():
        f = open('help.txt', 'r')
        s = f.read()
        f.close()
        helpRoot = Tk()
        L = Label(helpRoot, text = s)
        L.pack()
        helpRoot.resizable(height = FALSE, width = FALSE)
        helpRoot.mainloop()
    c1 = Radiobutton(root, text = 'Easy', variable = rvar, value = 1, command = levelEasy)
    c1.pack()
    c2 = Radiobutton(root, text = 'Hard', variable = rvar, value = 2, command = levelHard)
    c2.pack()
    confirmButton = Button(root, text = 'Play!', command = start, width = 7)
    confirmButton.pack(pady = 5)
    helpButton = Button(root, text = 'Help', command = Help, width = 7)
    helpButton.pack(pady = 5)
    root.resizable(height = FALSE, width = FALSE)
    root.mainloop()
#------------------------------------------------------------
#Authentication check
f = open('MACFILE.dat', 'rb')
fw = open('temp.dat', 'wb')
try:
    while True:
        d = {}
        d = pickle.load(f)
        if d == {}:
            print 'Master permission required!!!'
            msterKey = raw_input('Enter master key: ')
            if msterKey == hex(mac).split('x')[1]:
                d.update({mac:'Registered'})
                pickle.dump(d, fw)
                tkMessageBox.showinfo('Alert', 'You are now registered, open game again, you will now be able to play it.')
            else:
                pickle.dump(d, fw)
        else:
            pickle.dump(d, fw)
            game()
except:
    f.close()
fw.close()
os.remove('MACFILE.dat')
os.rename('temp.dat', 'MACFILE.dat')

    
