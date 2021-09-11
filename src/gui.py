import tkinter

BACKGROUND='white'

def main(width=800, height=600):
  root = tkinter.Tk()
  try:
    root.attributes('-type', 'dialog')
    print('Entering floating mode')
  except:
    pass 
  canvas = tkinter.Canvas(root, bg=BACKGROUND, height=height, width=width)
  canvas.pack()
  root.mainloop()

main()
