import pygame
import time
import random

FPS = 60
WIN_WIDTH = 620
WIN_HEIGHT = 480
BOX_SIZE = 20
BG_COLOR = (20, 92, 68)
shift = 10
WHITE = (BG_COLOR[0]+shift, BG_COLOR[1]+shift, BG_COLOR[2]+shift)
shift = 35
SNAKE_COLOR = (BG_COLOR[0]+shift, BG_COLOR[1]+shift, BG_COLOR[2]+shift)
FOOD_COLOR = (255, 0, 0)

class Box:
  def __init__(self, row, column, size = BOX_SIZE, color = WHITE, width = 1):
    self.r = row 
    self.c = column 
    self.s = size 
    self.color = color 
    self.width = width 
  
  def _get_rect(self):
    return pygame.Rect(self.c * self.s, self.r * self.s, self.s, self.s)

  def draw(self, surf):
    pygame.draw.rect(surf, self.color, self._get_rect(), self.width)

class Food(Box):
  def __init__(self):
    row, column = self._get_rand_pos()
    super().__init__(row, column, BOX_SIZE, FOOD_COLOR, 0)

  def _get_rand_pos(self):
    return random.randint(1, WIN_HEIGHT // BOX_SIZE), random.randint(1, WIN_WIDTH // BOX_SIZE)
  
  def hitbox(self, snake):
    if self.r == snake[0][0] and self.c == snake[0][1]:
       self.r, self.c = self._get_rand_pos()

class Snake:
  def __init__(self, head_row, head_col):
    self.b = [[head_row, head_col]]
    self.s = BOX_SIZE 
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
  
  def get_body(self):
    return self.b 
  
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
    
  def move(self, key):
    if key == pygame.K_UP or key == pygame.K_w:
      self.vy = -1
      self.vx = 0
    elif key == pygame.K_DOWN or key == pygame.K_s:
      self.vy = 1
      self.vx = 0
    elif key == pygame.K_LEFT or key == pygame.K_a:
      self.vx = -1
      self.vy = 0 
    elif key == pygame.K_RIGHT or key == pygame.K_d:
      self.vx = 1
      self.vy = 0


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
  snake = Snake(10, 10)
  food = Food()
  clock = pygame.time.Clock()
  running = True
  while running:
    dt = clock.tick(FPS)
    screen.fill(BG_COLOR)
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_ESCAPE:
          running = False 
        snake.move(event.key)
    food.hitbox(snake.get_body())
    snake.update()
    food.draw(screen)
    draw_grid(grid, screen)
    snake.draw(screen)
    pygame.display.flip()
  pygame.quit()

if __name__ == '__main__':
  main()