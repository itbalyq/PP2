import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')  

clock = pygame.time.Clock()

# Set snake block size and initial speed
snake_block = 10
snake_speed = 10

# Define fonts for text rendering
font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("arial", 25)

# Define different weights for food
food_weights = [1, 2, 3]  # Adjust the weights as needed

# Function to display score and level
def Your_score(score, level):
    score_text = score_font.render("Score: " + str(score) + " | Level: " + str(level), True, yellow)
    dis.blit(score_text, [0, 0])

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Function to generate food for the snake
def generate_food(snake_List):
    global food_weights  # Access global variable
    # Randomly choose food position based on weights
    food_index = random.choices(range(len(food_weights)), weights=food_weights)[0]
    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    return food_index, foodx, foody

# Main game loop
def gameLoop():
    global snake_speed
    game_over = False
    game_close = False

    x1 = dis_width // 2
    y1 = dis_height // 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1 

    food_index, foodx, foody = generate_food(snake_List)

    score = 0  
    level = 1  
    food_eaten = 0  

    # Timer variables for food disappearance
    start_time = time.time()
    food_timer = 5  # Food disappears after 5 seconds

    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        our_snake(snake_block, snake_List)
        Your_score(score, level)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            food_index, foodx, foody = generate_food(snake_List)
            Length_of_snake += 1
            score += food_weights[food_index]  # Update score based on food weight
            food_eaten += 1
            if score >= 3:  
                level += 1
                food_eaten = 0
                snake_speed += 2  

        # Check if food timer has expired
        current_time = time.time()
        if current_time - start_time > food_timer:
            food_index, foodx, foody = generate_food(snake_List)
            start_time = current_time  # Reset the timer

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
