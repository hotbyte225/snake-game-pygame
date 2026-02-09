import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True


class Snake:
    def __init__(self):
        self.body = [[180,180]]
        self.color = "Green"
        self.width = 20
        self.height = 20
        self.dir_x = 0
        self.dir_y = 0
        
    def draw(self):
        for body in self.body:
            pygame.draw.rect(screen,self.color, pygame.Rect(body[0], body[1], self.width,self.height))
    def control(self, key):
        if game_over.game_over == False:
            if key == pygame.K_UP and self.dir_y == 0:
                    self.dir_x, self.dir_y = 0, -20
            elif key == pygame.K_DOWN and self.dir_y == 0:
                self.dir_x, self.dir_y = 0, 20
            elif key == pygame.K_LEFT and self.dir_x == 0:
                self.dir_x, self.dir_y = -20, 0
            elif key == pygame.K_RIGHT and self.dir_x == 0:
                self.dir_x, self.dir_y = 20, 0
        if key == pygame.K_r:
            game_over.game_over = False
            snake.restart()
    def move(self):
        if game_over.game_over == False:
            if self.dir_x == 0 and self.dir_y == 0:
                return
            head_x, head_y = self.body[-1]
            if head_x > SCREEN_WIDTH:
                head_x = -20
            elif head_x < 0:
                head_x = SCREEN_WIDTH - 20
            if head_y > SCREEN_HEIGHT:
                head_y = -20
            elif head_y < 0:
                head_y = SCREEN_HEIGHT - 20
            new_head = [head_x + self.dir_x, head_y + self.dir_y]
            self.body.append(new_head)
            self.body.pop(0)
        
    def head_rect(self):
        head = self.body[-1]
        return pygame.Rect(head[0], head[1], self.width, self.height)
    def hit_itself(self):
        head = self.body[-1]
        return head in self.body[:-1]
    def restart(self):
        self.body = [[160,180],[180,180]]
        score.score = 0
        self.dir_x = 0
        self.dir_y = 0
class Apple:
    def __init__(self):
        self.color = "Red"
        self.width = 20
        self.height = 20
        self.x = random.randrange(0, 400, 20)
        self.y = random.randrange(0, 400, 20)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def respawn(self):
        self.x = random.randrange(0, 400, 20)
        self.y = random.randrange(0, 400, 20)
        self.rect.topleft = (self.x, self.y)
        
class Score:
    def __init__(self):
        self.score = 0
        self.color = "White"
        self.font_size = 20
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)
        
    def draw(self):
        self.text = self.font.render(f'Score: {self.score}', True, self.color)
        screen.blit(self.text, (0, 0))


class GameOver:
    def __init__(self):
        self.game_over = False
        self.color = "Red"
        self.font_size = 15
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)
    def draw(self):
        self.game_over = True
        self.text = self.font.render(f'Game Over, To restart the  game press "R" key', True, self.color)
        screen.blit(self.text, (SCREEN_WIDTH /2 - 150 , SCREEN_HEIGHT / 2))
snake = Snake()
apple = Apple()
score = Score()
game_over = GameOver()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            snake.control(event.key)
    screen.fill("black")
    
    snake.move()
    if snake.hit_itself():
        game_over.draw()
    snake.draw()

    apple.draw()
   
    snake_head_rect = snake.head_rect()
    
    
    

    if snake_head_rect.colliderect(apple.rect):
        apple.respawn()
        snake.body.insert(0, snake.body[0])
        score.score += 1  
        
    
    score.draw()

    pygame.display.flip()

    clock.tick(10) 

pygame.quit()