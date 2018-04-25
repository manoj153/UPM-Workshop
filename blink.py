import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

print("Let's watch LED Blinking")

try:
	while 1:
		GPIO.output(23, GPIO.LOW)
		time.sleep(0.5)
		GPIO.output(23, GPIO.HIGH)
		time.sleep(0.5)

except KeyboardInterrupt: 
	GPIO.cleanup()
