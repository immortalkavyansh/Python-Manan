import pygame
import random
import os

pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255,255,0)
orange = (255,165,0)
maroon = (128, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Background Image
bimage = pygame.image.load('G:\\Python-Manan\\Python-Projects\\MainGame.png')
bimage = pygame.transform.scale(bimage, (screen_width, screen_height)).convert_alpha()
wimage = pygame.image.load('G:\\Python-Manan\\Python-Projects\\welcomeimage.jpg')
wimage = pygame.transform.scale(wimage, (screen_width, screen_height)).convert_alpha()
gameover = pygame.image.load('G:\\Python-Manan\\Python-Projects\\gameoooo.jpg')
gameover = pygame.transform.scale(gameover, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("SnakesWithManan - PythonWithManan")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(wimage, (0, 0))
        text_screen("Welcome to Snakes", black, 170, 260)
        text_screen("Press Space Bar To Play", black, 130, 300)
        text_screen("Happy Birthday Kavi", blue, 510  , 4)
        text_screen("A small Gift", blue, 670, 40)
        text_screen("From your Brother Manan", blue,430, 73)
        text_screen("Hope You enjoy!!!", blue, 590, 110)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('G:\\Python-Manan\\Python-Projects\\Game-On-Ujjwal-Edition.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(50)


# Game Loop
def gameloop():
    snk_list = []
    snk_length = 1

    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    food_size = 20
    snake_size = 20
    score = 0
    fps = 50
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 55, 30)
    # Check if hiscore file exists

    if (not os.path.exists("PygameHighscore.txt")):
        with open("PygameHighscore.txt", "w") as f:
            f.write("0")

    with open("PygameHighscore.txt", "r") as f:
        highscore = f.read()
    while not exit_game:
        if game_over:
            with open("PygameHighscore.txt", "w") as f:
                f.write (str(highscore))
            gameWindow.fill(orange)
            gameWindow.blit(gameover, (0, 0))
            text_screen("Game Over! Press Enter To Play Again", yellow, 100, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x = 6
                            velocity_y = 0

                        if event.key == pygame.K_LEFT:
                            velocity_x = - 6
                            velocity_y = 0

                        if event.key == pygame.K_UP:
                            velocity_y = - 6
                            velocity_x = 0

                        if event.key == pygame.K_DOWN:
                            velocity_y = 6
                            velocity_x = 0

                        if event.key == pygame.K_q:
                            score += 20

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
                score += 10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(highscore):
                    highscore = score

            gameWindow.fill(white)
            gameWindow.blit(bimage, (0, 0))
            text_screen("Score: " + str(score) + "  Highscore:  "+str(highscore), black, 5, 5)
            pygame.draw.rect(gameWindow, maroon, [food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

                if head in snk_list[:-1]:
                    game_over = True
                    pygame.mixer.music.load('G:\\Python-Manan\\Python-Projects\\game_over.mp3')
                    pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('G:\\Python-Manan\\Python-Projects\\game_over.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow, blue, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()
gameloop()