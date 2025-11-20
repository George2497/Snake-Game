import config
import random

class Food:
  def __init__(self, canvas):
    x = random.randint(0, (config.GAME_WIDTH/config.SPACE_SIZE)-1) * config.SPACE_SIZE
    y = random.randint(0, (config.GAME_HEIGHT/config.SPACE_SIZE)-1) * config.SPACE_SIZE
    self.coordinates = [x,y]
    self.canvas = canvas
    self.canvas.create_oval(x,y, x+config.SPACE_SIZE, y+config.SPACE_SIZE, fill=config.FOOD_COLOR, tag="food")
