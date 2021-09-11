
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
    super().__init__(x_0, y_0, width, length, func)
    self.isClicked = False
    self.buttonList = buttons
    self.pmButtons = []


  def inButton(self, x, y):
    if self.x_0 <= x and x <= self.x_0 + self.w and self.y_0 <= y and y <= self.y_0 + self.l:
      for button in self.pmButtons:
        button.inButton(x, y)
    
      self.isClicked = True
      leftAddButt = AddButton(self.x_0, self.y_0, self.w/3, self.y_0 + self.l/8, lambda: print("+"))
      rightaddButt = AddButton(self.x_0 + self.w*2/3, self.y_0, self.w/3, self.y_0 + self.l/8, lambda: print("+"))
      minusButton = AddButton(self.x_0 + self.w/3, self.y_0, self.w/3, self.y_0 + self.l/8, lambda: print("-"))
      self.pmButtons += [leftAddButt, rightaddButt, minusButton]
      return True
    if self.isClicked and  False:
      pass
    self.isClicked = False
    self.pmButtons = []
    return False

  def drawButton(self, canvas):
    if self.isClicked:
      super().drawButton(canvas, color="red")
      for button in self.pmButtons:
        button.drawButton(canvas)



class AddButton(Button):
  def __init__(self, x_0, y_0, width, length, func):
    super().__init__(x_0, y_0, width, length, func)
    self.isClicked = False
  
  def inButton(self, x, y):
    if self.x_0 <= x and x <= self.x_0 + self.w and self.y_0 <= y and y <= self.y_0 + self.l:
      self.isClicked = True
      self.onClicked()
      return True
    self.isClicked = False
    return False

  def drawButton(self, canvas):
    super().drawButton(canvas)
    canvas.create_line((self.x_0 + self.w)/2, self.y_0 + self.l/8, (self.x_0 + self.w)/2, self.y_0 + self.l/8*7)
    canvas.create_line(self.x_0 + self.w/8 , (self.y_0 + self.l)/2, self.x_0 + self.w/8*7, (self.y_0 + self.l)/2)
