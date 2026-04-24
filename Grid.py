import pygame as py
from random import randint
from Player import Player, Obstacle
py.mixer.init()
#pudzian img: https://pudzian.pl/biografia/
#in this script we will generate n x n grid on the screen
# our player can only move within these cells in the grid
cell_w, cell_h = 60, 60
row, col = 9, 9
screen_w = col * cell_w
screen_h = row * cell_h
panel_w = 3*cell_w
panel_h = screen_h
#generating random value of 0 and 1 in the grid list
#which decides where we draw o stacles
#we choose our probabilities to be 70 - 30 against obstacle
grid = [[randint(0,4) for i in range(col)] for j in range(row)]
grid[0][0], grid[0][1], grid[1][0] = 1, 1, 1
for r in grid:
    print(r)

dig = py.mixer.Sound("C:\\Users\\08Solec\\PreDP2-AntoniP\\GameProject\\Villager_deny1.oga")
char = py.image.load("C:\\Users\\08Solec\\PreDP2-AntoniP\\MyGame\\MyGame1\\Image2.png")
char = py.transform.scale(char, (60, 60))
pudzian = py.image.load("C:\\Users\\08Solec\\PreDP2-AntoniP\\MyGame\\MyGame1\\pudzian.png")
pudzian = py.transform.scale(pudzian, (60,60))
bg = py.image.load("C:\\Users\\08Solec\\PreDP2-AntoniP\\MyGame\\MyGame1\\rikitiki.png")
bg = py.transform.scale(bg, (screen_w, screen_h))
coin_sound = py.mixer.Sound("C:\\Users\\08Solec\\PreDP2-AntoniP\\GameProject\\Mario_Coin.ogg")
coin_image = py.image.load("C:\\Users\\08Solec\\PreDP2-AntoniP\\MyGame\\MyGame1\\coin.png")
coin_image = py.transform.scale(coin_image, (60, 60))

p1 = Player(5, 5, 50, 50, char)
Player.speedX = cell_w
Player.speedY = cell_h
clock = py.time.Clock()
obstacleList = []

for r in range(row):
    for c in range(col):
        if grid[r][c] == 0:
            obstacleList.append(Obstacle(c*cell_w, r*cell_h, pudzian))

def drawGrid(grid:list[list]):
    index = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 0:
                obstacleList[index].draw(screen)
                index += 1
            elif grid[r][c] == 6:
                screen.blit(coin_image, (c*cell_w, r*cell_h))

                


coin = 0
def draw_panel(screen):
    font = py.font.SysFont(None, 30)
    py.draw.rect(screen, "#8BD0Ca", (screen_w, 0, panel_w, screen_h))
    textSurface = font.render(f"Coins: {coin}", True, "#df2323")
    screen.blit(textSurface, (screen_w + 20, 40))

def find(coin):
    r = p1.y // 60
    c = p1.x // 60
    if event.type == py.KEYDOWN:
        if event.key == py.K_SPACE and grid[r][c] == 3:
            coin += 1
            grid[r][c] = 6
            coin_sound.play()
    return coin

py.init()
screen = py.display.set_mode((screen_w + panel_w, screen_h))
py.display.set_caption("Generatiing random grid")

run = True
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        p1.move(screen, grid, event)
        coin = find(coin)
    clock.tick(15)
    screen.blit(bg, (0, 0))
    drawGrid(grid)
    draw_panel(screen)
    p1.draw(screen)


    py.display.flip()
py.quit