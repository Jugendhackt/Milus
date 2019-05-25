from pins import * 
import machine

#ungesetzt
pwm_left_motor, pwm_right_motor, pwm_up_motor, pwm_down_motor = False

def setup() {
	pwm_left_motor = machine.PWM(machine.Pin(LEFT_MOTOR_PIN, machine.Pin.OUT))
	pwm_right_motor = machine.PWM(machine.Pin(RIGHT_MOTOR_PIN, machine.Pin.OUT))
	pwm_up_motor = machine.PWM(machine.Pin(UP_MOTOR_PIN, machine.Pin.OUT))
	pwm_down_motor = machine.PWM(machine.Pin(DOWN_MOTOR_PIN, machine.Pin.OUT))

	pwm_left_motor.freq(2000)
	pwm_right_motor.freq(2000)
	pwm_up_motor.freq(2000)
	pwm_down_motor.freq(2000)
}

def set_power(left, right, height, up) {
	pwm_left_motor.duty(left)
	pwm_right_motor.duty(right)

	if(up) {
		pwm_down_motor.duty(0)
		pwm_up_motor.duty(height)
	} else {
		pwm_up_motor.duty(0)
		pwm_down_motor.duty(height)
	}
}