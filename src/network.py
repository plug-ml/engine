import entity

NODE_WIDTH = 40
NODE_GAP = 20
LAYER_GAP = 60
LAYER_BUFFER = 10
TECH_BUTTON_DIM = NODE_WIDTH - 2 * LAYER_BUFFER


class Layer(entity.Entity):
    def __init__(self, index, num_nodes):
        self.is_static = False
        self.index = index
        self.num_nodes = num_nodes

    def draw(self, canvas, width):
        x, y = self.getPos(width)
        for i in range(self.num_nodes):
            canvas.create_oval(x, y + (NODE_WIDTH + NODE_GAP) * i, x + NODE_WIDTH, y + (NODE_WIDTH + NODE_GAP) * i + NODE_WIDTH, fill='white')
    
    def getPos(self, width):
        x = 400 - width/2 + self.index * (NODE_WIDTH + LAYER_GAP)
        y = 300 - (self.num_nodes*NODE_WIDTH + (self.num_nodes - 1)*NODE_GAP)/2
        if not self.is_static:
            x += entity.Offset_x
            y += entity.Offset_y
        return x, y   

    def getOutline(self):
        return NODE_WIDTH, NODE_WIDTH * self.num_nodes + NODE_GAP * (self.num_nodes - 1)

    def incNode(self):
        self.num_nodes += 1
    
    def decNode(self):
        if self.num_nodes > 1:
            self.num_nodes -= 1
    
    def incNodesTechPos(self, width):
        x, y = self.getPos(width)
        _, height = self.getOutline()
        return x + LAYER_BUFFER, y - TECH_BUTTON_DIM / 2

    def decNodesTechPos(self, width):
        x, y = self.getPos(width)
        _, height = self.getOutline()
        return x + LAYER_BUFFER, y + height - TECH_BUTTON_DIM / 2

    # TODO: delete
    def inLayer(self, x, y, width):
        x_left, y_top = self.getPos(width)
        x_right = x_left + NODE_WIDTH
        y_bot = y_top + (self.num_nodes*NODE_WIDTH + (self.num_nodes - 1)*NODE_GAP)
        return x >= x_left and x <= x_right and y <= y_bot and y >= y_top

class Network:
    def __init__(self):
        self.layer_list = []
        self.addLayer(0)
        self.highlighted = -1

    def addLayer(self, index, num_nodes = 1):
        self.layer_list.insert(index, Layer(index, num_nodes))
        for i in range(index + 1, len(self.layer_list)):
            self.layer_list[i].index += 1

    def removeLayer(self, index):
        if len(self.layer_list) > 1:
            self.layer_list.pop(index)
            for i in range(index, len(self.layer_list)):
                self.layer_list[i].index -= 1

    def width(self):
        n = len(self.layer_list)
        return n * NODE_WIDTH + (n - 1) * LAYER_GAP

    def drawNetwork(self, canvas):
        for l in self.layer_list:
            l.draw(canvas, self.width())
        if self.highlighted >= len(self.layer_list):
            self.highlighted = -1
        if self.highlighted != -1:
            layer = self.layer_list[self.highlighted]
            x, y = layer.getPos(self.width())
            width, height = layer.getOutline()
            canvas.create_rectangle(x - LAYER_BUFFER, y - LAYER_BUFFER, x + width + LAYER_BUFFER, y + height + LAYER_BUFFER, outline = "blue", dash=(4, 2))

            incNodes_x, incNodes_y = layer.incNodesTechPos(self.width())
            decNodes_x, decNodes_y = layer.decNodesTechPos(self.width())

            canvas.create_line(incNodes_x, y, incNodes_x + TECH_BUTTON_DIM, y, fill = 'blue')
            canvas.create_line(x + NODE_WIDTH / 2, incNodes_y, x + NODE_WIDTH / 2, incNodes_y + TECH_BUTTON_DIM, fill = 'blue')
            canvas.create_oval(incNodes_x, incNodes_y, incNodes_x + TECH_BUTTON_DIM, incNodes_y + TECH_BUTTON_DIM, outline = 'blue')

            canvas.create_line(decNodes_x, y + height, decNodes_x + TECH_BUTTON_DIM, y + height, fill = 'red')
            canvas.create_oval(decNodes_x, decNodes_y, decNodes_x + TECH_BUTTON_DIM, decNodes_y + TECH_BUTTON_DIM, outline = 'red')

    def mouseClick(self, x, y):
        if self.highlighted >= len(self.layer_list):
            self.hightlighted = -1
        if self.highlighted != -1:
            layer = self.layer_list[self.highlighted]
            incNodes_x, incNodes_y = layer.incNodesTechPos(self.width())
            decNodes_x, decNodes_y = layer.decNodesTechPos(self.width())
            if incNodes_x <= x <= incNodes_x + TECH_BUTTON_DIM and incNodes_y <= y <= incNodes_y + TECH_BUTTON_DIM:
                layer.incNode()
                return
            if decNodes_x <= x <= decNodes_x + TECH_BUTTON_DIM and decNodes_y <= y <= decNodes_y + TECH_BUTTON_DIM:
                layer.decNode()
                return
        for i in range(len(self.layer_list)):
            layer = self.layer_list[i]
            x_left, y_top = layer.getPos(self.width())
            width, height = layer.getOutline()
            if y_top <= y and y <= y_top + height and x_left <= x and x <= x_left + width:
                self.highlighted = i
                return
        self.highlighted = -1
    
    def addNode(self, layer):
        self.layer_list[layer].incNode()

    def removeNode(self, layer):
        self.layer_list[layer].decNode()
