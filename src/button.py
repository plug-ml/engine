
class Button:
  def __init__(self, x_0, y_0, width, length, onClicked):
    self.x_0 = x_0
    self.y_0 = y_0
    self.w = width
    self.l = length
    self.onClicked = onClicked 

  def drawButton(self, canvas, color="black"):
    canvas.create_line(self.x_0, self.y_0, self.x_0 + self.w, self.y_0, fill=color)
    canvas.create_line(self.x_0, self.y_0, self.x_0, self.y_0 + self.l, fill=color)
    canvas.create_line(self.x_0 + self.w, self.y_0, self.x_0 + self.w, self.y_0 + self.l, fill=color)
    canvas.create_line(self.x_0, self.y_0 + self.l, self.x_0 + self.w, self.y_0 + self.l, fill=color)

  def inButton(self, x, y):
    return self.x_0 <= x and x <= self.x_0 + self.w and self.y_0 <= y and y <= self.y_0 + self.l

  def onClick(self):
    self.onClicked()

class NodeLayer(Button):
  def __init__(self, x_0, y_0, width, length, func, buttons):
    super.__init__(self, x_0, y_0, width, length, func)
    self.isClicked = False
    self.buttonList = buttons

  def inButton(self, x, y):
    if self.x_0 <= x and x <= self.x_0 + self.w and self.y_0 <= y and y <= self.y_0 + self.l:
      self.isClicked = True
      return True
    self.isClicked = False
    return False

  def drawButton(self, canvas):
      if self.isClicked:
        super.drawButton(self, canvas, color="red")

class AddButton(Button):
  def __init__(self, x_0, y_0, width, length, func):
    super.__init__(self, x_0, y_0, width, length, func)
    self.isClicked = False
  
  def inButton(self, x, y):
    if self.x_0 <= x and x <= self.x_0 + self.w and self.y_0 <= y and y <= self.y_0 + self.l:
      self.isClicked = True
      return True
    self.isClicked = False
    return False

  def drawButton(self, canvas):
      if self.isClicked:
        super.drawButton(self, canvas)
        canvas.create_line((self.x_0 + self.w)/2, self.y + self.l/8, (self.x_0 + self.w)/2, self.y + self.l/8*7)
        canvas.create_line(self.x + self.w/8 , (self.y_0 + self.l)/2, self.x + self.w/8*7, (self.y_0 + self.l)/2)
