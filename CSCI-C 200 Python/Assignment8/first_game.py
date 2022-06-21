import pygame
import sys
import random as rn

 
DARKGREEN = (0,55,0)
BLACK = ( 0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
RED =   (255,0,0)
YELLOW = (255,255,0)


class Rectangle:

    def __init__(self,color,loc):
        self.loc = loc
        self.color = color

    def my_draw(self,screen):
        pygame.draw.rect(screen, self.color, self.loc)
    
    def my_move(self,xoffset,yoffset):
        self.loc = [self.loc[0]+xoffset,self.loc[1]+yoffset] + self.loc[2:]#

    def my_color(self, newColor):
        self.color = newColor
  
       




if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a8.py`. Feel free to add print statements. 
    """
    pygame.init()
    size = [300, 300]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("C200 CHANGE")

    r = Rectangle(RED, [0, 0, 20, 20])

    while True:
        
        pygame.time.wait(40)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
    
        screen.fill(WHITE)
        
        r.my_draw(screen)
        
        if r.loc[0] > 280:
            xd = -rn.randint(1,3)
            newColor = DARKGREEN
        if r.loc[1] > 280:
            yd = -rn.randint(1,3)
            newColor = BLUE
        if r.loc[0] < 10:
            xd = rn.randint(1,3)
            newColor = RED
        if r.loc[1] < 10:
            yd = rn.randint(1,3)
            newColor = YELLOW
        r.my_color(newColor)
        r.my_move(xd,yd)

        pygame.display.flip()