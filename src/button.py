import entity

class Button(entity.Entity):
  def __init__(self, x, y, width, height, onClicked):
    super().__init__(x, y, width, height, is_static=False)
    self.onClicked = onClicked 

  def inButton(self, x, y):
    return self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height

  def onClick(self):
    self.onClicked()

class NodeLayer(Button):
  def __init__(self, x, y, width, height, func, buttons):
    super().__init__(x, y, width, height, func)
    self.isClicked = False
    self.buttonList = buttons
    self.pmButtons = []

  def inButton(self, x, y):
    if self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height:
      for button in self.pmButtons:
        button.inButton(x, y)
    
      self.isClicked = True
      if self.pmButtons == []:
        leftAddButt = AddButton(self.x, self.y, self.width / 3, self.y + self.height / 8, lambda: print("+"))
        rightaddButt = AddButton(self.x + self.width * 2 / 3, self.y, self.width / 3, self.y + self.height / 8, lambda: print("+"))
        minusButton = AddButton(self.x + self.width / 3, self.y, self.width / 3, self.y + self.height / 8, lambda: print("-"))
        self.pmButtons += [leftAddButt, rightaddButt, minusButton]
      return True
    if self.isClicked and False:
      pass
    self.isClicked = False
    self.pmButtons = []
    return False

  def drawButton(self, canvas):
    if self.isClicked:
      super().draw(canvas, color="red")
      for button in self.pmButtons:
        button.draw(canvas)



class AddButton(Button):
  def __init__(self, x, y, width, height, func):
    super().__init__(x, y, width, height, func)
    self.isClicked = False
  
  def inButton(self, x, y):
    if self.x <= x and x <= self.x + self.width and self.y <= y and y <= self.y + self.height:
      self.isClicked = True
      self.onClicked()
      return True
    self.isClicked = False
    return False

  def draw(self, canvas):
    super().draw(canvas)
    canvas.create_line((self.x + self.width)/2, self.y + self.height/8, (self.x + self.width)/2, self.y + self.height/8*7)
    canvas.create_line(self.x + self.width/8 , (self.y + self.height)/2, self.x + self.width/8*7, (self.y + self.height)/2)
