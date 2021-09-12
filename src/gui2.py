import tkinter
import entity
from network import *

BACKGROUND='white'


Mouse_x, Mouse_y = 0, 0

network = None

def updateMousePos(event):
  global Mouse_x, Mouse_y
  Mouse_x, Mouse_y = event.x, event.y

def handleMouseMove(event):
  updateMousePos(event)
  
def KeyRelease(event):
  global network
  if event.char == "d":
      network.addNode(2)
  elif event.char == "f":
      network.removeNode(2)
  elif event.char == "z":
      network.addLayer(0)
  elif event.char == "x":
      network.removeLayer(0)
  canvas.delete("all")
  network.drawNetwork(canvas)
  

def handleMouseDrag(event):
  global root, canvas, network, Mouse_x, Mouse_y 
  x, y = event.x, event.y
  entity.Offset_x += x - Mouse_x
  entity.Offset_y += y - Mouse_y
  updateMousePos(event)
  canvas.delete("all")
  network.drawNetwork(canvas)

def handleMousePress(event):
  global network, canvas

  network.mouseClick(event.x, event.y)
  canvas.delete("all")
  network.drawNetwork(canvas)

def main(width=800, height=600):
  global root, canvas, network
  
  root = tkinter.Tk()
  try:
      root.attributes('-type', 'dialog')
      print('Entering floating mode')
  except:
      pass

  network = Network()
  canvas = tkinter.Canvas(root, bg=BACKGROUND, height=height, width=width)
  canvas.pack()
  network.drawNetwork(canvas)
  root.bind('<B1-Motion>', handleMouseDrag)
  root.bind('<Motion>', handleMouseMove)
  root.bind('<Button-1>', handleMousePress)
  root.bind('<KeyRelease>', KeyRelease)
  #redrawAll(canvas)
  root.mainloop()
  
main()
