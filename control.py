from motors import set_power, setup as intern_setup

def setup():
	intern_setup()


def move(power, direction, height):
	'''Move the airship.
		* power: integer 0 - 1023 (power of the stronger motor)
		* direction: integer -127 - +128 (diff to 0 indicates ration of power of stronger and weaker motor.
										 (when direction < 0 -> move left -> right motor)
		* height: integer -127 - +128 (goes down when < 0)'''


	#=======================================
	#		Power

	left, right = (power, power)


	#=======================================
	#		Direction

	fraction =  1 - abs(direction) / 127

	if(direction < 0): 
		#steer left
		#right motor pulls stronger
		#left motor strength decreased

		left *= fraction
	elif (direction > 0):
		right *= fraction


	#=======================================
	#		Height

	up = height > 0
	height = abs(height) * 8

	set_power(left, right, height, up)

	print("left: " + str(left))
	print("right: " + str(right))
	print("height: " + str(height))
	print("up: " + str(up))