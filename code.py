import time
import board
import analogio
import array

print('Hello World')

length = 1000
mybuffer = array.array("H", [0] * length)
knob = analogio.AnalogFastIn(board.GP26, mybuffer)

t1 = time.monotonic()
knob.capture()
t2 = time.monotonic()
td = t2-t1

knob.deinit()

for i in range(999):
    print(i, mybuffer[i])
print('td', td)
