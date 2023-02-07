import pygame
import time
import random

GREY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Food:
    def __init__(self, x, y, block_size, parent_screen_width, parent_screen_height):
        self.x = x
        self.y = y
        self.block_size = block_size

        self.parent_screen_width = parent_screen_width
        self.parent_screen_height = parent_screen_height
    
    def draw(self, screen):
        food = pygame.Rect(self.x, self.y, self.block_size, self.block_size)
        pygame.draw.rect(screen, RED, food)

    def respawn(self, snake):
        snake_x = [body.x for body in snake.bodys]
        snake_x.insert(0, snake.head.x)
        snake_y = [body.y for body in snake.bodys]
        snake_y.insert(0, snake.head.y)
        snake_positions = list(zip(snake_x, snake_y))

        food_position = (random.randint(0, (self.parent_screen_width - self.block_size) // self.block_size) * self.block_size,
                         random.randint(0, (self.parent_screen_height - self.block_size) // self.block_size) * self.block_size)

        if food_position not in snake_positions:
            self.x = food_position[0]
            self.y = food_position[1]
        else:
            self.respawn(snake)

class Snake:
    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size

        self.head = pygame.Rect(self.x, self.y, self.block_size, self.block_size)
        self.bodys = [pygame.Rect(self.x - self.block_size, self.y, self.block_size, self.block_size),
                      pygame.Rect(self.x - 2 * self.block_size, self.y, self.block_size, self.block_size),
                      pygame.Rect(self.x - 3 * self.block_size, self.y, self.block_size, self.block_size)]
        self.direction = "right"

    def move_up(self):
        self.direction = "up"
        self.y -= self.block_size
        self._move()
    
    def move_down(self):
        self.direction = "down"
        self.y += self.block_size
        self._move()

    def move_left(self):
        self.direction = "left"
        self.x -= self.block_size
        self._move()

    def move_right(self):
        self.direction = "right"
        self.x += self.block_size
        self._move()

    def auto_move(self):
        if self.direction == "up":
            self.move_up()
        elif self.direction == "down":
            self.move_down()
        elif self.direction == "left":
            self.move_left()
        elif self.direction == "right":
            self.move_right()

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.head)
        for body in self.bodys:
            pygame.draw.rect(screen, GREEN, body)

    def _move(self):
        for i in range(len(self.bodys)-1, -1, -1):
            if i == 0:
                self.bodys[i].x, self.bodys[i].y = self.head.x, self.head.y
            else:
                self.bodys[i].x, self.bodys[i].y = self.bodys[i-1].x, self.bodys[i-1].y
        self.head = pygame.Rect(self.x, self.y, self.block_size, self.block_size)

class SnakeGame:
    def __init__(self, width, height, block_size):
        pygame.init()

        self.width = width
        self.height = height
        self.block_size = block_size

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.snake = Snake(self.width // 2, self.height // 2, self.block_size)

        self.food = Food(self.block_size, self.block_size, self.block_size, self.width, self.height)

        self.score = 0

    def run(self):
        gameover = False
        while not gameover:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gameover = True
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameover = True

                    if event.key == pygame.K_UP and self.snake.direction != "down":
                        self.snake.move_up()
                        if self._did_eat():
                            self._increase_score()
                            self._increase_snake_size()
                            self.food.respawn(self.snake)
                            
                    
                    if event.key == pygame.K_DOWN and self.snake.direction != "up":
                        self.snake.move_down()
                        if self._did_eat():
                            self._increase_score()
                            self._increase_snake_size()
                            self.food.respawn(self.snake)
                            

                    if event.key == pygame.K_LEFT and self.snake.direction != "right":
                        self.snake.move_left()
                        if self._did_eat():
                            self._increase_score()
                            self._increase_snake_size()
                            self.food.respawn(self.snake)
                            

                    if event.key == pygame.K_RIGHT and self.snake.direction != "left":
                        self.snake.move_right()
                        if self._did_eat():
                            self._increase_score()
                            self._increase_snake_size()
                            self.food.respawn(self.snake)
                            

            while True:
                self.snake.auto_move()
                self.screen.fill((0, 0, 0))
                self.snake.draw(self.screen)
                self.food.draw(self.screen)
                self._draw_grid(self.screen)
                self._draw_score(self.screen)
                pygame.display.update()
                time.sleep(0.05)

                if self._did_eat():
                    self._increase_score()
                    self._increase_snake_size()
                    self.food.respawn(self.snake)

                if self._is_colliding_with_itself():
                    gameover = True
                    break

                if self._is_colliding_with_wall():
                    gameover = True
                    break

                if pygame.event.peek(pygame.KEYDOWN):
                    break

    def _draw_grid(self, screen):
        for x in range(0, self.width, self.block_size):
            for y in range(0, self.height, self.block_size):
                grid = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(screen, GREY, grid, 1)

    def _did_eat(self):
        if self.snake.head.x == self.food.x and self.snake.head.y == self.food.y:
            return True
        else:
            return False

    def _increase_snake_size(self):
        self.snake.bodys.append(pygame.Rect(self.snake.head.x, self.snake.head.y, self.block_size, self.block_size))

    def _increase_score(self):
        self.score += 1

    def _draw_score(self, screen):
        font = pygame.font.SysFont("arial", 30)
        score = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score, (0, 0))

    def _is_colliding_with_itself(self):
        body_xs = [body.x for body in self.snake.bodys]
        body_ys = [body.y for body in self.snake.bodys]
        body_positions = list(zip(body_xs, body_ys))
        head_position = (self.snake.head.x, self.snake.head.y)

        if head_position not in body_positions[:-1]:
            return False
        else:
            return True

    def _is_colliding_with_wall(self):
        if 0 <= self.snake.head.x < self.width and 0 <= self.snake.head.y < self.height:
            return False
        else:
            return True

if __name__ == "__main__":
    game = SnakeGame(800, 800, 50)
    game.run()
    pygame.quit()