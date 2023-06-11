import pygame
import random


def score():  # Function to display scores

    player_score_surface = game_font.render(f'{player_score}', False, color)
    player_score_rect = player_score_surface.get_rect(center=(375, 40))
    screen.blit(player_score_surface, player_score_rect)

    computer_score_surface = game_font.render(f'{computer_score}', False, color)
    computer_score_rect = computer_score_surface.get_rect(center=(625, 40))
    screen.blit(computer_score_surface, computer_score_rect)


def final_score():  # Function to display final scores

    player_final_score_surface = game_font.render(f' User Score: {player_score}', False, color)
    player_final_score_rect = player_final_score_surface.get_rect(center=(500, 100))
    screen.blit(player_final_score_surface, player_final_score_rect)

    computer_final_score_surface = game_font.render(f' Computer Score: {computer_score}', False, color)
    computer_final_score_rect = computer_final_score_surface.get_rect(center=(500, 300))
    screen.blit(computer_final_score_surface, computer_final_score_rect)

    replay_message = game_font.render('Press Space to play again!', False, color)
    replay_message_rect = replay_message.get_rect(center=(500, 500))
    screen.blit(replay_message, replay_message_rect)


def title_screen_text():  # Function to display the title screen info

    title_surface = title_screen_font.render('PONG', False, color)
    title_surface_rect = title_surface.get_rect(center=(500, 100))
    screen.blit(title_surface, title_surface_rect)

    play_message_surface = game_font.render('Press Space to Play', False, color)
    play_message_surface_rect = play_message_surface.get_rect(center=(500, 500))
    screen.blit(play_message_surface, play_message_surface_rect)


def color_change():  # Function to display color changing information

    color_change_title_surface = color_change_font.render('Color Settings', False, color)
    color_change_title_rect = color_change_title_surface.get_rect(center=(500, 200))
    screen.blit(color_change_title_surface, color_change_title_rect)

    color_change_red = color_change_font.render('1 - Red', False, (255, 0, 0))
    color_change_red_rect = color_change_red.get_rect(center=(450, 225))
    screen.blit(color_change_red, color_change_red_rect)

    color_change_green = color_change_font.render('2 - Green', False, (0, 255, 0))
    color_change_green_rect = color_change_green.get_rect(center=(450, 250))
    screen.blit(color_change_green, color_change_green_rect)

    color_change_blue = color_change_font.render('3 - Blue', False, (0, 0, 255))
    color_change_blue_rect = color_change_blue.get_rect(center=(450, 275))
    screen.blit(color_change_blue, color_change_blue_rect)

    color_change_yellow = color_change_font.render('4 - Yellow', False, (255, 255, 0))
    color_change_yellow_rect = color_change_yellow.get_rect(center=(450, 300))
    screen.blit(color_change_yellow, color_change_yellow_rect)

    color_change_orange = color_change_font.render('5 - Orange', False, (255, 165, 0))
    color_change_orange_rect = color_change_orange.get_rect(center=(450, 325))
    screen.blit(color_change_orange, color_change_orange_rect)

    color_change_purple = color_change_font.render('6 - Purple', False, (160, 32, 240))
    color_change_purple_rect = color_change_purple.get_rect(center=(550, 225))
    screen.blit(color_change_purple, color_change_purple_rect)

    color_change_pink = color_change_font.render('7 - Pink', False, (255, 192, 203))
    color_change_pink_rect = color_change_pink.get_rect(center=(550, 250))
    screen.blit(color_change_pink, color_change_pink_rect)

    color_change_cyan = color_change_font.render('8 - Cyan', False, (0, 100, 100))
    color_change_cyan_rect = color_change_cyan.get_rect(center=(550, 275))
    screen.blit(color_change_cyan, color_change_cyan_rect)

    color_change_brown = color_change_font.render('9 - Brown', False, (150, 75, 0))
    color_change_brown_rect = color_change_brown.get_rect(center=(550, 300))
    screen.blit(color_change_brown, color_change_brown_rect)

    color_change_white = color_change_font.render('0 - White', False, (255, 255, 255))
    color_change_white_rect = color_change_white.get_rect(center=(550, 325))
    screen.blit(color_change_white, color_change_white_rect)


pygame.init()  # Starts Pygame

pygame.display.set_caption('Pong')  # Sets a caption for the display screen

# Constant Variables

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))  # Sets the display screen

clock = pygame.time.Clock()  # Is a part of managing FPS

game_active = False

color = (255, 255, 255)  # White

left_paddle = pygame.Rect(10, 240, 10, 150)  # Draws the left paddle rectangle
left_paddle_speed = 8  # Speed of the left paddle

right_paddle = pygame.Rect(980, 240, 10, 150)  # Draws the right paddle rectangle
right_paddle_speed = 5  # Speed of the right paddle

ball = pygame.Rect((screen_width / 2) - 15, (screen_height / 2) - 15, 30, 30)  # Draws the ball rectangle
ball_x_speed = 10  # Speed of the ball (x-pos)
ball_y_speed_list = [-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]  # All the possible speeds that the y speed can have
ball_y_speed_list_pos = [1, 2, 3, 4, 5, 6]
ball_y_speed_list_neg = [-1, -2, -3, -4, -5, -6]
ball_y_speed = 0  # Speed of the ball (y-pos)

line_start_pos = (500, 0)  # Start position of the line
line_end_pos = (500, 600)  # End position of the line

up_key_pressed = None

down_key_pressed = None

player_score = 0
computer_score = 0

collision_tolerance = 10

# Imported Assets

game_font = pygame.font.Font('Minecraft.ttf', 50)  # Loads in the font for the scores
title_screen_font = pygame.font.Font('Minecraft.ttf', 90)  # Loads the font for the title screen
color_change_font = pygame.font.Font('Minecraft.ttf', 20)  # Loads the font for the color changing text

ball_hit_paddle = pygame.mixer.Sound('sounds_ping_pong_8bit/ping_pong_8bit_beeep.ogg')
score_sound = pygame.mixer.Sound('sounds_ping_pong_8bit/ping_pong_8bit_peeeeeep.ogg')
ball_hit_border = pygame.mixer.Sound('sounds_ping_pong_8bit/ping_pong_8bit_plop.ogg')

# Main Game Loop

while True:

    # Event Loop

    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # Checks if the user quits

            pygame.quit()

            exit()

        if event.type == pygame.KEYDOWN:

            # Changing the color of the game

            if event.key == pygame.K_0:

                color = (255, 255, 255)  # White

            if event.key == pygame.K_1:

                color = (255, 0, 0)  # Red

            if event.key == pygame.K_2:

                color = (0, 255, 0)  # Green

            if event.key == pygame.K_3:

                color = (0, 0, 255)  # Blue

            if event.key == pygame.K_4:

                color = (255, 255, 0)  # Yellow

            if event.key == pygame.K_5:

                color = (255, 165, 0)  # Orange

            if event.key == pygame.K_6:

                color = (160, 32, 240)  # Purple

            if event.key == pygame.K_7:

                color = (255, 192, 203)  # Pink

            if event.key == pygame.K_8:

                color = (0, 100, 100)  # Cyan

            if event.key == pygame.K_9:

                color = (150, 75, 0)  # Brown

        if game_active:

            # Checks for player input

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:

                    up_key_pressed = True

                if event.key == pygame.K_DOWN:

                    down_key_pressed = True

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:

                    up_key_pressed = False

                if event.key == pygame.K_DOWN:

                    down_key_pressed = False

        else:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    # Resetting the game

                    game_active = True

                    player_score = 0

                    computer_score = 0

                    ball.x = (screen_width / 2) - 15

                    ball.y = (screen_height / 2) - 15

                    ball_x_speed = 10

                    ball_y_speed = 0

                    left_paddle.y = 230

                    right_paddle.y = 230

    if game_active:

        # Checks if flag variables are True

        if up_key_pressed:

            left_paddle.y -= left_paddle_speed

        if down_key_pressed:

            left_paddle.y += left_paddle_speed

        # Collision of left paddle

        if left_paddle.top <= 0:

            left_paddle.top = 0

        if left_paddle.bottom >= screen_height:

            left_paddle.bottom = screen_height

        # Movement of Right Paddle

        if right_paddle.y > ball.y:

            right_paddle.y -= right_paddle_speed

        if right_paddle.y < ball.y:

            right_paddle.y += right_paddle_speed

        # Making sure the right paddle doesn't go off-screen

        if right_paddle.top <= 0:

            right_paddle.top = 0

        if right_paddle.bottom >= screen_height:

            right_paddle.bottom = screen_height

        # Movement of the ball

        ball.x += ball_x_speed

        ball.y += ball_y_speed

        # Collisions with the paddles

        if ball.colliderect(right_paddle):  # Collision with right paddle

            # Collision with the side of the right paddle

            if abs(right_paddle.left - ball.right) < collision_tolerance:

                ball_x_speed *= -1

                ball_y_speed = random.choice(ball_y_speed_list)

                ball_hit_paddle.play()

            # Collision with the top of the right paddle

            if abs(right_paddle.top - ball.bottom) < collision_tolerance:

                ball_x_speed *= -1

                ball_y_speed = random.choice(ball_y_speed_list_neg)

                ball_hit_paddle.play()

            # Collision with the bottom of the right paddle

            if abs(right_paddle.bottom - ball.top) < collision_tolerance:

                ball_x_speed *= -1

                ball_y_speed = random.choice(ball_y_speed_list_pos)

                ball_hit_paddle.play()

        if ball.colliderect(left_paddle):  # Collision with left paddle

            # Collision with the side of the left paddle

            if abs(left_paddle.right - ball.left) < collision_tolerance:

                ball_x_speed *= -1

                ball_y_speed = random.choice(ball_y_speed_list)

                ball_hit_paddle.play()

            # Collision with the top of the left paddle

            if abs(left_paddle.top - ball.bottom) < collision_tolerance:

                ball_x_speed *= -1

                ball_y_speed = random.choice(ball_y_speed_list_neg)

                ball_hit_paddle.play()

            # Collision with the bottom of the left paddle

            if abs(left_paddle.bottom - ball.top) < collision_tolerance:

                ball_x_speed *= -1

                ball_y_speed = random.choice(ball_y_speed_list_pos)

                ball_hit_paddle.play()

        # Ball going past paddles

        if ball.x < -30:

            # Resetting the game display

            ball.x = (screen_width / 2) - 15

            ball.y = (screen_height / 2) - 15

            computer_score += 1

            ball_x_speed = -10  # Makes the ball go towards the left

            ball_y_speed = 0

            left_paddle.y = 230

            right_paddle.y = 230

            score_sound.play()

        if ball.x > 1030:

            # Resetting the game display

            ball.x = (screen_width / 2) - 15

            ball.y = (screen_height / 2) - 15

            player_score += 1

            ball_x_speed = 10  # Makes the ball go towards the right

            ball_y_speed = 0

            left_paddle.y = 230

            right_paddle.y = 230

            score_sound.play()

        # Ball hitting the top or bottom

        if ball.top <= 0:

            ball_y_speed *= -1

            ball_hit_border.play()

        if ball.bottom >= screen_height:

            ball_y_speed *= -1

            ball_hit_border.play()

        # Displaying the objects on the screen

        screen.fill((0, 0, 0))

        pygame.draw.line(screen, color, line_start_pos, line_end_pos, 1)  # Draws the line

        score()  # Calls the score function to display scores

        pygame.draw.ellipse(screen, color, ball)  # Draws the ball onto the screen

        pygame.draw.rect(screen, color, left_paddle)  # Draws the left paddle on the screen

        pygame.draw.rect(screen, color, right_paddle)  # Draws the right paddle on the screen

        if (player_score == 3) or (computer_score == 3):

            game_active = False

    else:

        if (player_score == 0) and (computer_score == 0):

            screen.fill((0, 0, 0))

            title_screen_text()

            color_change()

        else:

            screen.fill((0, 0, 0))

            final_score()

    pygame.display.update()  # Updates the display

    clock.tick(60)  # Acts as FPS
