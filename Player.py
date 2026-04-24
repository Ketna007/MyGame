import pygame as py
from random import randint
py.mixer.init()
class Player:
    '''
    Player is a rectangle object of pygame
    So it must take x, y, width and height
    '''
    #the following variables are known as static or class variables
    speedX, speedY = randint(3, 6), randint(1, 4)
    dig = py.mixer.Sound("C:\\Users\\08Solec\\PreDP2-AntoniP\\GameProject\\Villager_deny1.oga")
    def __init__(self, x:int, y:int, w:int, h:int, img):
        #the following variables are called instamce objects because 
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.collide = False
        self.img = img

    def draw(self, screen):
        # py.draw.rect(screen, "#ffffff", (self.x, self.y, self.w, self.h))
        screen.blit(self.img, (self.x, self.y))
    
    def move(self, screen, grid, event):
        r = self.y // 60
        c = self.x // 60
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT and c - 1 >= 0 and grid[r][c-1] != 0:
                self.x -= 60
                Player.dig.play()
            if event.key == py.K_RIGHT and c + 1 < len(grid[0]) and grid[r][c+1] != 0:
                self.x += 60
                Player.dig.play()
            if event.key == py.K_UP and r - 1 >= 0 and grid[r-1][c] != 0:
                self.y -= 60
                Player.dig.play()
            if event.key == py.K_DOWN and r + 1 < len(grid) and grid[r+1][c] != 0:
                self.y += 60
                Player.dig.play()

    def collision(self,enemy):
        #enemy is also a player object
        #the collision happens is the difference between x cord and y cord is
        #less than width and height respectively
        if abs(self.x - enemy.x) <= self.w and abs(self.y - enemy.y) <= self.h:
            if self.collide == False:
                print("Collision")
                self.collide = True
        elif self.collide == True:
            self.collide = False

class Obstacle:
    def __init__(self, x:int, y:int, img):
        self.x = x
        self.y = y
        self.img = img
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
    