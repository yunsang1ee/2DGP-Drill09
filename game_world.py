world = [[],[],[]]

def addObject(object, depth):
    world[depth].append(object)
    pass

def removeObject(object):
    for layer in world:
        if object in layer:
            layer.remove(object)
            return True
    return False

def update():
    for layer in world:
        for o in layer:
            o.update()
    pass

def render():
    for layer in world:
        for o in layer:
            o.draw()
    pass