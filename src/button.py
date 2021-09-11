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
  def __init__(self, x, y, dim, gap, onClicked, index):
    super().__init__(x, y, dim, dim, onClicked, draw_func=self.drawLayer, is_static=False)
    self.dim = dim
    self.gap = gap
    self.nodes = 1 
    self.index = index

  def drawLayer(self, canvas, x, y, width, height):
    dim = self.dim
    gap = self.gap
    nodes = self.nodes
    for i in range(nodes):
      canvas.create_oval(x, y + (dim + gap) * i, x + dim, y + (dim + gap) * i + dim, fill='white')


def newLayer(x, y, dim, gap, onClicked, x_displace, layer_list, index):
  for i in range(len(layer_list)):
    if i < index:
      layer_list[i].changePos(-x_displace, 0)
    else:
      layer_list[i].changePos(+x_displace, 0)
  layer_list.insert(i, NodeLayer(x, y, dim, gap, onClicked))


def removeLayer(x_displace, layer_list, index):
  for i in range(index, len(layer_list)):
    layer_list[i].changePos(-x_displace, 0)
  layer_list.pop(index)


def makePMButtons(x, y, width, height, index, dim, gap, onClicked, x_displace, layer_list):
  btn_list = []
  btn_list.append(Button(x, y, width/3, height/5, index, newLayer(x, y, dim, gap, onClicked, x_displace, layer_list, index)))
  btn_list.append(Button(x + width/3, y, width/3, height/5, index, removeLayer(x_displace, layer_list, index)))
  btn_list.append(Button(x + width/3*2,y, width/3, height/5, index, newLayer(x, y, dim, gap, onClicked, x_displace, layer_list, index)))
  

  return btn_list