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
    {"name": "Emerald", "health": 6, "color": GREEN, "points": 3},
    {"name": "Zlato", "health": 10, "color": GOLD, "points": 5},
    {"name": "", "health": 10, "color": GOLD, "points": 5},
    {"name": "Sůl", "health": 2, "color": (255, 250, 250), "points": 1},
    {"name": "Síra", "health": 3, "color": (255, 255, 0), "points": 1},
    {"name": "Hematit", "health": 5, "color": (105, 105, 105), "points": 2},
    {"name": "Magnetit", "health": 6, "color": (70, 70, 70), "points": 2},
    {"name": "Pyrit", "health": 6, "color": (255, 215, 0), "points": 3},
    {"name": "Fluorit", "health": 4, "color": (100, 200, 255), "points": 2},
    {"name": "Křemen", "health": 7, "color": (230, 230, 250), "points": 3},
    {"name": "Rubín", "health": 9, "color": (220, 20, 60), "points": 5},
    {"name": "Safír", "health": 9, "color": (15, 82, 186), "points": 5},
    {"name": "Topaz", "health": 8, "color": (255, 200, 124), "points": 4},
    {"name": "Ametyst", "health": 7, "color": (153, 102, 204), "points": 3},
    {"name": "Citrín", "health": 7, "color": (230, 190, 0), "points": 3},
    {"name": "Tyrkys", "health": 6, "color": (64, 224, 208), "points": 3},
    {"name": "Jadeit", "health": 7, "color": (0, 168, 107), "points": 3},
    {"name": "Obsidian", "health": 8, "color": (40, 40, 40), "points": 4},
    {"name": "Beryl", "health": 7, "color": (0, 255, 127), "points": 3},
    {"name": "Granát", "health": 7, "color": (115, 35, 35), "points": 3},
    {"name": "Kyanit", "health": 6, "color": (0, 102, 204), "points": 3},
    {"name": "Spinel", "health": 8, "color": (255, 0, 0), "points": 4},
    {"name": "Peridot", "health": 6, "color": (204, 255, 0), "points": 3},
    {"name": "Malachit", "health": 5, "color": (11, 218, 81), "points": 2},
    {"name": "Lapis lazuli", "health": 6, "color": (38, 97, 156), "points": 3},
    {"name": "Onyx", "health": 7, "color": (0, 0, 0), "points": 3},
    {"name": "Azurit", "health": 5, "color": (0, 127, 255), "points": 2},
    {"name": "Chalkopyrit", "health": 6, "color": (184, 115, 51), "points": 3},
    {"name": "Galena", "health": 5, "color": (169, 169, 169), "points": 2},
    {"name": "Smaragd", "health": 9, "color": (0, 201, 87), "points": 5},
    {"name": "Diamant", "health": 10, "color": (185, 242, 255), "points": 6},
    {"name": "Platina", "health": 9, "color": (229, 228, 226), "points": 5},
    {"name": "Měď", "health": 5, "color": (184, 115, 51), "points": 2},
    {"name": "Stříbro", "health": 6, "color": (192, 192, 192), "points": 3},
    {"name": "Zinek", "health": 5, "color": (115, 115, 115), "points": 2},
    {"name": "Ocel", "health": 7, "color": (70, 70, 70), "points": 3},
    {"name": "Železo", "health": 6, "color": (100, 100, 100), "points": 3},
    {"name": "Titan", "health": 8, "color": (135, 134, 130), "points": 4},
    {"name": "Kobalt", "health": 7, "color": (0, 71, 171), "points": 3},
    {"name": "Nikiel", "health": 6, "color": (105, 105, 105), "points": 3},
    {"name": "Chrom", "health": 8, "color": (183, 183, 183), "points": 4},
    {"name": "Uran", "health": 6, "color": (0, 255, 0), "points": 3},
    {"name": "Rutil", "health": 6, "color": (228, 150, 45), "points": 3},
    {"name": "Zirkon", "health": 7, "color": (252, 252, 252), "points": 3},
    {"name": "Chrysoberyl", "health": 8, "color": (227, 218, 185), "points": 4},
    {"name": "Kalcit", "health": 3, "color": (255, 255, 224), "points": 1},
    {"name": "Dolomit", "health": 4, "color": (212, 212, 212), "points": 2},
    {"name": "Garnierit", "health": 5, "color": (34, 139, 34), "points": 2},
    {"name": "Pyrolusit", "health": 4, "color": (50, 50, 50), "points": 2},
    {"name": "Magnetovec", "health": 5, "color": (90, 90, 90), "points": 2},
    {"name": "Ilmenit", "health": 6, "color": (88, 88, 88), "points": 3},
    {"name": "Gips", "health": 2, "color": (245, 245, 245), "points": 1}
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