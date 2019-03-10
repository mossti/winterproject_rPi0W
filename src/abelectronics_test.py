# heavily inspired by https://www.abelectronics.co.uk/kb/article/1078/generating-a-pwm-signal

from ServoPi import PWM
import time
pwm = PWM(0x40)

pwm.set_pwm_freq(50)


ts = 0.2

#output_enable()

low = 205
mid = 307
high = 410

i = 1


while i < 13:
	pwm.set_pwm(i, 0, mid)

	time.sleep(ts)

	pwm.set_pwm(i, 0, low)

	time.sleep(ts)

	pwm.set_pwm(i, 0, mid)

	time.sleep(ts)

	pwm.set_pwm(i, 0, high)

	time.sleep(ts)

	pwm.set_pwm(i, 0, mid)

	i += 1




