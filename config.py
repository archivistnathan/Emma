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

# Select which modules are active

humidex_set = TRUE
light_set = TRUE
accel_set = TRUE
sound_set = TRUE
gas_set = TRUE
user_set = TRUE

# Select threshold preferences for system alerts

temp_alert_low					# Sets alert threshold for low temperature [-40 to 80 deg Celsius]
temp_alert_high					# Sets alert threshold for high temperature [-40 to 80 deg Celsius, must be higher than temp_alert_low]
hum_alert_low					# Sets alert threshold for low humidity
hum_alert_high					# Sets alert threshold for high humidity
vlum_alert						# Sets alert threshold for high luminosity of visible light [must be higher than hum_alert_low]
uv_alert						# Sets alert threshold for high UV light index
accel_alert						# Sets alert threshold for high acceleration
noise_alert						# Sets alert threshold for high noise level
comb_alert						# Sets alert threshold for high combustible gas level
pol_alert						# Sets alert threshold for high pollutant gas level