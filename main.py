import pygame

import random



SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400

MOVEMENT_SPEED = 5

FONT_SIZE = 72



pygame.init()


background_image = pygame.transform.scale(pygame.image.load("bg1.jpeg"), (SCREEN_WIDTH, SCREEN_HEIGHT))



font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
     self.rect.x = max(
        min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
     self.rect.y = max(
        min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()


spritel = Sprite(pygame.Color('black'), 20, 30)
spritel.rect.x, spritel.rect.y = random.randint(0, SCREEN_WIDTH - spritel.rect.width), random.randint(0, SCREEN_HEIGHT - spritel.rect.height)
all_sprites.add(spritel)

sprite2 = Sprite(pygame.Color('red'), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, SCREEN_WIDTH - sprite2.rect.width), random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)
running, won = True, False

clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED

        spritel.move(x_change, y_change)

        if spritel.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2, (SCREEN_HEIGHT - win_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()



