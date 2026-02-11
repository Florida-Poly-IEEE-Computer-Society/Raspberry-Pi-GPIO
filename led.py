from gpiozero import LED, Button
import time

# led = LED(26)
# led.on()
# time.sleep(3)
# led.off()

led = LED(26)

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)

