import pygame
import random as rnd

pygame.init()

fps = 25
clock = pygame.time.Clock()
size = 400, 300
scr = pygame.display.set_mode(size)
balloons = []
v = 100
rect_scr = pygame.Rect(-10, -10, 420, 300)
scr2 = pygame.Surface(scr.get_size())

running = True
while running:
    scr.blit(scr2, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            color = pygame.Color(rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
            rect = pygame.Rect(pos[0] - 10, pos[1] - 10, 20, 20)
            balloons.append((color, rect))

    for b in balloons:
        pygame.draw.ellipse(scr, b[0], b[1], 0)
    pygame.display.flip()
    for b in balloons:
        if rect_scr.contains(b[1]):
            b[1].move_ip(0, int(100 / fps))
        else:
            pygame.draw.ellipse(scr2, b[0], b[1], 0)
            del balloons[balloons.index(b)]
    clock.tick(fps)

pygame.quit()
