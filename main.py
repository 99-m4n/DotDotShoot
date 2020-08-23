import sys, pygame, random

# init pygame
pygame.init()

# fps
clock = pygame.time.Clock()

# screen size
size = width, height = (1280, 720)
screen = pygame.display.set_mode(size)

# player
player_pos_x = width // 2
player_pos_y = height // 2
player_radius = 10
player_color = (255, 255, 255)
player_lvl = 1
player_weapon = 1
player_speed = 3

# Enemies ([pos_x, pos_y, radius, color, speed)
max_enemies = 5
num_enemies = 0

class Enemy:
    def __init__(lvl):
        side = random.randint(0, 4)  # (up, down, right, left)
        if side == 0:
            self.x = random.randint(0, width)
            self.y = -30
        elif side == 1:
            self.x = random.randint(0, width)
            self.y = height + 30
        elif side == 2:
            self.x = -30 
            self.y = random.randint(0, height)
        else:
            self.x = width + 30
            self.y = random.randint(0, height)

        enemy_num = random.randint(1, 

    def getEnemy(lvl: int = 1):
        if lvl == 1:
            rad = 15
            color = (255, 0, 0)
            speed = 2

        return [x, y, rad, color, speed]

# main loop
game = True
while game:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_pos_x > player_radius:
        player_pos_x -= player_speed
    if keys[pygame.K_d] and player_pos_x < width - player_radius:
        player_pos_x += player_speed
    if keys[pygame.K_w] and player_pos_y > player_radius:
        player_pos_y -= player_speed
    if keys[pygame.K_s] and player_pos_y < height - player_radius:
        player_pos_y += player_speed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            sys.exit()

    screen.fill((50, 50, 50))
    
    pygame.draw.circle(screen, player_color, (player_pos_x, player_pos_y), player_radius)
    
    if num_enemies < max_enemies:
        for i in range(max_enemies - num_enemies):
            enemy = getEnemy(player_lvl)

            if player_pos_x < enemy[0]:
                factorx = -1
            else:
                factorx = 1
            if player_pos_y < enemy[1]:
                factory = -1
            else:
                factory = 1

            pygame.draw.circle(screen, enemy[3], (enemy[0],

    pygame.display.update()
    clock.tick(60)

