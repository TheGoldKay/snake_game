import pygame
import time

FPS = 60
WIN_WIDTH = 620
WIN_HEIGHT = 480
BOX_SIZE = 20
BG_COLOR = (20, 92, 68)
WHITE = (150, 150, 150)
SNAKE_COLOR = WHITE

class Box:
  def __init__(self, row, column, size):
    self.r = row 
    self.c = column 
    self.s = size 
  
  def draw(self, surf):
    rect = pygame.Rect(self.c * self.s, self.r * self.s, self.s, self.s)
    pygame.draw.rect(surf, WHITE, rect, 1)

class Snake:
  def __init__(self, head_row, head_col, size):
    self.b = [[head_row, head_col]]
    self.s = size 
    self.timer = 0.2
    self.clock = time.time()
    self.vx = -1
    self.vy = 0
    self.c = WIN_WIDTH // BOX_SIZE
    self.r = WIN_HEIGHT // BOX_SIZE 

  def draw(self, surf):
    for box in self.b:
      rect = pygame.Rect(box[1] * self.s, box[0] * self.s, self.s, self.s)
      pygame.draw.rect(surf, SNAKE_COLOR, rect)  
  
  def update(self):
    if time.time() - self.clock > self.timer:
      self.b[0][0] += self.vy 
      self.b[0][1] += self.vx 
      if self.b[0][0] > self.r:
        self.b[0][0] = 0
      elif self.b[0][0] < 0:
        self.b[0][0] = self.r 
      if self.b[0][1] > self.c:
        self.b[0][1] = 0
      elif self.b[0][1] < 0:
        self.b[0][1] = self.c 
      for i in range(len(self.b) - 1, 1):
        self.b[i] = self.b[i - 1]
      self.clock = time.time()


def make_grid(box_size):
  cols = WIN_WIDTH // box_size
  rows = WIN_HEIGHT // box_size 
  boxlist = []
  for r in range(rows):
    column = []
    for c in range(cols):
      box = Box(r, c, box_size)
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
  grid = make_grid(BOX_SIZE)
  snake = Snake(10, 10, BOX_SIZE)
  clock = pygame.time.Clock()
  running = True
  while running:
    dt = clock.tick(FPS)
    print(dt)
    screen.fill(BG_COLOR)
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = False
    snake.update()
    draw_grid(grid, screen)
    snake.draw(screen)
    pygame.display.flip()
  pygame.quit()

if __name__ == '__main__':
  main()