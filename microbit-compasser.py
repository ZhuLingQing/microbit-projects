
def getInnerPoint(_value):
    innerTable = (2,2,3,3,3,3,3,3,3,3,3,2,2,2,1,1,1,1,1,1,1,1,1,2)
    offsetX = 0
    offsetY = -6
    offsetX = (_value + offsetX + len(innerTable)) % len(innerTable)
    offsetY = (_value + offsetY + len(innerTable)) % len(innerTable)
    return (innerTable[offsetX],innerTable[offsetY])

def getOuterPoint(_value):
    outerTable = (2,3,3,4,4,4,4,4,4,4,3,3,2,1,1,0,0,0,0,0,0,0,1,1)
    offsetX = 0
    offsetY = -6
    offsetX = (_value + offsetX + len(outerTable)) % len(outerTable)
    offsetY = (_value + offsetY + len(outerTable)) % len(outerTable)
    return (outerTable[offsetX],outerTable[offsetY])

def drawHalfLine(_value):
    innerPoint = getInnerPoint(_value)
    led.plot(innerPoint[0], innerPoint[1])
    outerPoint = getOuterPoint(_value)
    led.plot(outerPoint[0], outerPoint[1])

def undrawHalfLine(_value):
    innerPoint = getInnerPoint(_value)
    led.unplot(innerPoint[0], innerPoint[1])
    outerPoint = getOuterPoint(_value)
    led.unplot(outerPoint[0], outerPoint[1])

compass_default = -1
led.plot(2,2)
def on_forever():
    global compass_default
    compass_value = int("" + str(input.compass_heading() / (360/24)))
    if compass_default != compass_value:
        undrawHalfLine(compass_default)
    drawHalfLine(compass_value)
    compass_default = compass_value
basic.forever(on_forever)

def on_button_pressed_ab():
    input.calibrate_compass()
input.on_button_pressed(Button.AB, on_button_pressed_ab)