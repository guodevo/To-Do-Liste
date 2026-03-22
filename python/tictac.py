import pygame
from sys import exit

width = 600
height = 600

pygame.init()

pygame.display.set_caption("Trying out new things ")

window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

player = pygame.Rect(50, 50, 50, 50)

def draw_display():
   window.fill('blue')
   pygame.rect(('blue'), 50, 50)


while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()
   
   pygame.display.update()
   clock.tick(120)
   window.fill("blue")
        


