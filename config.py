# ------------------------------------------------------------------------------
# Environmental Monitoring and Management for Archives (EMMA) Project
#
# Configures system modules and user preferences for sensor
#
# (c) 2020 Jonathan Isip, Quezon City, Philippines
# A project with the University of the Philippines School of Library and Information Studies
# Released under GNU General Public License (GPL v3.0) 
# email nathan@slis.upd.edu.ph
# ------------------------------------------------------------------------------

# Identify sensor for database
sensor_id = 001
sensor_name = "Reading Room"
# sensor location
# sensor description


# Select which modules are active

humidex_set = True
light_set = True
accel_set = True
sound_set = True
gas_set = True
user_set = True

# Divides user count by 2 when True for bidirectional passages

user_bi = True

# Enable audible and led alerts

alerts_set = True
audible_alert_set = True
led_alert_set = True

# Select threshold preferences for system alerts

temp_alert_low = 13				# Sets alert threshold for low temperature [-40 to 80 deg Celsius]
temp_alert_high = 20			# Sets alert threshold for high temperature [-40 to 80 deg Celsius, must be higher than temp_alert_low]
hum_alert_low = 35				# Sets alert threshold for low humidity [0-100%]
hum_alert_high = 60				# Sets alert threshold for high humidity [0-100%, must be higher than hum_alert_low]
vlum_alert = 165				# Sets alert threshold for high luminosity of visible light
uv_alert = 75					# Sets alert threshold for high UV light [mW/m2]
accel_alert	= 0.039				# Sets alert threshold for high acceleration [abs(16g), this is just the audible alert, event logging starts at 0.014g]
noise_alert = 50				# Sets alert threshold for high noise level [dB]
comb_alert = 0					# Sets alert threshold for high combustible gas level
pol_alert = 0					# Sets alert threshold for high pollutant gas level

# DB config
db_host = "localhost"
db_user = "pi"
db_password = "raspberry"
db_name = "emma"