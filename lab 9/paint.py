import pygame
import random

# Function to draw a simple line
def draw_line(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)

# Function to draw a rectangle
def draw_rect(screen, pos, color, a):
    x1 = pos[0]
    y1 = pos[1]

    print(pos)
    pygame.draw.rect(screen, color, (x1, y1, a, a), 5)

def draw_right_triangle(screen, pos, color, base, height):
    x, y = pos
    points = [(x, y), (x + base, y), (x, y - height)]
    pygame.draw.polygon(screen, color, points, 5)

def draw_equilateral_triangle(screen, pos, color, side_length):
    x, y = pos
    height = side_length * (3 ** 0.5) / 2
    points = [(x, y), (x + side_length, y), (x + side_length / 2, y - height)]
    pygame.draw.polygon(screen, color, points, 5)

def draw_rhombus(screen, pos, color, diagonal1, diagonal2):
    x, y = pos
    half_diagonal1 = diagonal1 / 2
    half_diagonal2 = diagonal2 / 2
    points = [(x, y), (x + half_diagonal1, y - half_diagonal2),
              (x + diagonal1, y), (x + half_diagonal1, y + half_diagonal2)]
    pygame.draw.polygon(screen, color, points, 5)

# Function to draw circles
def draw_c(screen, pos, color, radius):
    x = pos[0]
    y = pos[1]

    pygame.draw.circle(screen, color, pos, radius, 5)

def main():
    screen = pygame.display.set_mode((1100, 600))
    mode = 'random'
    draw_on = False
    last_pos = {0, 0}
    color = (255, 128, 0)
    radius = 10

    # Setting up colors
    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0),
        'eraser': (255, 255, 255)
    }

    screen.fill((255, 255, 255))

    while True:

        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.image.save(screen, "image.jpg")
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                # if press ctrl+r draw rectangle
                if event.key == pygame.K_s and ctrl_held:
                    mp = pygame.mouse.get_pos()
                    draw_rect(screen, mp, color, radius * 10)

                #right triangle
                if event.key == pygame.K_t and ctrl_held:
                    mp = pygame.mouse.get_pos()
                    draw_right_triangle(screen, mp, color, radius * 10, radius * 20)

                #equilateral triangle
                if event.key == pygame.K_e and ctrl_held:
                    mp = pygame.mouse.get_pos()
                    draw_equilateral_triangle(screen, mp, color, radius * 10)

                #rhombus
                if event.key == pygame.K_r and ctrl_held:
                    mp = pygame.mouse.get_pos()
                    draw_rhombus(screen, mp, color, radius * 10, radius * 20)

                # if press ctrl+c draw circles
                if event.key == pygame.K_c and ctrl_held:
                    mp = pygame.mouse.get_pos()
                    draw_c(screen, mp, color, radius * 5)

                # if press ctrl + e eraser
                if event.key == pygame.K_e and ctrl_held:
                    mode = 'eraser'
                # press t get red
                if event.key == pygame.K_k:
                    mode = 'red'
                # press b get blue
                if event.key == pygame.K_b:
                    mode = 'blue'
                # press g get green
                if event.key == pygame.K_g:
                    mode = 'green'
                # press up line get wider
                if event.key == pygame.K_UP:
                    radius += 1
                # press down line gets shrinker
                if event.key == pygame.K_DOWN:
                    radius -= 1

                # pressing just a left click will cause random color lines
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]
                pygame.draw.circle(screen, color, event.pos, radius)
                draw_on = True
            if event.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if event.type == pygame.MOUSEMOTION:
                if draw_on:
                    draw_line(screen, last_pos, event.pos, radius, color)

                last_pos = event.pos

        pygame.display.flip()

    pygame.quit()

main()
