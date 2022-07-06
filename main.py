import pygame

WIN_WIDTH = 500
WIN_HEIGHT = 500
BG_COLOR = (20, 92, 68)
WHITE = (255, 255, 255)

class Box:
  def __init__(self, row, column, height, width):
    self.r = row 
    self.c = column 
    self.h = height
    self.w = width
  
  def draw(self, surf):
    rect = pygame.Rect(self.c * self.w, self.r * self.h, self.w, self.h)
    pygame.draw.rect(surf, (0,0,0), rect, 1)



def make_grid(rows, cols):
  width = WIN_WIDTH / cols 
  height = WIN_HEIGHT / rows 
  boxlist = []
  for r in range(rows):
    column = []
    for c in range(cols):
      box = Box(r, c, height, width)
      column.append(box)
    boxlist.append(column)
  return boxlist

def draw_grid(grid, surf):
  for line in grid:
    for box in line:
      box.draw(surf)

def main():
  screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
  pygame.display.set_caption('Snake')
  screen.fill(BG_COLOR)
  pygame.display.flip()
  grid = make_grid(25, 25)
  running = True
  while running:
    screen.fill(BG_COLOR)
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = False
    draw_grid(grid, screen)
    pygame.display.flip()
  pygame.quit()

if __name__ == '__main__':
  main()