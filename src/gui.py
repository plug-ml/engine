import button

import tkinter

BACKGROUND='white'

# stuff to work on: order in which things are drawn, how we should draw listnode by listnode and all 
# child objects in each listnode from top to bottom. Each listnode also has a list of addbuttons as well.

fbutton_list = []
button_list = []


btn = button.Button(50, 50, 200, 200, lambda: print('hi'))
button_list.append(btn)

def MousePos(event):
  x, y = event.x, event.y
  return x, y

def MousePress(event):
  for btn in button_list:
    if btn.inButton(event.x, event.y):
      btn.onClick()

def KeyPressed(event):
  pass
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
