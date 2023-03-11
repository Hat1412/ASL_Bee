import pygame
from string import ascii_uppercase

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("ASL_Bee")
window = pygame.display.set_mode((500, 500))
font = pygame.font.SysFont("Times New Roman", 36)
font2 = pygame.font.SysFont("Times New Roman", 12)
time_elapsed_since_last_action = 0
color_index = 0
delay = 1
run = True
d = {"":""}

for i in list(ascii_uppercase):
    img = pygame.image.load(fr"{i}.png")
    d[i] = img


class Box:
    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.word = "A"
        self.counter = 0

    def type(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                if len(self.word) > 0:
                    self.word = self.word[:-1]

            else:
                try:
                    if ord(event.unicode.upper()) in range(65, 91):
                        self.word += event.unicode.upper()
                except TypeError:
                    pass

    def slideshow(self):
        self.counter += 1
        if self.counter >= len(self.word):
            self.counter = 0

    def update(self):
        center_img_x = 500 / 2 - 150
        center_img_y = 500 / 2 - 150
        pygame.draw.rect(self.window, (255, 0, 0), pygame.Rect(0, 0, 500, 50))
        txt = font.render(self.word, True, (0, 0, 0))

        self.window.blit(txt, (self.x, self.y))

        try:
            self.window.blit(d[self.word[self.counter]], (center_img_x, center_img_y))
        except IndexError:
            pass

class Scale:
    def __init__(self,window):
        self.window = window

    def update(self):
        pygame.draw.line(window, (65,65,65),(10,480),(480,480),3)
        self.x = 10

        l = [(0,0,255)] * 5
        l[color_index] = (0,255,0)

        txt = font2.render("0.25 sec",True,(0,0,0))
        self.window.blit(txt, (10,460))
        self.b0 = pygame.draw.circle(self.window,l[0],(10,480),7)

        txt = font2.render("0.5 sec",True,(0,0,0))
        self.window.blit(txt, (127.5,460))
        self.b1 = pygame.draw.circle(self.window,l[1],(127.5,480),7)

        txt = font2.render("1 sec",True,(0,0,0))
        self.window.blit(txt, (245.5,460))
        self.b2 = pygame.draw.circle(self.window,l[2],(245.5,480),7)

        txt = font2.render("2 sec",True,(0,0,0))
        self.window.blit(txt, (362.5,460))
        self.b3 = pygame.draw.circle(self.window,l[3],(362.5,480),7)

        txt = font2.render("3 sec",True,(0,0,0))
        self.window.blit(txt, (480,460))
        self.b4 = pygame.draw.circle(self.window,l[4],(480,480),7)




    def chk(self,event):
        global delay,color_index

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()

            if self.b0.collidepoint(mousepos[0],mousepos[1]):
                delay = 1/4
                color_index = 0
            
            if self.b1.collidepoint(mousepos[0],mousepos[1]):
                delay = 1/2
                color_index = 1
            
            if self.b2.collidepoint(mousepos[0],mousepos[1]):
                delay = 1
                color_index = 2
            
            if self.b3.collidepoint(mousepos[0],mousepos[1]):
                delay = 2
                color_index = 3
            
            if self.b4.collidepoint(mousepos[0],mousepos[1]):
                delay = 3
                color_index = 4
            
a = Box(window, 200, 10)
b = Scale(window)

while run:
    window.fill("#1677c5")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

        a.type(event)
        b.chk(event)

    a.update()
    b.update()

    dt = clock.tick(30)

    time_elapsed_since_last_action += dt

    if time_elapsed_since_last_action >= delay * 1000:
        a.slideshow()
        time_elapsed_since_last_action = 0


    pygame.display.flip()


quit()