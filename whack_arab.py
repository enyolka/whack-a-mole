import pygame, random
pygame.init()

class Game:

    def __init__(self):
        self.display_width = 600
        self.display_height = 800

        self.bg = pygame.image.load('tlo2.png')
        self.gameDisplay = pygame.display.set_mode((self.display_width,self.display_height))
        self.ibg = pygame.image.load('intro_bg.png')
        self.igameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        self.ebg = pygame.image.load('end_bg.png')
        self.egameDisplay = pygame.display.set_mode((self.display_width, self.display_height))

        pygame.display.set_caption("Whack a mole")

        self.rab_width = 41
        self.rab_height = 50
        self.rabbit = pygame.image.load('rab.png')

        self.hole_position = ((130,400),(430,400),(280,450),(80,500),(480,500),(280,550),(130,600),(430,600))

        self.score = 0
        self.counter = 0
        self.speed = 1000
        self.start_time = 0
        self.play_time = 60

        self.intro = True
        self.run = True
        self.end = True

    def update_score(self):

        self.font = pygame.font.SysFont(None,25)
        self.text_score = self.font.render("Score:" + str(self.score),True,(100,100,100))
        self.text_time = self.font.render("Time: " + str(self.timer), True,(100,100,200))
        self.gameDisplay.blit(self.text_score,(50,50))
        self.gameDisplay.blit(self.text_time, (50, 25))

    def redrawDisplay(self):

        self.gameDisplay.blit(self.bg,(0,0))
        self.gameDisplay.blit(self.rabbit, (self.rand_xy))
        self.update_score()
        pygame.display.update()

    def text_objects(self):

        self.textSurface = self.font.render(self.text_score, True, (0,0,0))
        return self.textSurface, self.textSurface.get_rect()

    def time(self):

        self.timer = pygame.time.get_ticks() - self.start_time - 2000
        self.timer = self.timer/1000
        self.timer = int(self.play_time - self.timer)

    def game_loop(self):

        self.gameDisplay.blit(self.bg, (0, 0))
        self.rand_xy = random.choice(self.hole_position)
        self.start_time = pygame.time.get_ticks()

        while self.run:
            pygame.time.delay(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
                        self.end_screen()
                if self.timer < 1:
                    self.run = False
                    self.end_screen()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mx, self.my = pygame.mouse.get_pos()
                    if (self.rand_xy[0] + self.rab_width > self.mx > self.rand_xy[0]) and (self.rand_xy[1] + self.rab_height > self.my > self.rand_xy[0]):
                        self.score += 10
                    else:
                        self.score -= 5

            self.counter += 1
            self.time()

            if self.score < 50:
                self.speed = 1000
            elif 50 <= self.score < 150:
                self.speed = 900
            elif 150 <= self.score < 300:
                self.speed = 850
            else:
                self.speed = 750

            if self.counter == self.speed:
                self.rand_xy = random.choice(self.hole_position)
                self.redrawDisplay()
                self.counter = 0

    def game_intro(self):

        self.gameDisplay.blit(self.ibg, (0, 0))
        pygame.display.update()

        while self.intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.intro = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_loop()

    def end_screen(self):

        self.gameDisplay.blit(self.ebg, (0, 0))
        self.font = pygame.font.SysFont(None, 75)
        self.text_score = self.font.render("Score: " + str(self.score), True, (55, 97, 38))
        self.gameDisplay.blit(self.text_score, (185, 400))
        pygame.display.update()

        self.end = True
        while self.end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.run = True
                        self.score = 0
                        self.game_loop()

my_game = Game()
my_game.game_intro()
pygame.quit()
