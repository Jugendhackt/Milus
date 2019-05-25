from motors import set_powers, setup as intern_setup

def setup() {
	intern_setup()
}

def move(power, direction, height):
	'''Move the airship.
		* power: integer 0 - 1023 (power of the stronger motor)
		* direction: integer -127 - +128 (diff to 0 indicates ration of power of stronger and weaker motor.
										 (when direction < 0 -> move left -> right motor)
		* height: integer -127 - +128 (goes down when < 0)'''


	#=======================================
	#		Power

	left, right = power


	#=======================================
	#		Direction

	fraction =  abs(direction) / 127

	if(direction < 0) { 
		#steer left
		#right motor pulls stronger
		#left motor strength decreased

		left *= fraction
	} else if (direction > 0) {
		right *= fraction
	}


	#=======================================
	#		Height

	height = abs(height) * 8
	up = height > 0


	set_powers(left, right, height, up)