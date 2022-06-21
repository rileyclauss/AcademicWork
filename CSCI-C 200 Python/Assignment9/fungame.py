##############
# PROBLEM Six
##############

import pygame
import sys
import random as rn

pygame.init()
 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
RED =   (255,0,0)
YELLOW = (255,255,0)

class Rectangle(pygame.Rect):
    
    def __init__(self,color,loc, change = [0,0]):
        self.pre_loc = [0,0],0
        self.loc = loc
        self.color = color
        pygame.Rect.__init__(self,self.loc)
        self.change = change
        
    def my_draw(self,screen):
        pygame.draw.rect(screen, self.color, self.loc)
        
    def my_move(self,xoffset,yoffset):
        self.loc = [self.loc[0]+xoffset,self.loc[1]+yoffset] + self.loc[2:]
        self.pre_loc = self[0:2],0
        self.x = self.loc[0]
        self.y = self.loc[1]

    #INPUT another rectangle object
    #OUTPUT nothing, but toggles object's color between
    #black and blue when square collides with it
    def change_color(self,other):
        pass
  
       
size = [500, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Fun C200")

r = Rectangle(RED, [0, 0, 10, 10])
w = Rectangle(BLACK, [50,200,15,300])

if __name__ == "__main__":

    suspend = 0

    while True:
        
        
        r.change_color(w)
       
        pygame.time.wait(10)
        
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:
                print("key pressed")
                suspend = 1 - suspend
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
    
        screen.fill(WHITE)
        
        r.my_draw(screen)
        w.my_draw(screen)

        
        if r.loc[0] > 495:
            xd = -rn.randint(1,3)
        if r.loc[1] > 495:
            yd = -rn.randint(1,3)
        if r.loc[0] < 5:
            xd = rn.randint(1,3)
        if r.loc[1] < 5:
            yd = rn.randint(1,3)
        
        if not suspend:
            r.my_move(xd,yd)

        pygame.display.flip()
