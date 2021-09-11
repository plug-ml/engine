import button
import entity

import tkinter

BACKGROUND='white'

# stuff to work on: order in which things are drawn, how we should draw listnode by listnode and all 
# child objects in each listnode from top to bottom. Each listnode also has a list of addbuttons as well.

root, canvas = None, None

Mouse_x, Mouse_y = 0, 0

fbutton_list = []
button_list = []

lyr = button.NodeLayer(50, 50, 50, 20, lambda: print('hi'))
lyr.nodes = 10
button_list.append(lyr)

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
  for btn in button_list:
    if btn.inButton(event.x, event.y):
      btn.onClick()

def KeyPressed(event):
  pass

def redrawAll(canvas, root):
  canvas.delete("all")
  for button in button_list:
    button.draw(canvas)
    
def main(width=800, height=600):
  global root, canvas
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
