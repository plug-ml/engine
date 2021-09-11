import entity

class Button(entity.Entity):
  def __init__(self, x, y, width, height, onClicked, draw_func=entity.draw_box, is_static=False):
    super().__init__(x, y, width, height, draw_func=draw_func, is_static=is_static)
    self.onClicked = onClicked 

  def inButton(self, x, y):
    return self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height

  def onClick(self):
    self.onClicked()

class NodeLayer(Button):
  def __init__(self, x, y, dim, gap, onClicked):
    super().__init__(x, y, dim, dim, onClicked, draw_func=self.drawLayer, is_static=False)
    self.dim = dim
    self.gap = gap
    self.nodes = 1 
 
  def drawLayer(self, canvas, x, y, width, height):
    dim = self.dim
    gap = self.gap
    nodes = self.nodes
    for i in range(nodes):
      canvas.create_oval(x, y + (dim + gap) * i, x + dim, y + (dim + gap) * i + dim, fill='white')
