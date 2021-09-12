import button
import entity

import tkinter

BACKGROUND='white'

root, canvas, prior_button_list, button_list  = None, None, None, None

Mouse_x, Mouse_y = 0, 0

nn = [1]



def updateMousePos(event):
  global Mouse_x, Mouse_y
  Mouse_x, Mouse_y = event.x, event.y

def handleMouseMove(event):
  updateMousePos(event)
  
def handleMouseDrag(event):
  global root, canvas, Mouse_x, Mouse_y 
  x, y = event.x, event.y
  entity.Offset_x += x - Mouse_x
  entity.Offset_y += y - Mouse_y
  updateMousePos(event)
  redrawAll(canvas, root)

def handleMousePress(event):
  global prior_button_list
  inButtonList = False
  for btn in prior_button_list:
      if btn.inButton(event.x, event.y):
        inButtonList = True
  if not inButtonList:
    prior_button_list = []

  for btn in button_list:
    if btn.inButton(event.x, event.y):
      btn.onClick()


def redrawAll(canvas, root):
  canvas.delete("all")
  for button in button_list:
    button.draw(canvas)
        
def main(width=800, height=600):
  global root, canvas, prior_button_list, button_list 
  
  prior_button_list = []
  button_list = []

  lyr = button.NodeLayer(50, 50, 50, 20, lambda: print("hi"), 0)
  lyr.nodes = 10
  button_list.append(lyr)

  root = tkinter.Tk()
  try:
    root.attributes('-type', 'dialog')
    print('Entering floating mode')
  except:
    pass 
  canvas = tkinter.Canvas(root, bg=BACKGROUND, height=height, width=width)
  canvas.pack()

  root.bind('<B1-Motion>', handleMouseDrag)
  root.bind('<Motion>', handleMouseMove)
  root.bind('<Button-1>', handleMousePress)
  root.bind('<Key>', KeyPressed)
  redrawAll(canvas, root)
  root.mainloop()
  
main()
