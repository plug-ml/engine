import tkinter

BACKGROUND='white'

button_list = []

class Button:
  def __init__(self, x_0, y_0, width, length, func):
    self.x_0 = x_0
    self.y_0 = y_0
    self.w = width
    self.l = length
    self.func = func

  def drawButton(self, canvas):
    canvas.create_line(self.x_0, self.y_0, self.x_0 + self.w, self.y_0)
    canvas.create_line(self.x_0, self.y_0, self.x_0, self.y_0 + self.l)
    canvas.create_line(self.x_0 + self.w, self.y_0, self.x_0 + self.w, self.y_0 + self.l)
    canvas.create_line(self.x_0, self.y_0 + self.l, self.x_0 + self.w, self.y_0 + self.l)

  def inButton(self, x, y):
    return self.x_0 <= x and x <= self.x_0 + self.w and self.y_0 <= y and y <= self.y_0 + self.l

  def onClick(self):
    self.func()

def MousePos(event):
  x,y = event.x, event.y
  return x,y

def MousePress(event):
  for button in button_list:
    if button.inButton(event.x,event.y):
      button.onClick()

def KeyPressed(event):
  pass

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
