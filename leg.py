class Leg:
	def __init__(self, side, pelvis, knee, ankle):
		self.side = side

		self.pelvis = self.side.servo[pelvis["index"]]
		self.knee   = self.side.servo[knee["index"]]
		self.ankle  = self.side.servo[ankle["index"]]

		self.knee.set_pulse_width_range(*knee["pulse_width_range"])
		self.knee.actuation_range = knee["actuation_range"]

		self.ankle.set_pulse_width_range(*ankle["pulse_width_range"])
		self.ankle.actuation_range = ankle["actuation_range"]

	def reset_leg(self):
		for servo in leg:
			self.side.servo[servo["index"]].angle = servo["resting"]

	def disable_leg(self):
		for servo in leg:
			self.side.servo[servo["index"]].angle = None
