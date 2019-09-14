import time
from adafruit_servokit import ServoKit

left  = ServoKit(channels=16, address=0x40)
right = ServoKit(channels=16, address=0x41)

front_right = [
	{
		"index": 0,
		"pulse_width_range": [ 1600, 2500 ],
		"actuation_range":   90,
	},
	{
		"index": 1,
		"pulse_width_range": [ 1200, 2750 ],
		"actuation_range":   180,
	},
	{
		"index": 2,
		"pulse_width_range": [ 500, 2000 ],
		"actuation_range":   130,
	},
]

mid_right = [
	{
		"index": 3,
		"pulse_width_range": [ 2200, 2500 ],
		"actuation_range":   90,
	},
	{
		"index": 4,
		"pulse_width_range": [ 550, 2500 ],
		"actuation_range":   180,
	},
	{
		"index": 5,
		"pulse_width_range": [ 600, 2000 ],
		"actuation_range":   130,
	},
]

back_right = [
	{
		"index": 6,
		"pulse_width_range": [ 550, 1300 ],
		"actuation_range":   90,
	},
	{
		"index": 7,
		"pulse_width_range": [ 750, 2500 ],
		"actuation_range":   180,
	},
	{
		"index": 8,
		"pulse_width_range": [ 600, 2000 ],
		"actuation_range":   130,
	},
]

front_left = [
	{
		"index": 15,
		"pulse_width_range": [ 550, 1300 ],
		"actuation_range":   90,
	},
	{
		"index": 14,
		"pulse_width_range": [ 750, 2500 ],
		"actuation_range":   180,
	},
	{
		"index": 13,
		"pulse_width_range": [ 600, 2000 ],
		"actuation_range":   130,
	},
]

mid_left = [
	{
		"index": 12,
		"pulse_width_range": [ 550, 1300 ],
		"actuation_range":   90,
	},
	{
		"index": 11,
		"pulse_width_range": [ 750, 2500 ],
		"actuation_range":   180,
	},
	{
		"index": 10,
		"pulse_width_range": [ 600, 2000 ],
		"actuation_range":   130,
	},
]

back_left = [
	{
		"index": 9,
		"pulse_width_range": [ 1600, 2500 ],
		"actuation_range":   90,
	},
	{
		"index": 8,
		"pulse_width_range": [ 1200, 2750 ],
		"actuation_range":   180,
	},
	{
		"index": 7,
		"pulse_width_range": [ 500, 2000 ],
		"actuation_range":   130,
	},
]

legs_right = [
	front_right,
	mid_right,
	back_right,
]

legs_left = [
	front_left,
	mid_left,
	back_left,
]

for joints in legs_right:
	for joint in joints:
		right.servo[joint["index"]].set_pulse_width_range(*joint["pulse_width_range"])
		right.servo[joint["index"]].actuation_range = joint["actuation_range"]

for joints in legs_left:
	for joint in joints:
		left.servo[joint["index"]].set_pulse_width_range(*joint["pulse_width_range"])
		left.servo[joint["index"]].actuation_range = joint["actuation_range"]

# BACK LEFT
left.servo[6].set_pulse_width_range(1500, 2700)
left.servo[6].actuation_range = 100

left.servo[7].set_pulse_width_range(450, 2400)
left.servo[7].actuation_range = 180

left.servo[8].set_pulse_width_range(500, 2000)
left.servo[8].actuation_range = 130

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

servo_to_test = 0

time.sleep( 2 )

right.servo[servo_to_test].angle = 90

time.sleep( 2 )

right.servo[servo_to_test].angle = 0
