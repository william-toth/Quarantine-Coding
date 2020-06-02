from cs1lib import *
from random import *

FRAMERATE = 20
GAME_OVER_X = 140
GAME_OVER_Y = 150

snake_link_list = []
direction = "right"
game_over = False
food_x = randint (1, 39) * 10
food_y = randint (1, 39) * 10
length = 0

class SnakeLink:
    def __init__ (self, x_link, y_link):
        self.x = x_link
        self.y = y_link

    def draw (self):
        if self.x % 20 == 0:
            rvalue = 1
        else:
            rvalue = 0
        if self.x % 20 == 10:
            gvalue = 1
        else:
            gvalue = 0
        if self.y % 20 == 0:
            bvalue = 1
        else:
            bvalue = 0

        set_fill_color (rvalue, gvalue, bvalue)
        disable_stroke()
        draw_circle (self.x, self.y, 5)

def keypress (key):
    global direction, snake_link_list, game_over, food_x, food_y, length
    if key.lower () == "w" and direction != "down":
        direction = "up"
    elif key.lower () == "a" and direction != "right":
        direction = "left"
    elif key.lower () == "s" and direction != "up":
        direction = "down"
    elif key.lower () == "d" and direction != "left":
        direction = "right"
    if key.lower () == "q":
        cs1_quit ()
    if key.lower () == " ":
        snake_link_list = []
        direction = "right"
        game_over = False
        food_x = randint(1, 39) * 10
        food_y = randint(1, 39) * 10
        length = 0

def game_over_func ():
    global direction
    if game_over:
        direction = None

        enable_stroke()
        set_font_size (20)
        set_stroke_color(1, 0, 0)

        set_fill_color (0, 0, 0)
        draw_rectangle (GAME_OVER_X - 52, GAME_OVER_Y - 20, 225, 67)

        draw_text ("GAME OVER", GAME_OVER_X, GAME_OVER_Y)

        set_font_size(15)
        draw_text("Your length was", GAME_OVER_X, GAME_OVER_Y + 20)
        length_string = str (length)
        draw_text(length_string, GAME_OVER_X + 110, GAME_OVER_Y + 20)
        draw_text ("Press Q to quit, Space to restart", GAME_OVER_X - 45, GAME_OVER_Y + 40)


def draw_everything ():
    global snake_link_list, food_x, food_y, game_over, length

    if len(snake_link_list) == 0:
        first_link = SnakeLink (200, 200)
        second_link = SnakeLink (190, 200)
        snake_link_list.append (first_link)
        snake_link_list.append (second_link)
        length = 2

    set_clear_color (0, 0, 0)
    clear ()

    for link in snake_link_list:
        link.draw ()

    disable_stroke ()
    set_fill_color (1, uniform (0, 1), 0)
    draw_circle (food_x, food_y, 5)

    game_over_func()

    if direction != None:
        if direction == "right":
            new_link = SnakeLink (snake_link_list[0].x + 10, snake_link_list[0].y)
        if direction == "left":
            new_link = SnakeLink (snake_link_list[0].x - 10, snake_link_list[0].y)
        if direction == "up":
            new_link = SnakeLink (snake_link_list[0].x, snake_link_list[0].y - 10)
        if direction == "down":
            new_link = SnakeLink (snake_link_list[0].x, snake_link_list[0].y + 10)

        for i in range (len(snake_link_list) - 1, 0, -1):
            snake_link_list[i] = snake_link_list[i-1]

        snake_link_list[0] = new_link

    if snake_link_list[-1].x - 10 == snake_link_list[-2].x:
        added_link = SnakeLink (snake_link_list[-1].x + 10, snake_link_list[-1].y)
    if snake_link_list[-1].x + 10 == snake_link_list[-2].x:
        added_link = SnakeLink (snake_link_list[-1].x - 10, snake_link_list[-1].y)
    if snake_link_list[-1].y - 10 == snake_link_list[-2].y:
        added_link = SnakeLink (snake_link_list[-1].x, snake_link_list[-1].y + 10)
    if snake_link_list[-1].y + 10 == snake_link_list[-2].y:
        added_link = SnakeLink(snake_link_list[-1].x, snake_link_list[-1].y - 10)

    if snake_link_list[0].x == food_x and snake_link_list[0].y == food_y:
        food_x = randint (1, 39) * 10
        food_y = randint (1, 39) * 10
        snake_link_list.append (added_link)
        length += 1

    if snake_link_list[0].x == 0 or snake_link_list[0].x == 400 or snake_link_list[0].y == 0 or snake_link_list[0].y == 400:
        game_over = True

    for i in range (0, len(snake_link_list)):
        for j in range (0, len(snake_link_list)):
            if i == j:
                continue
            if snake_link_list[i].x == snake_link_list[j].x and snake_link_list[i].y == snake_link_list[j].y:
                game_over = True



start_graphics (draw_everything, framerate = FRAMERATE, key_press = keypress)