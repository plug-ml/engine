import entity

START_Y = 375

class Button(entity.Entity):
  def __init__(self, x, y, width, height, onClicked, draw_func=entity.draw_box, is_static=False):
    super().__init__(x, y, width, height, draw_func=draw_func, is_static=is_static)
    self.onClicked = onClicked

  def inButton(self, x, y):
    return self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height

  def onClick(self):
    self.onClicked()
  

class NodeLayer(Button):
  def __init__(self, x, dim, gap, onClicked, index):
    super().__init__(x, START_Y - dim / 2, dim, dim, onClicked, draw_func=self.drawLayer, is_static=False)
    self.dim = dim
    self.gap = gap
    self.nodes = 1 
    self.index = index
    self.spawnNodeButtons = lambda: AddButton(), MinusButton()
    self.spawnLayerButtons = lambda: AddButton(x, START_Y, dim, gap, newLayer(x, START_Y, dim, gap, onClicked, 50, , index)), MinusButton(), AddButton()

  def drawLayer(self, canvas, x, y, width, height):
    dim = self.dim
    gap = self.gap
    nodes = self.nodes
    for i in range(nodes):
      canvas.create_oval(x, y + (dim + gap) * i, x + dim, y + (dim + gap) * i + dim, fill='white')
    self.leftAdd.draw(canvas)
    self.minusBtn.draw(canvas)
    self.rightAdd.draw(canvas)

  def inButton(self, x, y):
    if self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height:
      self.spawnLayerButtons()

class AddButton(Button):
  def __init__(self, x, y, dim, gap, onClicked, index):
    super().__init__(x, y, dim, dim, onClicked, draw_func=self.drawLayer, is_static=False)
    self.index = index
  
  def onClick(self):
    self.onClicked()

class MinusButton(Button):
  def __init__(self, x, y, dim, gap, onClicked, index):
    super().__init__(x, y, dim, dim, onClicked, draw_func=self.drawLayer, is_static=False)
    self.index = index
  
def newLayer(x, y, dim, gap, onClicked, x_displace, layer_list, index):
  for i in range(index, len(layer_list)):
    layer_list[i].changePos(x_displace, 0)
  layer_list.insert(i, NodeLayer(x, y, dim, gap, onClicked))


def removeLayer(x_displace, layer_list, index):
  for i in range(index, len(layer_list)):
    layer_list[i].changePos(-x_displace, 0)
  layer_list.pop(index)
