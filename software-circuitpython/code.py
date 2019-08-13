## CircuitPython Imports
import digitalio
import analogio
import pulseio
import busio
import supervisor
import board
import time
import neopixel

## Local Imports
import adafruit_max31865 as max31865
import vnh5019

def mean(data):
    return sum(data)/float(len(data))

def _ss(data):
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def stddev(data, ddof=0):
    ss = _ss(data)
    pvar = ss/(len(data)-ddof)
    return pvar**0.5

RTD_NOMINAL   = 1000.0  ## Resistance of RTD at 0C
RTD_REFERENCE = 4300.0  ## Value of reference resistor on PCB

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

## Create SPI Chip Select pins
cs1  = digitalio.DigitalInOut(board.D10)
cs2  = digitalio.DigitalInOut(board.D9)
cs3  = digitalio.DigitalInOut(board.D6)
cs4  = digitalio.DigitalInOut(board.D5)
css  = [cs1, cs2, cs3, cs4]

sensors = []
pixel = False

if hasattr(board, 'NEOPIXEL'):
    led = neopixel.NeoPixel(board.NEOPIXEL, 1)
    led.brightness = 0.3
    pixel = True

## Create array for the RTD sensors on the SenseTemp Wing
for cs in css:
    cs.switch_to_output(digitalio.DriveMode.PUSH_PULL)

    sensors.append(
        max31865.MAX31865(
            spi, cs,
            wires        = 4,
            rtd_nominal  = RTD_NOMINAL,
            ref_resistor = RTD_REFERENCE
        )
    )

redled = digitalio.DigitalInOut(board.D13)
redled.switch_to_output(digitalio.DriveMode.PUSH_PULL)

ON = 0.05

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0:
        return 0, 0, 0

    if pos > 255:
        return 255, 0, 0

    if pos < 85:
        return int(255 - pos * 3), int(pos * 3), 0

    if pos < 170:
        pos -= 85
        return 0, int(255 - pos * 3), int(pos * 3)

    pos -= 170
    return int(pos * 3), 0, int(255 - (pos * 3))




pins = dict(
    ina=board.A0, inb=board.A1,
    diaga=board.A3, diagb=board.A2, 
    pwm=board.D11, fb=board.A4
)

vnh = vnh5019.VNH5019(pins)
aux = pulseio.PWMOut(board.TX, frequency=100) 

def fan(value):
    aux.duty_cycle = value

def tec(value):
    vnh.set(value)

def temps():
    data = [sensor.temperature for sensor in sensors]
    print(data)

while True:
    # print("faults  : {} {}".format(*vnh.faults()))
    # print("current : {}".format(vnh.current()))

    led.value = True
    time.sleep(ON)
    led.value = False
    time.sleep(1.0 - ON)

    data = [sensor.temperature for sensor in sensors]

    if pixel:
        # Scale and reverse colors so that high temperatures (30C) -> red color
        color = 255 - data[0]*7
        led.fill(wheel(int(color)))

    if supervisor.runtime.serial_connected:
        print(data, mean(data), max(data) - min(data), stddev(data))
        time.sleep(0.3)

    time.sleep(0.2)


