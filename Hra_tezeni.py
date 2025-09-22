import pygame
import random

pygame.init()

# -Nastavení okna-
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hej co ja vim proste cool nazev hry")

# -Rychlost hry-
clock = pygame.time.Clock()

# -Barvičky-
WHITE = pygame.Color("White")
BLACK = pygame.Color("black")
GREEN = pygame.Color("green")
RED = pygame.Color("red")
GRAY = pygame.Color("gray")
BLUE = pygame.Color("dodgerblue")
GREEN = pygame.Color("green")
GOLD = pygame.Color("gold")
# -Hráč-
player_x, player_y = 100, 100
player_radius = 20
player_speed = 4
    
# -Kámen-
stone_size = 60
stone_health = 4
mine_timer = 0
num_stones = 5
respawn_time = 4000 #každé 4 vteřiny se spawne nový kámen

stone_types = [
    {"name": "kámen", "health": 4, "color": GRAY, "points": 1},
    {"name": "Copper", "health": 6, "color": GREEN, "points": 3},
    {"name": "Tin", "health": 10, "color": GOLD, "points": 5},
    {"name": "Iron", "health": 10, "color": GOLD, "points": 5},
    {"name": "Lead", "health": 10, "color": GOLD, "points": 5},
    {"name": "Silver", "health": 10, "color": GOLD, "points": 5},
    {"name": "Tungsten", "health": 10, "color": GOLD, "points": 5},
    {"name": "Gold", "health": 10, "color": GOLD, "points": 5},
    {"name": "Platinum", "health": 10, "color": GOLD, "points": 5},
    #{"name": "Meteorite", "health": 10, "color": GOLD, "points": 5},
]

stones = []
for _ in range(num_stones):
    typ = random.choice(stone_types)
    stone_rect = pygame.Rect(random.randint(0, WIDTH-stone_size),
                             random.randint(0, HEIGHT-stone_size),
                             stone_size, stone_size)
    stones.append({
        "rect": stone_rect,
        "type": typ,
        "health": typ["health"],
        "mine_timer": 0,
        "respawn_timer": 0
    })
    
# -body-
score = 0
font = pygame.font.SysFont(None, 30)
# -Hlavní smyčka-
running = True
while running:
    screen.fill(WHITE)
    dt = clock.tick(60)
    
    # -Hráč pohyb-
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed 
        
    player = pygame.draw.circle(screen, BLUE, (player_x, player_y), player_radius)     

    # -Těžba kamene-
    for stone in stones:
        rect = stone["rect"]
        color = stone["type"]["color"]
        if stone["health"] > 0:
            pygame.draw.rect(screen, color, rect)
            if player.colliderect(rect):
                stone["mine_timer"] += dt
                if stone["mine_timer"] > 1000:  # 1 život za 1 sekundu
                    stone["health"] -= 1
                    stone["mine_timer"] = 0
                    if stone["health"] <= 0:
                        score += stone["type"]["points"]
        else:
            # Respawn timer
            stone["respawn_timer"] += dt
            if stone["respawn_timer"] > respawn_time:
                new_type = random.choice(stone_types)  # -nový typ kamení při respawnu-
                stone["rect"].x = random.randint(0, WIDTH-stone_size)
                stone["rect"].y = random.randint(0, HEIGHT-stone_size)
                stone["type"] = new_typed
                stone["health"] = new_type["health"]
                stone["respawn_timer"] = 0

    # -skore-
    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    

pygame.quit()
