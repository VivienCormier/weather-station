import time
import board
import busio
import adafruit_veml6075

i2c = busio.I2C(board.SCL, board.SDA)

veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)

print("Integration time: %d ms" % veml.integration_time)

while True:
    print("UV Index: %s UV A: %s UV B: %s" % (veml.uv_index, veml.uva, veml.uvb))
    time.sleep(1)
