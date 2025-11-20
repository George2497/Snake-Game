from tkinter import *
import random
import food
import snake
import config

def next_turn(snake, snake_food):
  x, y = snake.coordinates[0]

  if direction == "up":
    y -= config.SPACE_SIZE
  elif direction == "down":
    y += config.SPACE_SIZE
  elif direction == "left":
    x -= config.SPACE_SIZE
  elif direction == "right":
    x += config.SPACE_SIZE

  snake.coordinates.insert(0, (x, y))

  square = canvas.create_rectangle(x, y, x + config.SPACE_SIZE, y + config.SPACE_SIZE, fill=config.SNAKE_COLOR)

  snake.squares.insert(0, square)

  if x == snake_food.coordinates[0] and y == snake_food.coordinates[1]:
    global score 
    
    score += 1

    canvas.delete("food")

    snake_food = food.Food(canvas)
    scoreLabel.config(text="Score: {}".format(score))


  else:
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]

  if check_collisions(snake):
    game_over()
  else:
    window.after(config.SPEED, next_turn, snake, snake_food)

def change_direction(new_direction):
  global direction

  if new_direction == "left":
    if direction != "right":
      direction = new_direction

  elif new_direction == "right":
    if direction != "left":
      direction = new_direction

  elif new_direction == "up":
    if direction != "down":
      direction = new_direction

  elif new_direction == "down":
    if direction != "up":
      direction = new_direction

def check_collisions(snake):
  x, y, = snake.coordinates[0]

  if x < 0 or x >= config.GAME_WIDTH:
    return True
  elif y < 0 or y >= config.GAME_HEIGHT:
    return True
  
  for config.body_part in snake.coordinates[1:]:
    if x == config.body_part[0] and y == config.body_part[1]:
      return True

  return False

def game_over():
  canvas.delete(ALL)
  canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas", 70), text="GAME OVER", fill="#ff0000", tag="gameover")
  pass

window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

scoreLabel = Label(window, text="Score:{}".format(score), font=("consolas", 40))
scoreLabel.pack()

canvas = Canvas(window, bg=config.BACKGROUND_COLOR, height=config.GAME_HEIGHT, width=config.GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = snake.Snake(canvas)
snake_food = food.Food(canvas)

next_turn(snake, snake_food)

window.mainloop()