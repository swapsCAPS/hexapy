import time

class Joint:
	def __init__(self, side, is_calibrated, index, pulse_width_range, actuation_range, resting):
		self.side = side

		self.servo = self.side.servo[index]

		self.servo.set_pulse_width_range(*pulse_width_range)

		self.servo.actuation_range = actuation_range

		self.positions = {
			"resting": resting
		}

		self.servo.angle = None

	def set_resting_pose(self):
		self.servo.angle = self.positions["resting"]

	def disable(self):
		self.servo.angle = None

	def sweep(self):
		actuation_range = self.servo.actuation_range
		angle           = self.servo.angle

		angle           = angle or self.positions["resting"]

		print(angle)

		for i in range(angle, actuation_range):
			self.servo.angle = i
			print(self.servo.angle)
			time.sleep(0.03)
		for i in range(actuation_range, angle, -1):
			self.servo.angle = i
			print(self.servo.angle)
			time.sleep(0.03)

class Leg:
	def __init__(self, side, pelvis, knee, ankle):
		self.side = side

		self.pelvis = Joint(side, **pelvis)
		self.knee   = Joint(side, **knee)
		self.ankle  = Joint(side, **ankle)

		self.joints = [
			self.pelvis,
			self.knee,
			self.ankle,
		]

	def reset_leg(self):
		for joint in joints:
			joint.set_resting_pose()

	def disable_leg(self):
		for joint in joints:
			joint.disable()


