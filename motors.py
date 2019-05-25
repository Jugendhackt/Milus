from pins import * 
import machine
import math

def setup():
	global pwm_left_motor
	global pwm_right_motor
	global pwm_height_motor
	global move_up_pin
	global move_down_pin

	pwm_left_motor = machine.PWM(machine.Pin(LEFT_MOTOR_PIN, machine.Pin.OUT))
	pwm_right_motor = machine.PWM(machine.Pin(RIGHT_MOTOR_PIN, machine.Pin.OUT))
	pwm_height_motor = machine.PWM(machine.Pin(HEIGHT_MOTOR_PIN, machine.Pin.OUT))
	move_up_pin = machine.Pin(MOVE_UP_PIN, machine.Pin.OUT)
	move_down_pin = machine.Pin(MOVE_DOWN_PIN, machine.Pin.OUT)

	pwm_left_motor.freq(2000)
	pwm_right_motor.freq(2000)
	pwm_height_motor.freq(2000)

	set_power(0,0,0,0)

def set_power(left, right, height, up):
	pwm_left_motor.duty(math.floor(left))
	pwm_right_motor.duty(math.floor(right))

	#Wichtig: erst aus, dann anschalten -> sonst kurzschluss
	if up:
		move_down_pin(False)
		move_up_pin(True)
	else:
		move_up_pin(False)
		move_down_pin(True)

	pwm_height_motor.duty(math.floor(height))