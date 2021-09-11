import button

import tkinter

BACKGROUND='white'

# stuff to work on: order in which things are drawn, how we should draw listnode by listnode and all 
# child objects in each listnode from top to bottom. Each listnode also has a list of addbuttons as well.

fbutton_list = []
button_list = []




lyr = button.NodeLayer(50, 50, 50, 20, lambda: print('hi'))
lyr.nodes = 10
button_list.append(lyr)

def MousePos(event):
  x, y = event.x, event.y
  return x, y

def MousePress(event):
  for btn in button_list:
    if btn.inButton(event.x, event.y):
      btn.onClick()

def KeyPressed(event):
  pass

def redrawAll(canvas, root):
  canvas.delete("all")
  for button in button_list:
    button.draw(canvas)
  root.after(2000, lambda: redrawAll(canvas, root))

    
def main(width=800, height=600):
  root = tkinter.Tk()
  try:
    root.attributes('-type', 'dialog')
    print('Entering floating mode')
  except:
    pass 
  canvas = tkinter.Canvas(root, bg=BACKGROUND, height=height, width=width)
  canvas.pack()



  root.bind('<Motion>', MousePos)
  root.bind('<Button-1>', MousePress)
  root.bind('<Key>', KeyPressed)
  root.after(2000, lambda: redrawAll(canvas, root))
  root.mainloop()

  
main()
