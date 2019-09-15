import time
from adafruit_servokit import ServoKit
from leg import Leg

left  = ServoKit(channels=16, address=0x40)
right = ServoKit(channels=16, address=0x41)

front_right_config = {
	"pelvis": {
		"is_calibrated":     True,
		"index":             0,
		"pulse_width_range": [ 1600, 2500 ], # first is backward
		"actuation_range":   90,
		"resting":           60,
	},
	"knee": {
		"is_calibrated":     True,
		"index":             1,
		"pulse_width_range": [ 450, 2000 ], # first is downward
		"actuation_range":   130,
		"resting":           0,
	},
	"ankle": {
		"is_calibrated":     True,
		"index":             2,
		"pulse_width_range": [ 500, 2000 ], # first is inward
		"actuation_range":   130,
		"resting":           30,
	}
}

mid_right_config = {
	"pelvis": {
		"is_calibrated":     True,
		"index": 3,
		"pulse_width_range": [ 1300, 1900 ],
		"actuation_range":   90,
		"resting":           45,
	},
	"knee": {
		"is_calibrated":     True,
		"index": 4,
		"pulse_width_range": [ 510, 2000 ],
		"actuation_range":   130,
		"resting":           0,
	},
	"ankle": {
		"is_calibrated":     True,
		"index": 5,
		"pulse_width_range": [ 550, 2200 ],
		"actuation_range":   130,
		"resting":           30,
	}
}

back_right_config = {
	"pelvis": {
		"is_calibrated":     True,
		"index": 6,
		"pulse_width_range": [ 450, 1380 ],
		"actuation_range":   90,
		"resting":           45,
	},
	"knee": {
		"is_calibrated":     True,
		"index": 7,
		"pulse_width_range": [ 460, 2000 ],
		"actuation_range":   180,
		"resting":           0,
	},
	"ankle": {
		"is_calibrated":     True,
		"index": 8,
		"pulse_width_range": [ 750, 2050 ],
		"actuation_range":   130,
		"resting":           30,
	}
}

front_left_config = {
	"pelvis": {
		"is_calibrated":     True,
		"index": 15,
		"pulse_width_range": [ 550, 1350 ], # first is forward
		"actuation_range":   90,
		"resting":           45,
	},
	"knee": {
		"is_calibrated":     True,
		"index": 14,
		"pulse_width_range": [ 900, 2380 ], # first is upward
		"actuation_range":   130,
		"resting":           130,
	},
	"ankle": {
		"is_calibrated":     True,
		"index": 13,
		"pulse_width_range": [ 1100, 2650 ], # first is outward
		"actuation_range":   130,
		"resting":           90,
	}
}

mid_left_config = {
	"pelvis": {
		"is_calibrated":     True,
		"index": 12,
		"pulse_width_range": [ 1300, 1900 ],
		"actuation_range":   90,
		"resting":           45,
	},
	"knee": {
		"is_calibrated":     True,
		"index": 11,
		"pulse_width_range": [ 900, 2550 ], # first is upward
		"actuation_range":   130,
		"resting":           130,
	},
	"ankle": {
		"is_calibrated":     True,
		"index": 10,
		"pulse_width_range": [ 1000, 2650 ],
		"actuation_range":   130,
		"resting":           90,
	}
}

back_left_config = {
	"pelvis": {
		"is_calibrated":     True,
		"index": 9,
		"pulse_width_range": [ 1580, 2500 ],
		"actuation_range":   90,
		"resting":           60,
	},
	"knee": {
		"is_calibrated":     True,
		"index": 8,
		"pulse_width_range": [ 1200, 2730 ], # first is upward
		"actuation_range":   130,
		"resting":           130,
	},
	"ankle": {
		"is_calibrated":     True,
		"index": 7,
		"pulse_width_range": [ 1200, 2650 ],
		"actuation_range":   130,
		"resting":           90,
	}
}

front_right = Leg(right, **front_right_config)
mid_right   = Leg(right, **mid_right_config)
back_right  = Leg(right, **back_right_config)

front_left = Leg(left, **front_left_config)
mid_left   = Leg(left, **mid_left_config)
back_left  = Leg(left, **back_left_config)

# TODO state for each joint
# TODO Slow move

mid_right.ankle.sweep()
