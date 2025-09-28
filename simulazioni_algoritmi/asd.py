import pygame
import random
import math

# --- CONFIGURAZIONE ---
NUM_NODI = 5          # Numero di nodi sulla circonferenza
NUM_ARCHI = 15         # Numero totale di archi (minimo NUM_NODI-1)
DIREZIONATO = True     # True se il grafo è orientato
WIDTH, HEIGHT = 800, 600
RAGGIO_NODO = 20
PADDING_PESO = 4       # Margine intorno al peso
RAGGIO_CIRCONFERENZA = 250  # Raggio della circonferenza dei nodi

# --- INIZIALIZZAZIONE PYGAME ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grafo Pesato su Circonferenza")
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

# --- GENERA NODI SU CIRCONFERENZA ---
cx, cy = WIDTH // 2, HEIGHT // 2  # Centro circonferenza
nodi = []
for i in range(NUM_NODI):
    theta = 2 * math.pi * i / NUM_NODI
    x = int(cx + RAGGIO_CIRCONFERENZA * math.cos(theta))
    y = int(cy + RAGGIO_CIRCONFERENZA * math.sin(theta))
    nodi.append((x, y))

# --- CREA ARCHI PER GARANTIRE CONNESSIONE ---
archi = set()
connessi = set()
remaining = list(range(NUM_NODI))
random.shuffle(remaining)

# Inizio dal primo nodo
connessi.add(remaining.pop())

while remaining:
    u = random.choice(list(connessi))
    v = remaining.pop()
    peso = random.randint(1, 20)
    archi.add((u, v, peso))
    connessi.add(v)

# --- AGGIUNGI ALTRI ARCHI CASUALI FINO A NUM_ARCHI ---
while len(archi) < NUM_ARCHI:
    u = random.randint(0, NUM_NODI - 1)
    v = random.randint(0, NUM_NODI - 1)
    if u == v:
        continue
    arco = (u, v) if DIREZIONATO else tuple(sorted((u, v)))
    if any(a[:2] == arco for a in archi):
        continue
    peso = random.randint(1, 20)
    archi.add((u, v, peso))

archi = list(archi)

# --- FUNZIONE PER DISEGNARE IL GRAFO ---
def draw_graph():
    screen.fill((0, 0, 0))  # Sfondo nero

    # Disegna archi e pesi
    for u, v, peso in archi:
        x1, y1 = nodi[u]
        x2, y2 = nodi[v]
        pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 2)

        # Freccia se direzionato
        if DIREZIONATO:
            angle = math.atan2(y2 - y1, x2 - x1)
            arrow_size = 10
            end_x = x2 - arrow_size * math.cos(angle)
            end_y = y2 - arrow_size * math.sin(angle)
            left = (end_x - 5 * math.cos(angle - math.pi / 2), 
                    end_y - 5 * math.sin(angle - math.pi / 2))
            right = (end_x - 5 * math.cos(angle + math.pi / 2), 
                     end_y - 5 * math.sin(angle + math.pi / 2))
            pygame.draw.polygon(screen, (255,255,255), [(x2, y2), left, right])

        # Peso al centro con quadrato bianco dietro
        text = font.render(str(peso), True, (255, 255, 255))
        text_rect = text.get_rect(center=((x1 + x2)//2, (y1 + y2)//2))
        rect_bg = pygame.Rect(
            text_rect.left - PADDING_PESO,
            text_rect.top - PADDING_PESO,
            text_rect.width + 2*PADDING_PESO,
            text_rect.height + 2*PADDING_PESO
        )
        pygame.draw.rect(screen, (0,0,0), rect_bg)          # sfondo nero
        pygame.draw.rect(screen, (255,255,255), rect_bg, 1) # bordo bianco
        screen.blit(text, text_rect)

    # Disegna nodi
    for i, (x, y) in enumerate(nodi):
        pygame.draw.circle(screen, (0, 0, 0), (x, y), RAGGIO_NODO)  # nodo nero
        pygame.draw.circle(screen, (255, 255, 255), (x, y), RAGGIO_NODO, 2)  # bordo bianco
        text = font.render(str(i), True, (255, 255, 255))
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

# --- MAIN LOOP ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_graph()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
