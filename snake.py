import pygame
import random
from enum import Enum
from collections import namedtuple

class Direction(Enum):
    RIGHT = 1
    LEFT= 2
    UP= 3
    DOWN = 4
    
Point = namedtuple('point','x, y')
blockSize = 20
speed = 30
color_1 = (255, 0, 0)   # red
color_2 = (255, 255, 255)   # white
color_3 = (0, 0, 0)   # black
color_4 = (161, 252, 223) #green
color_5 = (127, 216, 190) #green1
    
pygame.init()
font = pygame.font.Font('Merathus.ttf', 25)
# font = pygame.font.Font('Thunderous One Free.ttf', 25)

# font = pygame.font.SysFont('arial', 25)


class snakeGame:
    def __init__(self, w =720, h =600):
        self.w = w
        self.h = h
        
        # display
        self.display = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption("SNAKE GAME")
        self.clock = pygame.time.Clock()
        
        # gameplay state
        self.direction = Direction.RIGHT
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head,
                      Point(self.head.x-blockSize, self.head.y),
                      Point(self.head.x-(2*blockSize),self.head.y)]
        
        self.score = 0
        self.food = None
        self.foodPlacement()
        
    def foodPlacement(self):
        x = random.randint(0, (self.w - blockSize)//blockSize)* blockSize
        y = random.randint(0, (self.h - blockSize)//blockSize)* blockSize
        self.food = Point(x, y)
        if self.food in self.snake:
            self.foodPlacement()
            

        
                
    def play_step(self):
        # user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN        
            
            # movement
            self.move(self.direction)
            self.snake.insert(0, self.head) 
            
            
            # new food
            if self.head == self.food:
                self.score +=1
                self.foodPlacement()
            else:
                self.snake.pop()
            
            
            # update ui and clock
            self.update_ui()
            self.clock.tick(speed)
            
            
            # check and return game over and score
            game_over = False 
            if self.collide():
                game_over = True
                return game_over, self.score



    def collide(self):
     # hits boundary
        if self .head.x > self.w - blockSize or self.head.x < 0 or self.head.y > self.h - blockSize or self.head.y < 0:
            return True
        
    
    
     # hits itself
        if self.head in self.head[1:]:
            return True
            
    
    
    
    def update_ui(self):
       self.display.fill(color_3)
        
       for pt in self.snake:
            pygame.draw.rect(self.display, color_4, pygame.Rect(pt.x, pt.y, blockSize, blockSize))
            pygame.draw.rect(self.display, color_5, pygame.Rect(pt.x +4, pt.y +4, 12, 12))
            
       pygame.draw.rect(self.display, color_1, pygame.Rect(self.food.x, self.food.y,blockSize,blockSize))
        
       text = font.render("Score: "+ str(self.score),True,color_2)
       self.display.blit(text, [0, 0])
       pygame.display.flip()
        
        
         
    def move(self, direction):
         x = self.head.x
         y = self.head.y
         if direction == Direction.RIGHT:
            x += blockSize
         elif direction == Direction.LEFT:
            x -= blockSize
         elif direction == Direction.UP:
            y -= blockSize
         elif direction == Direction.DOWN:
            y += blockSize
         
         self.head = Point(x, y)
        
    
    
if __name__ =='__main__':
    game = snakeGame()
    
    # game loop
    while True:
        game_over, score = game.play_step()
        
        if game_over == True:
            break
        
    print("Final Score",score)

pygame.quit()
