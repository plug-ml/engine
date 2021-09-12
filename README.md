# PlugML
A PennApps XXII submission by the _Carnegie Felons_

[![yt video](https://img.youtube.com/vi/BUKXlUkaGOo/0.jpg)](https://www.youtube.com/watch?v=BUKXlUkaGOo)

# Story
## Inspiration
Once upon a time, a systems engineer wanted to learn machine learning. They tried and failed. Then, they met a machine learning engineer, and together they brought together a team to make machine learning easy.

## What it does
PlugML provides two components: the **PlugML Engine** and the **Endpoint Library**. The **engine** is a hands-on visual application that allows users to easily design neural networks. App developers can then use the very simple **endpoint library** to connect their applications through a pipeline to the engine in real time.

The engine has two modes: *training* and *testing*. In *training* mode, the engine will consume data points and their corresponding labels from the pipeline to develop a learnt neural network model. In *testing* mode, the engine will be able to make predictions on input data from the pipeline based on the model and transmit the results back through the pipeline to the app.

## How we built it
The **Endpoint Library** is a simple python library compressed into a *whl* file for easy pip install.

The **PlugML Engine** is a *tkinter* application with visuals displayed on *canvas*. The machine learning back-end is powered by *tensorflow*. The pipeline between the engine and a developed app is implemented using *TCP* sockets.

## Challenges we ran into
UI.

## Accomplishments that we're proud of
Successfully integrating a neural network into a simple, easy-to-use user interface.

## What we learned
UI is hard and requires systematic planning and delegation.

## What's next for PlugML
More ML features! (CNN, DQN, KNN, A*, etc.)

# Usage
Git clone the repo and run `python src/main.py` to launch the engine. Here is the code for the sample projects used in the presentation video:

## Sine curve (-4, 4)
### Training
```
import math
import plugml.ipc as ipc
import random

x_data = []
y_data = []
for i in range(int(input('train size: '))):
  x = random.uniform(-4, 4)
  y = math.sin(x)
  x_data.append(x)
  y_data.append(y)

ipc.connect(int(input('port: ')))
ipc.transmit_list(x_data)
ipc.transmit_list(y_data)
```
### Testing
```
import math
import plugml.ipc as ipc
import random

port = int(input('port: '))
while True:
  ipc.connect(port)
  x = random.uniform(-4, 4)
  y = math.sin(x)
  ipc.transmit_list([x])
  data = ipc.retrieve_mapped_list(float)
  prediction = data[0]
  error = (prediction - y)**2
  print('x:', x)
  print('y', y)
  print('predict', prediction)
  print('err', error)
  print('')
```
