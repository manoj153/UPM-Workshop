import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

print("helo press the button to on the LED")

try:
 while 1:
  if GPIO.input(24):
   GPIO.output(23, GPIO.LOW)
  else:
   GPIO.output(23, GPIO.HIGH)

except KeyboardInterrupt:
 GPIO.cleanup()
