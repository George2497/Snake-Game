import config

class Snake:
  def __init__(self, canvas):
    self.body_size = config.BODY_PARTS
    self.coordinates = []
    self.squares = []
    self.canvas = canvas

    for i in range(0, config.BODY_PARTS):
      self.coordinates.append([0, 0])

    for x, y in self.coordinates:
      square = self.canvas.create_rectangle(x, y, x + config.SPACE_SIZE, y + config.SPACE_SIZE, fill=config.SNAKE_COLOR, tag="snake")
      self.squares.append(square)