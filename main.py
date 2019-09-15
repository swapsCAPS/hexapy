import time
from adafruit_servokit import ServoKit
from leg import Leg

left  = ServoKit(channels=16, address=0x40)
right = ServoKit(channels=16, address=0x41)

positions_right = {
	"knee": {
		"lifted": 20, # higher num is higher lift
		"rested": 0,
	},
	"ankle": {
		"lifted": 65,
		"rested": 30,
	}
}

positions_left = {
	"knee": {
		"lifted": 110, # lower num is higher lift
		"rested": 130,
	},
	"ankle": {
		"lifted": 65,
		"rested": 90,
	}
}

front_right_config = {
	"pelvis": {
		"is_calibrated":     True,
		"index":             0,
		"pulse_width_range": [ 1600, 2500 ], # first is backward
		"actuation_range":   90,
		"positions": {
			"rested":        60,
			"stepped_front": 60,
			"stepped_back":  40,
		}
	},
	"knee": {
		"is_calibrated":     True,
		"index":             1,
		"pulse_width_range": [ 450, 2000 ], # first is downward
		"actuation_range":   130,
		"positions": {
			**positions_right["knee"],
		}
	},
	"ankle": {
		"is_calibrated":     True,
		"index":             2,
		"pulse_width_range": [ 500, 2000 ], # first is inward
		"actuation_range":   130,
		"positions": {
			**positions_right["ankle"],
		}
	}
}

mid_right_config = {
	"pelvis": {
		"is_calibrated":     True,
		"index": 3,
		"pulse_width_range": [ 1300, 1900 ],
		"actuation_range":   90,
		"positions": {
			"rested":       45,
			"stepped_front": 60,
			"stepped_back":  30,
		}
	},
	"knee": {
		"is_calibrated":     True,
		"index": 4,
		"pulse_width_range": [ 510, 2000 ],
		"actuation_range":   130,
		"positions": {
			**positions_right["knee"],
		}
	},
	"ankle": {
		"is_calibrated":     True,
		"index": 5,
		"pulse_width_range": [ 550, 2200 ],
		"actuation_range":   130,
		"positions": {
			**positions_right["ankle"],
		}
	}
}

back_right_config = {
	"pelvis": {
		"is_calibrated":     True,
		"index": 6,
		"pulse_width_range": [ 450, 1380 ],
		"actuation_range":   90,
		"positions": {
			"rested":        45,
			"stepped_front": 60,
			"stepped_back":  40,
		}
	},
	"knee": {
		"is_calibrated":     True,
		"index": 7,
		"pulse_width_range": [ 460, 2000 ],
		"actuation_range":   180,
		"positions": {
			**positions_right["knee"],
		}
	},
	"ankle": {
		"is_calibrated":     True,
		"index": 8,
		"pulse_width_range": [ 750, 2050 ],
		"actuation_range":   130,
		"positions": {
			**positions_right["ankle"],
		}
	}
}

front_left_config = {
	"pelvis": {
		"is_calibrated":     True,
		"index": 15,
		"pulse_width_range": [ 550, 1350 ], # first is forward
		"actuation_range":   90,
		"positions": {
			"rested":       45,
			"stepped_front": 40,
			"stepped_back":  60,
		}
	},
	"knee": {
		"is_calibrated":     True,
		"index": 14,
		"pulse_width_range": [ 900, 2380 ], # first is upward
		"actuation_range":   130,
		"positions": {
			**positions_left["knee"],
			"rested": 130,
		}
	},
	"ankle": {
		"is_calibrated":     True,
		"index": 13,
		"pulse_width_range": [ 1100, 2650 ], # first is outward
		"actuation_range":   130,
		"positions": {
			**positions_left["ankle"],
		}
	}
}

mid_left_config = {
	"pelvis": {
		"is_calibrated":     True,
		"index": 12,
		"pulse_width_range": [ 1300, 1900 ],
		"actuation_range":   90,
		"positions": {
			"rested":       45,
			"stepped_front": 30,
			"stepped_back":  60,
		}
	},
	"knee": {
		"is_calibrated":     True,
		"index": 11,
		"pulse_width_range": [ 900, 2550 ], # first is upward
		"actuation_range":   130,
		"positions": {
			**positions_left["knee"],
		}
	},
	"ankle": {
		"is_calibrated":     True,
		"index": 10,
		"pulse_width_range": [ 1000, 2650 ],
		"actuation_range":   130,
		"positions": {
			**positions_left["ankle"],
		}
	}
}

back_left_config = {
	"pelvis": {
		"is_calibrated":     True,
		"index":             9,
		"pulse_width_range": [ 1580, 2500 ],
		"actuation_range":   90,
		"positions": {
			"rested":       60,
			"stepped_front": 40,
			"stepped_back":  60,
		}
	},
	"knee": {
		"is_calibrated":     True,
		"index":             8,
		"pulse_width_range": [ 1200, 2730 ], # first is upward
		"actuation_range":   130,
		"positions": {
			**positions_left["knee"],
		}
	},
	"ankle": {
		"is_calibrated":     True,
		"index":             7,
		"pulse_width_range": [ 1200, 2650 ],
		"actuation_range":   130,
		"positions": {
			**positions_left["ankle"],
		}
	}
}

front_right = Leg(right, **front_right_config)
mid_right   = Leg(right, **mid_right_config)
back_right  = Leg(right, **back_right_config)

front_left = Leg(left, **front_left_config)
mid_left   = Leg(left, **mid_left_config)
back_left  = Leg(left, **back_left_config)

legs = [
	front_right,
	mid_right,
	back_right,
	front_left,
	mid_left,
	back_left,
]

set_a = [
	front_right,
	back_right,
	mid_left,
]

set_b = [
	mid_right,
	front_left,
	back_left,
]

def move_set_a_forward():
	for leg in set_a:
		leg.move_forwards()

def move_set_a_backward():
	for leg in set_a:
		leg.move_backwards()

def lift_set_a():
	for leg in set_a:
		leg.lift()

def lower_set_a():
	for leg in set_a:
		leg.lower()

def move_set_b_forward():
	for leg in set_b:
		leg.move_forwards()

def move_set_b_backward():
	for leg in set_b:
		leg.move_backwards()

def lift_set_b():
	for leg in set_b:
		leg.lift()

def lower_set_b():
	for leg in set_b:
		leg.lower()

# TODO Slow move

for leg in legs:
	leg.set_rested_pose()

time.sleep(0.5)

lift_set_a()

time.sleep(0.5)

move_set_b_backward()
time.sleep(0.1)
move_set_a_forward()

time.sleep(0.5)

for i in range(4):
	lower_set_a()

	time.sleep(0.5)

	lift_set_b()

	time.sleep(0.5)

	move_set_a_backward()
	time.sleep(0.1)
	move_set_b_forward()

	time.sleep(0.5)

	lower_set_b()

	time.sleep(0.5)

	lift_set_a()

	time.sleep(0.5)

	move_set_a_forward()
	time.sleep(0.1)
	move_set_b_backward()

	time.sleep(0.5)

time.sleep(0.5)

for leg in legs:
	leg.set_rested_pose()

time.sleep(0.5)

for leg in legs:
	leg.disable()
