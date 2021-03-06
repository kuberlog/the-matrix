import sys, pygame
import time

pygame.init()
pygame.font.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0


ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

class View:
    def __init__(self, matrix):
        self.pixels_per_m = 20
        right_menu_width = 180
        bottom_menu_height = 160


        screen_size = ( matrix.width * self.pixels_per_m + right_menu_width, 
                matrix.height * self.pixels_per_m + bottom_menu_height)

        self.screen = pygame.display.set_mode(screen_size)
        self.matrix = matrix
        self.screen.fill(black)
        self.matrix.draw_background(self.screen, self.pixels_per_m)

    def step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        self.matrix.draw(self.screen, self.pixels_per_m)
        pygame.display.flip()

class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.contents = []
        for i in range(height):
            self.contents.append([])
            for i in range(width):
                self.contents.append(None)
        
    def draw_background(self, screen, pixels_per_m):
        for y in range(self.height):
            pygame.draw.line(screen, 111, (0, y*pixels_per_m),
                             (self.width*pixels_per_m, y*pixels_per_m), 1)
        for x in range(self.width):
            pygame.draw.line(screen, 111, (x*pixels_per_m, 0),
                             (x*pixels_per_m, self.height*pixels_per_m), 1)

    def draw(self, screen, pixels_per_unit):
        pass


matrix = Matrix(40,40)
view = View(matrix)
while 1:
    view.step()
    time.sleep(0.05)

