from pyfirmata import Arduino,util
import serial
import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

led = board.digital[13]

while True:
    led.write(1)
    time.sleep(1)
    led.write(0)
    time.sleep(1)