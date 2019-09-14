import time

from board import SCL, SDA
import busio

# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
left = PCA9685(i2c, address=0x40)
left.frequency = 50
right = PCA9685(i2c, address=0x41)
right.frequency = 50

front_right = [
	{
		# Lower is backward
		"is_calibrated":     True,
		"index":             0,
		"pulse_width_range": [ 1600, 2500 ],
		"actuation_range":   90,
		"resting":           60,
	},
	{
		# Lower is downward
		"is_calibrated":     True,
		"index":             1,
		"pulse_width_range": [ 450, 2000 ],
		"actuation_range":   130,
		"resting":           0,
	},
	{
		# Lower is outward
		"is_calibrated":     True,
		"index":             2,
		"pulse_width_range": [ 500, 2000 ],
		"actuation_range":   130,
		"resting":           30,
	},
]

mid_right = [
	{
		"is_calibrated":     False,
		"index": 3,
		"pulse_width_range": [ 1800, 2000 ],
		"actuation_range":   90,
		"resting":           45,
	},
	{
		"is_calibrated":     False,
		"index": 4,
		"pulse_width_range": [ 550, 2500 ],
		"actuation_range":   130,
		"resting":           0,
	},
	{
		"is_calibrated":     False,
		"index": 5,
		"pulse_width_range": [ 500, 2000 ],
		"actuation_range":   130,
		"resting":           30,
	},
]

back_right = [
	{
		"is_calibrated":     False,
		"index": 6,
		"pulse_width_range": [ 550, 1300 ],
		"actuation_range":   90,
	},
	{
		"is_calibrated":     False,
		"index": 7,
		"pulse_width_range": [ 750, 2500 ],
		"actuation_range":   180,
	},
	{
		"is_calibrated":     False,
		"index": 8,
		"pulse_width_range": [ 600, 2000 ],
		"actuation_range":   130,
	},
]

front_left = [
	{
		"is_calibrated":     False,
		"index": 15,
		"pulse_width_range": [ 550, 1300 ],
		"actuation_range":   90,
	},
	{
		"is_calibrated":     False,
		"index": 14,
		"pulse_width_range": [ 750, 2500 ],
		"actuation_range":   180,
	},
	{
		"is_calibrated":     False,
		"index": 13,
		"pulse_width_range": [ 600, 2000 ],
		"actuation_range":   130,
	},
]

mid_left = [
	{
		"is_calibrated":     False,
		"index": 12,
		"pulse_width_range": [ 550, 1300 ],
		"actuation_range":   90,
	},
	{
		"is_calibrated":     False,
		"index": 11,
		"pulse_width_range": [ 750, 2500 ],
		"actuation_range":   180,
	},
	{
		"is_calibrated":     False,
		"index": 10,
		"pulse_width_range": [ 600, 2000 ],
		"actuation_range":   130,
	},
]

back_left = [
	{
		"is_calibrated":     False,
		"index": 9,
		"pulse_width_range": [ 1600, 2500 ],
		"actuation_range":   90,
	},
	{
		"is_calibrated":     False,
		"index": 8,
		"pulse_width_range": [ 1200, 2750 ],
		"actuation_range":   180,
	},
	{
		"is_calibrated":     False,
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
	front_left,
]

servos_left = []
servos_right = []

for joints in legs_right:
	for joint in joints:
		index = joint["index"]
		args = {
			"min_pulse":       joint["pulse_width_range"][0],
			"max_pulse":       joint["pulse_width_range"][1],
			"actuation_range": joint["actuation_range"],
		}
		servos_right.insert(index, servo.Servo(right.channels[index], **args))

for joints in legs_left:
	for joint in joints:
		index              = joint["index"]
		args = {
			"min_pulse":       joint["pulse_width_range"][0],
			"max_pulse":       joint["pulse_width_range"][1],
			"actuation_range": joint["actuation_range"],
		}
		servos_left.insert(index, servo.Servo(left.channels[index], **args))

def reset_leg(side, leg):
	for servo in leg:
		side.servo[servo["index"]].angle = servo["resting"]
		time.sleep( 2 )

#  reset_leg(right, front_right)
leg_to_test = mig_right

for servo in leg_to_test:
	servos_right[servo["index"]].angle = None
	#  if servo["is_calibrated"]:
		#  continue

	#  time.sleep( 2 )

	#  right.servo[servo["index"]].angle = servo["actuation_range"]

	#  time.sleep( 2 )

	#  right.servo[servo["index"]].angle = 0
