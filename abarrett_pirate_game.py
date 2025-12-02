import pygame                
import os

pygame.init()


W, H = 800, 500
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pirate Game")


background = pygame.Surface(screen.get_size())
background.fill((180, 219, 210)) 


class Pirate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


        if os.path.exists("Pirate2.png"):
            self.image = pygame.image.load("Pirate2.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (80, 80))
        else:
            print("Pirate2.png not found — using placeholder box.")
            self.image = pygame.Surface((80, 80))
            self.image.fill((80, 180, 80))


        self.rect = self.image.get_rect()
        self.rect.centerx = W // 2
        self.rect.centery = H // 2


        self.dx = 5
        self.dy = 3

    def update(self):

        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.right > W:
            self.rect.left = 0
        if self.rect.bottom > H:
            self.rect.top = 0


def main():
    pirate = Pirate()
    allSprites = pygame.sprite.Group(pirate)


    clock = pygame.time.Clock()
    keepGoing = True


    while keepGoing:
        clock.tick(30)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                keepGoing = False


        screen.blit(background, (0, 0))
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()



if __name__ == "__main__":
    main()
    pygame.quit()