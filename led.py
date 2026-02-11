from gpiozero import LED
import time

# led = LED(26)
# led.on()
# time.sleep(3)
# led.off()

led = LED(26)

while True:
	led.on()
	sleep(1)
	led.off()
	sleep(1)

