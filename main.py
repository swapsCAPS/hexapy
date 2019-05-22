import time
from adafruit_servokit import ServoKit

left  = ServoKit(channels=16, address=0x40)
right = ServoKit(channels=16, address=0x41)

left.servo[0].set_pulse_width_range(1500, 2700)
left.servo[0].actuation_range = 100

left.servo[1].set_pulse_width_range(450, 2400)
left.servo[1].actuation_range = 180

left.servo[2].set_pulse_width_range(500, 2000)
left.servo[2].actuation_range = 130

def blReset():
	left.servo[0].angle = 45
	left.servo[1].angle = 45
	left.servo[2].angle = 90

servo_to_test = 2

time.sleep( 2 )

left.servo[servo_to_test].angle = 180

time.sleep( 2 )

left.servo[servo_to_test].angle = 0
