
Offset_x, Offset_y = 0, 0

def draw_box(canvas, x, y, width, height, color='black'):
  canvas.create_line(x, y, x + width, y, fill=color)
  canvas.create_line(x, y, x, y + height, fill=color)
  canvas.create_line(x + width, y, x + width, y + height, fill=color)
  canvas.create_line(x, y + height, x + width, y + height, fill=color)

class Entity:
  def __init__(self, x, y, width, height, is_static=True, draw_func=draw_box):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.is_static = is_static
    self.draw_func = draw_func

  def draw(self, canvas):
    self.draw_func(canvas, *self.get_params())

  def get_params(self):
    x, y, width, height = self.x, self.y, self.width, self.height
    if not self.is_static:
      x += Offset_x
      y += Offset_y
    return x, y, width, height

  def changePos(self, delta_x, delta_y):
    self.x += delta_x
    self.y += delta_y
