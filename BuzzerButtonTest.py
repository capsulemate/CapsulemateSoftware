## Buzzer Button Test
import time
from gpiozero import Button, Buzzer


BuzzerGPIO = 13
RedButton = 5
YellowButton = 6
GreenButton = 12

buzzer = Buzzer(BuzzerGPIO)
buzzer.on()
time.sleep(0.5)
buzzer.off()
time.sleep(1)

RedButton = Button(RedButton)
YellowButton = Button(YellowButton)
GreenButton = Button(GreenButton)

RedButton.wait_for_press()
print('Red Button')
YellowButton.wait_for_press()
print('Yellow Button')
GreenButton.wait_for_press()
print('Green Button')


