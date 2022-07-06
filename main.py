import pygame

def main():
  background_colour = (20, 92, 68)
  screen = pygame.display.set_mode((600, 400))
  pygame.display.set_caption('Snake')
  screen.fill(background_colour)
  pygame.display.flip()
  running = True
  while running:
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = False
  pygame.quit()

if __name__ == '__main__':
  main()