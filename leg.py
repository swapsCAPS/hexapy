import time

class Joint:
	def __init__(self, side, is_calibrated, index, pulse_width_range, actuation_range, positions):
		self.side = side

		self.servo = self.side.servo[index]

		self.servo.set_pulse_width_range(*pulse_width_range)

		self.servo.actuation_range = actuation_range

		self.positions = positions

		self.servo.angle = None

	def set_position(self, position):
		self.servo.angle = self.positions[position]

	def set_rested_pose(self):
		self.servo.angle = self.positions["rested"]

	def disable(self):
		self.servo.angle = None

	def sweep(self):
		actuation_range = self.servo.actuation_range
		angle           = self.servo.angle

		angle           = angle or self.positions["rested"]

		for i in range(angle, actuation_range):
			self.servo.angle = i
			time.sleep(0.03)
		for i in range(actuation_range, angle, -1):
			self.servo.angle = i
			time.sleep(0.03)

# For left and for right we have 3 types of legs
# So we should be able to define movements in a pretty abstract way
# is_left could define the step direction.
# Pelvis is the important one. Can we just use 'actuation_range'? Not really as we go too far sometimes.
# But then we could also recalibrate to have back and front legs make smaller steps

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

	def move_forwards(self):
		self.pelvis.set_position("stepped_front")

	def move_backwards(self):
		self.pelvis.set_position("stepped_back")

	def lower(self):
		self.knee.set_position("rested")
		self.ankle.set_position("rested")

	def lift(self):
		self.knee.set_position("lifted")
		self.ankle.set_position("lifted")

	def set_rested_pose(self):
		for joint in self.joints:
			joint.set_rested_pose()

	def disable(self):
		for joint in self.joints:
			joint.disable()


