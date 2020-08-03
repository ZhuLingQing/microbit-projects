_thretholdInner = 50
_thretholdOuter = 200
def drawDrop(_center):
    led.plot(_center[0],_center[1])
    #led.plot(_center[0]-1,_center[1])
    #led.plot(_center[0]+1,_center[1])
    #led.plot(_center[0],_center[1]-1)
    #led.plot(_center[0],_center[1]+1)
def undrawDrop(_center):
    led.unplot(_center[0],_center[1])
    #led.unplot(_center[0]-1,_center[1])
    #led.unplot(_center[0]+1,_center[1])
    #led.unplot(_center[0],_center[1]-1)
    #led.unplot(_center[0],_center[1]+1)

def getDimension(_point):
    global _thretholdInner,_thretholdOuter
    if _point < (_thretholdOuter * -1):
        return 0
    elif _point < (_thretholdInner * -1):
        return 1
    elif _point > _thretholdOuter:
        return 4
    elif _point > _thretholdInner:
        return 3
    else:
        return 2

drop_default = [2,2]
def on_forever():
    global drop_default
    drop_now = []
    drop_now[0] = getDimension(input.acceleration(Dimension.X))
    drop_now[1] = getDimension(input.acceleration(Dimension.Y))
    if drop_now != drop_default:
        undrawDrop(drop_default)
    drawDrop(drop_now)
    drop_default = drop_now
basic.forever(on_forever)

