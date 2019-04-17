from gpiozero import MCP3008

import time
import math


adc = MCP3008(channel=0)
count = 0
volts = {0.4: "n",
         1.4: "n-e",
         1.2: "n-e",
         2.8: "e",
         2.7: "e",
         2.9: "s-e",
         2.3: "s-e",
         2.2: "s-e",
         2.5: "s-e",
         1.8: "s",
         2.0: "s-w",
         0.7: "s-w",
         0.8: "s-w",
         0.1: "w",
         0.3: "w",
         0.2: "n-w",
         0.6: "n-w"}


def get_average(angles):
    sin_sum = 0.0
    cos_sum = 0.0

    for angle in angles:
        r = math.radians(angle)
        sin_sum += math.sin(r)
        cos_sum += math.cos(r)

    flen = float(len(angles))
    s = sin_sum / flen
    c = cos_sum / flen
    arc = math.degrees(math.atan(s / c))
    average = 0.0

    if s > 0 and c > 0:
        average = arc
    elif c < 0:
        average = arc + 180
    elif s < 0 and c > 0:
        average = arc + 360

    return 0.0 if average == 360 else average


def get_value(length=5):
    data = []
    print("Measuring wind direction for %d seconds..." % length)
    start_time = time.time()

    while time.time() - start_time <= length:
        wind = round(adc.value * 3.3, 1)
        if wind not in volts:  # keep only good measurements
            print('unknown value ' + str(wind))
        else:
            data.append(volts[wind])

    return get_average(data)


while True:
    wind = round(adc.value * 3.3, 1)
    if wind not in volts:
        print('unknown value ' + str(wind))
    else:
        print('found ' + str(wind) + ' ' + str(volts[wind]))
