import time
from adafruit_servokit import ServoKit

left  = ServoKit(channels=16, address=0x40)
right = ServoKit(channels=16, address=0x41)

# BACK LEFT
left.servo[0].set_pulse_width_range(1500, 2700)
left.servo[0].actuation_range = 100

left.servo[1].set_pulse_width_range(450, 2400)
left.servo[1].actuation_range = 180

left.servo[2].set_pulse_width_range(500, 2000)
left.servo[2].actuation_range = 130

# FRONT RIGHT
right.servo[6].set_pulse_width_range(1600, 2500)
right.servo[6].actuation_range = 90

right.servo[7].set_pulse_width_range(450, 2400)
right.servo[7].actuation_range = 180

right.servo[8].set_pulse_width_range(500, 2000)
right.servo[8].actuation_range = 130

# BACK RIGHT
right.servo[0].set_pulse_width_range(550, 1300) # back, front
right.servo[0].actuation_range = 90

right.servo[1].set_pulse_width_range(750, 2500) # up, down
right.servo[1].actuation_range = 180

right.servo[2].set_pulse_width_range(600, 2000) # up, down
right.servo[2].actuation_range = 130

def blReset():
	left.servo[0].angle = 45
	left.servo[1].angle = 45
	left.servo[2].angle = 90

def brReset():
	right.servo[0].angle = 45
	right.servo[1].angle = 135
	right.servo[2].angle = 90

def frReset():
	right.servo[6].angle = 45
	right.servo[7].angle = 135
	right.servo[8].angle = 90

#  frReset()

servo_to_test = 7

time.sleep( 2 )

right.servo[servo_to_test].angle = 180

time.sleep( 2 )

right.servo[servo_to_test].angle = 0
