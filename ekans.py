import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self, snake, obstacles):
        self.snake = snake
        self.obstacles = obstacles
        self.randomize()

    def randomize(self):
        all_positions = [Vector2(x, y) for x in range(cell_number) for y in range(cell_number)]
        available_positions = [pos for pos in all_positions if pos not in self.snake.body and pos not in self.obstacles]
        self.pos = random.choice(available_positions)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y *cell_size, cell_size, cell_size) #x,y,w,h
        screen.blit(apple, fruit_rect)

class SNAKE:
    def __init__(self):
        self.body = []
        maxcoord = 12
        mincoord = 6
        for x in range(maxcoord, mincoord - 1, -1):
            if x % 2 == 1:
                for y in range(maxcoord, mincoord -1, -1):
                    self.body.append(Vector2(x,y))
            else:
                for y in range(mincoord, maxcoord + 1) :
                    self.body.append(Vector2(x,y))
        self.direction = Vector2(1,0)
        self.del_block = False
        self.tail_pos = None

        self.head_up = pygame.image.load('graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('graphics/head_left.png').convert_alpha()
		
        self.tail_up = pygame.image.load('graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('graphics/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('sound/crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block

                # Wrap-around handling
                if previous_block.x == cell_number - 1: previous_block.x = -1
                elif previous_block.x == -(cell_number - 1): previous_block.x = 1
                if previous_block.y == cell_number - 1: previous_block.y = -1
                elif previous_block.y == -(cell_number - 1): previous_block.y = 1
                if next_block.x == cell_number - 1: next_block.x = -1
                elif next_block.x == -(cell_number - 1): next_block.x = 1
                if next_block.y == cell_number - 1: next_block.y = -1
                elif next_block.y == -(cell_number - 1): next_block.y = 1

                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    else:
                        screen.blit(self.body_br, block_rect)

        # Wrap-around handling
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation.x == cell_number - 1: head_relation.x = -1
        elif head_relation.x == -(cell_number - 1): head_relation.x = 1
        if head_relation.y == cell_number - 1: head_relation.y = -1
        elif head_relation.y == -(cell_number - 1): head_relation.y = 1

        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation.x == cell_number - 1: tail_relation.x = -1
        elif tail_relation.x == -(cell_number - 1): tail_relation.x = 1
        if tail_relation.y == cell_number - 1: tail_relation.y = -1
        elif tail_relation.y == -(cell_number - 1): tail_relation.y = 1

        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down


    def move_snake(self):
        if self.del_block == True:
            body_copy = self.body[:-2]
            self.del_block = False
        else:
            body_copy = self.body[:-1]
        self.tail_pos = self.body[-1]
        try:
            body_copy.insert(0,body_copy[0] + self.direction)
        except:
            print("YOU WON!")
            sys.exit(0)
        self.body = [Vector2(block.x % cell_number, block.y % cell_number) for block in body_copy]

    def remove_block(self):
        self.del_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.obstacles = []
        self.fruit = FRUIT(self.snake, self.obstacles)

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_obstacles()
        self.draw_score()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.remove_block()
            self.obstacles.append(self.snake.tail_pos)
            self.snake.play_crunch_sound()
        
    def check_fail(self):
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

        for obstacle in self.obstacles:
            if obstacle == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        grass_color = (167, 209, 61)

        for row in range(cell_number):
            for col in range(cell_number):
                if (row + col) % 2 == 0:
                    grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_obstacles(self):
        obstacle_color = (139, 69, 19)
        for obstacle in self.obstacles:
            obstacle_rect = pygame.Rect(obstacle.x * cell_size, obstacle.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, obstacle_color, obstacle_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 1)
        score_surface = game_font.render(score_text, True, (56,73,12))
        score_x = cell_size * cell_number - 60
        score_y = cell_size * cell_number - 40
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_rect)

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.display.set_caption("Snake")
cell_size = 40
cell_number  = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size)) #bg

clock = pygame.time.Clock()
apple = pygame.image.load('graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('./font/PoetsenOne-Regular.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_s and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_a and main_game.snake.direction.x != 1: 
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_d and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)

    screen.fill((175,215,70))
    main_game.draw_elements() 
    pygame.display.update()
    clock.tick(60) #setting framerate