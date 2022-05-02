import sys
from turtle import left
import pygame
from settings import *
from Paddle import *
from Ball import *
import sys

## Colours
WHITE = (255,255,255)
BLACK = (0,0,0)


## Pygame initialization
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

## Fonts
SCORE_FONT = pygame.font.SysFont("Ariel", 50)

## Paddle and Ball sizes
PADDLE_WIDTH , PADDLE_HEIGHT = 20, 100 
BALL_RADIUS = 7

## Set Background Colour
BACKGROUND_COLOR = BLACK

WIN_SCORE = 3

def main():
    running = True

    ## Initialize Paddles and Ball
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH//2, HEIGHT//2,BALL_RADIUS)

    ## Initialize score
    left_score = right_score = 0

    ## Win text

    while (running):

        ##Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        key_pressed = pygame.key.get_pressed()
        handle_paddle_movement(key_pressed, left_paddle, right_paddle)
        
        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        if (ball.x + ball.radius <= 0):
            right_score += 1
            reset(ball, left_paddle, right_paddle)
        elif (ball.x - ball.radius >= WIDTH):
            left_score += 1
            reset(ball, left_paddle, right_paddle)
        
        if (left_score >= WIN_SCORE or right_score >= WIN_SCORE):
            over_text = SCORE_FONT.render("Game Over", 1, WHITE)

            WIN.fill(BLACK)
            WIN.blit(over_text, (WIDTH //2 - over_text.get_width()//2, HEIGHT//2 - over_text.get_height()//2))

            pygame.display.update()
            pygame.time.delay(3000)

            reset(ball, left_paddle, right_paddle)
            left_score = 0
            right_score = 0
        
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)
        clock.tick(FPS)

    
    pygame.quit()

def handle_collision(ball, left_paddle, right_paddle):
    ##Check if the ball hits a border on the y-axis
    if (ball.y - ball.radius <= 0) or (ball.y + ball.radius >= HEIGHT):
        ball.y_velocity *= -1
    
    if ball.x_velocity < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                #Calculate ball x-velocity
                ball.x_velocity *= -1

                ##Calculate ball y-velocity
                mid_point = left_paddle.y + left_paddle.height/2
                diff_y = mid_point - ball.y 
                max_disp = left_paddle.height/2 ##Maximum displacement from the mid_point

                ## We want to make the ball has the highest velocity if it hits the edge of the paddle. In other words:
                ## Displacement / Rf (Reduction Factor) = MV(Max Velocity)
                ## Only if the ball is at the edge of the paddle, i.e the maximum displacement from the center of the paddle

                ## Hence, formula is MD(Maximum Displacement) / RF(Reduction factor) = MV(Max Velocity) or,
                ## RF(Reduction Factor) = MD(Maximum Displacement)/ MV(Max Velocity
                rf = max_disp / ball.max_velocity

                ball.y_velocity = -1 * (diff_y / rf)
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x :
                #Calculate ball x-velocity
                ball.x_velocity *= -1

                ##Calculate ball y-velocity
                mid_point = right_paddle.y + right_paddle.height/2
                diff_y = mid_point - ball.y 
                max_disp = right_paddle.height/2 ##Maximum displacement from the mid_point

                rf = max_disp / ball.max_velocity

                ball.y_velocity = -1 * (diff_y / rf)

def handle_paddle_movement(key_pressed, left_paddle, right_paddle):
    if key_pressed[pygame.K_w] and left_paddle.y - left_paddle.velocity >= 0:
        left_paddle.move(upDir = True)

    if key_pressed[pygame.K_s] and (left_paddle.y + left_paddle.height) + left_paddle.velocity <= HEIGHT:
        left_paddle.move(upDir = False)

    if key_pressed[pygame.K_UP] and right_paddle.y - right_paddle.velocity >= 0:
        right_paddle.move(upDir = True)

    if key_pressed[pygame.K_DOWN] and (right_paddle.y + right_paddle.height) + right_paddle.velocity <= HEIGHT:
        right_paddle.move(upDir = False)

def draw(win, paddles, ball, left_score, right_score):
    win.fill(BACKGROUND_COLOR)

    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)

    for i in range (10, HEIGHT + 1, HEIGHT // 20):
        if (i % 2 == 0):
            pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i ,10, HEIGHT//20))
    
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH//(4/3) - right_score_text.get_width()//2, 20))


    for paddle in paddles:
        paddle.draw(win)
    
    ball.draw(win)
    
    pygame.display.update()

def reset(ball, left_paddle, right_paddle):
    ball.reset()
    left_paddle.reset()
    right_paddle.reset()


    pass
if __name__ == "__main__":
    main()