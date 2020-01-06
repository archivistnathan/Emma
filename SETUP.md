# EMMA Set-up Guide

## System Requirements
- Raspberry Pi 3 B+ or later / Raspberry Pi Zero W/WH
- 3A power supply or higher for Raspberry Pi
- 16GB or bigger microSD card with latest Raspbian OS with Python 3.X (installed by default)
- 40-pin connector cable for RPi GPIO / RPi breakout board
- prototyping board / breadboard / universal PCB / Veroboard / custom PCB for mounting sensor modules
- sensor modules for:
  1. Temperature and Humidity (Humidex)
  2. Illuminance
  3. Acceleration
  4. Sound pressure
  5. Gas detection
  6. User counter
- Database server for logging (you can use the RPi locally or send it to a different server)
  
## External Python Libraries used
- Adafruit_DHT

## Set-up

1. Assemble the Raspberry Pi hardware and install the latest version of Raspbian

2. Connect the sensor modules to the Raspberry Pi GPIO. You may use a breakout board for easier connections. Some modules may come without the headers pre-attached. These need to be soldered. Do not however solder the headers directly into the PCB. Instead use mounts or female headers to allow for rapid module replacement in the future once sensitivity or accuracy has drifted. Refer to the connection diagram for pin numbering. 

3. Download the github repository to your RPi. Test modules once connected with the codes in the sensor_debug folder.

4. 