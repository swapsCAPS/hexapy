import time
from adafruit_servokit import ServoKit

left  = ServoKit(channels=16, address=0x40)
right = ServoKit(channels=16, address=0x41)

front_right = [
	{
		"is_calibrated":     True,
		"index":             0,
		"pulse_width_range": [ 1600, 2500 ], # first is backward
		"actuation_range":   90,
		"resting":           60,
	},
	{
		"is_calibrated":     True,
		"index":             1,
		"pulse_width_range": [ 450, 2000 ], # first is downward
		"actuation_range":   130,
		"resting":           0,
	},
	{
		"is_calibrated":     True,
		"index":             2,
		"pulse_width_range": [ 500, 2000 ], # first is inward
		"actuation_range":   130,
		"resting":           30,
	},
]

mid_right = [
	{
		"is_calibrated":     True,
		"index": 3,
		"pulse_width_range": [ 1300, 1900 ],
		"actuation_range":   90,
		"resting":           45,
	},
	{
		"is_calibrated":     True,
		"index": 4,
		"pulse_width_range": [ 510, 2000 ],
		"actuation_range":   130,
		"resting":           0,
	},
	{
		"is_calibrated":     True,
		"index": 5,
		"pulse_width_range": [ 550, 2200 ],
		"actuation_range":   130,
		"resting":           30,
	},
]

back_right = [
	{
		"is_calibrated":     True,
		"index": 6,
		"pulse_width_range": [ 520, 1380 ],
		"actuation_range":   90,
		"resting":           45,
	},
	{
		"is_calibrated":     True,
		"index": 7,
		"pulse_width_range": [ 460, 2000 ],
		"actuation_range":   180,
		"resting":           0,
	},
	{
		"is_calibrated":     True,
		"index": 8,
		"pulse_width_range": [ 750, 2050 ],
		"actuation_range":   130,
		"resting":           30,
	},
]

front_left = [
	{
		"is_calibrated":     True,
		"index": 15,
		"pulse_width_range": [ 550, 1350 ], # first is forward
		"actuation_range":   90,
		"resting":           45,
	},
	{
		"is_calibrated":     True,
		"index": 14,
		"pulse_width_range": [ 900, 2380 ], # first is upward
		"actuation_range":   130,
		"resting":           130,
	},
	{
		"is_calibrated":     True,
		"index": 13,
		"pulse_width_range": [ 1100, 2650 ], # first is outward
		"actuation_range":   130,
		"resting":           90,
	},
]

mid_left = [
	{
		"is_calibrated":     True,
		"index": 12,
		"pulse_width_range": [ 1300, 1900 ],
		"actuation_range":   90,
		"resting":           45,
	},
	{
		"is_calibrated":     True,
		"index": 11,
		"pulse_width_range": [ 900, 2550 ], # first is upward
		"actuation_range":   130,
		"resting":           130,
	},
	{
		"is_calibrated":     True,
		"index": 10,
		"pulse_width_range": [ 1000, 2650 ],
		"actuation_range":   130,
		"resting":           90,
	},
]

back_left = [
	{
		"is_calibrated":     True,
		"index": 9,
		"pulse_width_range": [ 1580, 2500 ],
		"actuation_range":   90,
		"resting":           60,
	},
	{
		"is_calibrated":     True,
		"index": 8,
		"pulse_width_range": [ 1200, 2730 ], # first is upward
		"actuation_range":   130,
		"resting":           130,
	},
	{
		"is_calibrated":     True,
		"index": 7,
		"pulse_width_range": [ 1200, 2650 ],
		"actuation_range":   130,
		"resting":           90,
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

def reset_leg(side, leg):
	for servo in leg:
		side.servo[servo["index"]].angle = servo["resting"]

def disable_leg(side, leg):
	for servo in leg:
		side.servo[servo["index"]].angle = None

leg_to_test = back_left

#  disable_leg(left, leg_to_test)
#  time.sleep(1)

for servo in leg_to_test:
	if servo["is_calibrated"]:
		continue

	left.servo[servo["index"]].angle = servo["actuation_range"]
	print(servo["actuation_range"])

	time.sleep( 2 )

	left.servo[servo["index"]].angle = 0
	print(0)

	time.sleep( 2 )

	left.servo[servo["index"]].angle = servo["resting"]

	time.sleep( 2 )

	left.servo[servo["index"]].angle = None

	time.sleep( 1 )
	#  reset_leg(left, leg_to_test)

	#  time.sleep( 1 )

	#  disable_leg(left, leg_to_test)

	#  time.sleep( 1 )

#  for leg in legs_right:
	#  reset_leg(right, leg)

#  time.sleep( 1 )

#  for leg in legs_right:
	#  disable_leg(right, leg)
