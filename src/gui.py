import tkinter
from typing import Collection

BACKGROUND='white'

# stuff to work on: order in which things are drawn, how we should draw listnode by listnode and all 
# child objects in each listnode from top to bottom. Each listnode also has a list of addbuttons as well.

fbutton_list = []
button_list = []

def MousePos(event):
  x,y = event.x, event.y
  return x,y

def MousePress(event):
  for button in button_list:
    if button.inButton(event.x,event.y):
      button.onClick()

def KeyPressed(event):
  pass


class Button:
  def __init__(self, x_0, y_0, width, length, func):
    self.x_0 = x_0
    self.y_0 = y_0
    self.w = width
    self.l = length
    self.func = func

  def drawButton(self, canvas, color = "black"):
    canvas.create_line(self.x_0, self.y_0, self.x_0 + self.w, self.y_0, color)
    canvas.create_line(self.x_0, self.y_0, self.x_0, self.y_0 + self.l, color)
    canvas.create_line(self.x_0 + self.w, self.y_0, self.x_0 + self.w, self.y_0 + self.l, color)
    canvas.create_line(self.x_0, self.y_0 + self.l, self.x_0 + self.w, self.y_0 + self.l, color)

  def inButton(self, x, y):
    return self.x_0 <= x and x <= self.x_0 + self.w and self.y_0 <= y and y <= self.y_0 + self.l

  def onClick(self):
    self.func()

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
        super.drawButton(self, canvas, color = "red")


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

# Need to add clicking an addbutton adds a listnode to the right or left of its parent listnode

def main(width=800, height=600):
  root = tkinter.Tk()
  try:
    root.attributes('-type', 'dialog')
    print('Entering floating mode')
  except:
    pass 
  canvas = tkinter.Canvas(root, bg=BACKGROUND, height=height, width=width)
  canvas.pack()

  for button in button_list:
    button.drawButton(canvas)
  
  root.bind('<Motion>', MousePos)
  root.bind('<Button-1>', MousePress)
  root.bind('<Key>', KeyPressed)
  root.mainloop()

main()
