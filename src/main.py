import tkinter

import button
import entity
import ipc
from network import *
import nn

BACKGROUND='white'


Mouse_x, Mouse_y = 0, 0

network = None
model = None

def draw_run_button(canvas, x, y, width, height):
  color = 'green'
  offset = 10
  canvas.create_oval(x, y, x + width, y + width, outline=color)
  canvas.create_line(x + offset, y + offset, x + offset, y + height - offset)
  canvas.create_line(x + width - offset, y + height / 2, x + offset, y + height - offset)
  canvas.create_line(x + width - offset, y + height / 2, x + offset, y + offset)

def run():
  params_dict = {"num_inputs": network.layer_list[0].num_nodes, "layer_sizes": list(map(lambda x: x.num_nodes, network.layer_list[1:]))}
  ipc.start()
  data = ipc.get_mapped_list(float)
  data = list(nn.test_network(data, model).flatten())
  ipc.send_list(data)
  # run nn into data
  # ipc.send_list(data)

def draw_train_button(canvas, x, y, width, height):
  color = 'purple'
  offset = 10
  canvas.create_oval(x, y, x + width, y + width, outline=color)
  canvas.create_line(x + offset, y + offset, x + width - offset, y + offset)
  canvas.create_line(x + width / 2, y + offset, x + width / 2, y + height - offset)

def train():
  global model
  input_size = network.layer_list[0].num_nodes
  params_dict = {"num_inputs": input_size, "layer_sizes": list(map(lambda x: x.num_nodes, network.layer_list[1:]))}
  ipc.start()
  inputs = ipc.get_mapped_list(float)
  outputs = ipc.get_mapped_list(float)
  model = nn.train_network(params_dict, inputs, outputs)

run_button = button.Button(10, 10, 50, 50, run, draw_run_button, is_static=True)
train_button = button.Button(70, 10, 50, 50, train, draw_train_button, is_static=True)

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
  redraw(canvas)
  

def handleMouseDrag(event):
  global root, canvas, network, Mouse_x, Mouse_y 
  x, y = event.x, event.y
  entity.Offset_x += x - Mouse_x
  entity.Offset_y += y - Mouse_y
  updateMousePos(event)
  redraw(canvas)

def handleMousePress(event):
  global network, canvas

  if run_button.inButton(event.x, event.y):
    run_button.onClick()
    return
  if train_button.inButton(event.x, event.y):
    train_button.onClick()
    return
  network.mouseClick(event.x, event.y)
  redraw(canvas)

def redraw(canvas):
  canvas.delete('all')
  network.drawNetwork(canvas)
  run_button.draw(canvas)
  train_button.draw(canvas)

def main(width=800, height=600):
  global root, canvas, network

  ipc.new(1234)  

  root = tkinter.Tk()
  try:
      root.attributes('-type', 'dialog')
      print('Entering floating mode')
  except:
      pass

  network = Network()
  canvas = tkinter.Canvas(root, bg=BACKGROUND, height=height, width=width)
  canvas.pack()
  redraw(canvas)
  root.bind('<B1-Motion>', handleMouseDrag)
  root.bind('<Motion>', handleMouseMove)
  root.bind('<Button-1>', handleMousePress)
  root.bind('<KeyRelease>', KeyRelease)
  #redrawAll(canvas)
  root.mainloop()
  
main()
