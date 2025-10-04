# Flappy bird game in python (Type shii)
import pygame, sys, random

# Initialize
pygame.init()
clock = pygame.time.Clock()

# Screen
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird 🐦")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (135, 206, 250)

# Bird
bird = pygame.Rect(50, 300, 30, 30)
gravity = 0
jump = -8

# Pipes
pipe_width = 70
gap = 150
pipes = []
pipe_timer = 0

score = 0
font = pygame.font.SysFont(None, 36)

def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

def move_pipes():
    global pipes, score
    new_pipes = []
    for pipe in pipes:
        pipe.x -= 4
        if pipe.right > 0:
            new_pipes.append(pipe)
        if pipe.centerx == bird.centerx:
            score += 1
    pipes = new_pipes

# Main game loop
while True:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            gravity = jump

    # Bird movement
    gravity += 0.5
    bird.y += gravity
    pygame.draw.ellipse(screen, WHITE, bird)

    # Pipes
    pipe_timer += 1
    if pipe_timer > 90:
        pipe_height = random.randint(100, 400)
        pipes.append(pygame.Rect(width, 0, pipe_width, pipe_height))
        pipes.append(pygame.Rect(width, pipe_height + gap, pipe_width, height))
        pipe_timer = 0

    move_pipes()
    draw_pipes()

    # Collision
    for pipe in pipes:
        if bird.colliderect(pipe):
            print("💀 Game Over! Final Score:", score)
            pygame.quit()
            sys.exit()

    if bird.top < 0 or bird.bottom > height:
        print("💀 Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    # Score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)
