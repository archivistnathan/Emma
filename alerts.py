# ------------------------------------------------------------------------------
# Environmental Monitoring and Management for Archives (EMMA) Project
#
# Functions for controlling alerts
#
# (c) 2020 Jonathan Isip, Quezon City, Philippines
# A project with the University of the Philippines School of Library and Information Studies
# Released under GNU General Public License (GPL v3.0) 
# email nathan@slis.upd.edu.ph
# ------------------------------------------------------------------------------

# use gpiozero library for controlling output devices
from gpiozero import LED
from gpiozero import RGBLED
from gpiozero import TonalBuzzer

# import config and current sensor data values
import config
import capture

# Visual alerts
# RGB led for humidex alerts
humidex_led = RGBLED(16, 20, 21)
# Two-colour LED set 1 for illuminance
illum_led_R = LED(23)
illum_led_R = LED(24)
# Two-colour LED set 2 for acceleration and noise
accel_led = LED(5)
noise_led = LED(6)
# Two-colour LED set 3 for gas level
comb_led = LED(19)
pol_led = LED(26)


# Buzzer
buzz = TonalBuzzer(12)



def temp_alert_low_light():
	


temp_alert_high
hum_alert_low
hum_alert_high
vlum_alert
uv_alert
accel_alert
noise_alert
comb_alert
pol_alert


